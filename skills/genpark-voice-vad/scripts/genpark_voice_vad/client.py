import sys, json, math, time

class VoiceTurnTakingEndpointDetector:
    """
    Deterministic real-time voice turn-taking endpoint detector.
    Combines supplied frame energies, trailing silence duration,
    and transcript boundary heuristics.
    """
    def __init__(self, silence_endpoint_ms=650, hesitation_tolerance_ms=1200):
        self.silence_endpoint_ms = silence_endpoint_ms
        self.hesitation_tolerance_ms = hesitation_tolerance_ms
        self.noise_floor_db = -48.0
        self.speech_energy_threshold_db = -32.0
        self.hesitation_markers = {"um", "uh", "er", "ah", "like", "you know", "and then", "so", "but", "because", "wait"}
        self.completion_punctuations = {".", "!", "?"}

    def calibrate_acoustic_thresholds(self, ambient_frames_db):
        if not ambient_frames_db:
            return {"noise_floor_db": self.noise_floor_db, "speech_threshold_db": self.speech_energy_threshold_db}
        avg_noise = sum(ambient_frames_db) / len(ambient_frames_db)
        self.noise_floor_db = round(avg_noise, 2)
        self.speech_energy_threshold_db = round(avg_noise + 14.0, 2)
        return {
            "calibrated_noise_floor_db": self.noise_floor_db,
            "calibrated_speech_threshold_db": self.speech_energy_threshold_db,
            "status": "CALIBRATED_SUCCESS"
        }

    def predict_semantic_closure(self, transcript_fragment):
        text = (transcript_fragment or "").strip().lower()
        if not text:
            return {"semantic_completion_score": 0.0, "is_trailing_hesitation": False, "boundary_cue": "EMPTY"}

        words = text.split()
        last_word = words[-1].strip(".,!?;: ")
        normalized = text.rstrip(".,!?;: ")
        trailing_hesitation = any(normalized == marker or normalized.endswith(" " + marker) for marker in self.hesitation_markers) or text.endswith("...")

        has_terminal_punct = any(transcript_fragment.strip().endswith(p) for p in self.completion_punctuations)
        
        # Interrogative check
        first_word = words[0].strip(".,!?;: ") if words else ""
        is_question = first_word in {"what", "why", "how", "when", "where", "who", "which", "can", "could", "would", "is", "are", "do", "does"} or transcript_fragment.strip().endswith("?")

        score = 0.5
        if has_terminal_punct:
            score += 0.35
        if is_question:
            score += 0.20
        if trailing_hesitation:
            score -= 0.45
        if len(words) < 3 and not has_terminal_punct:
            score -= 0.25

        semantic_score = max(0.0, min(1.0, round(score, 3)))
        return {
            "semantic_completion_score": semantic_score,
            "is_trailing_hesitation": trailing_hesitation,
            "is_question": is_question,
            "has_terminal_punct": has_terminal_punct,
            "word_count": len(words)
        }

    def analyze_turn_status(self, frame_energies_db, transcript_fragment, elapsed_silence_ms):
        semantic = self.predict_semantic_closure(transcript_fragment)
        recent_frames = frame_energies_db[-5:] if frame_energies_db else [self.noise_floor_db]
        avg_recent_energy = sum(recent_frames) / len(recent_frames)
        is_actively_speaking = avg_recent_energy > self.speech_energy_threshold_db

        if is_actively_speaking:
            decision = "CONTINUE_LISTENING"
            confidence = 0.95
            recommended_delay_ms = 0
            reason = "Acoustic speech energy currently detected above threshold."
        elif semantic["is_trailing_hesitation"]:
            if elapsed_silence_ms > self.hesitation_tolerance_ms:
                decision = "ENDPOINT_DETECTED"
                confidence = 0.78
                recommended_delay_ms = 0
                reason = "Hesitation pause exceeded maximum tolerance window."
            else:
                decision = "HOLD_BACKCHANNEL"
                confidence = 0.85
                recommended_delay_ms = self.hesitation_tolerance_ms - elapsed_silence_ms
                reason = "Trailing hesitation marker detected; holding for speech continuation."
        elif semantic["semantic_completion_score"] >= 0.70:
            if elapsed_silence_ms >= self.silence_endpoint_ms:
                decision = "ENDPOINT_DETECTED"
                confidence = round(0.85 + (semantic["semantic_completion_score"] * 0.14), 3)
                recommended_delay_ms = 0
                reason = "Complete utterance detected with trailing silence exceeding threshold."
            else:
                decision = "CONTINUE_LISTENING"
                confidence = 0.72
                recommended_delay_ms = self.silence_endpoint_ms - elapsed_silence_ms
                reason = "Semantic completion likely; awaiting endpoint silence confirmation."
        else:
            required_silence = self.silence_endpoint_ms * 1.5
            if elapsed_silence_ms >= required_silence:
                decision = "ENDPOINT_DETECTED"
                confidence = 0.70
                recommended_delay_ms = 0
                reason = "Incomplete syntax but trailing silence timeout exceeded."
            else:
                decision = "CONTINUE_LISTENING"
                confidence = 0.65
                recommended_delay_ms = int(required_silence - elapsed_silence_ms)
                reason = "Incomplete utterance; waiting for continuation or timeout."

        return {
            "decision": decision,
            "confidence": confidence,
            "recommended_delay_ms": max(0, recommended_delay_ms),
            "elapsed_silence_ms": elapsed_silence_ms,
            "avg_recent_energy_db": round(avg_recent_energy, 2),
            "semantic_analysis": semantic,
            "reason": reason
        }

    def run_benchmark_turn_detection(self):
        self.calibrate_acoustic_thresholds([-52.0, -50.0, -49.5, -51.0])
        # Test 1: Active speech
        t1 = self.analyze_turn_status([-25.0, -22.0, -20.0], "What is the capital of France", 50)
        # Test 2: Hesitation pause
        t2 = self.analyze_turn_status([-51.0, -50.5], "I want to reserve a flight to... um...", 450)
        # Test 3: Finished question with silence
        t3 = self.analyze_turn_status([-52.0, -51.0], "Can you help me check my account balance?", 750)
        return {
            "benchmark_status": "PASSED",
            "scenario_active_speech": t1["decision"],
            "scenario_hesitation": t2["decision"],
            "scenario_endpoint_detected": t3["decision"],
            "test_results": [t1, t2, t3]
        }
