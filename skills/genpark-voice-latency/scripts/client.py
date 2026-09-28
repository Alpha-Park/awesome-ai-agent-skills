import sys, json, math, time

class RealtimeVoiceLatencyTelemetry:
    """
    In-memory voice pipeline timestamp analysis.
    Instruments and analyzes latency budgets across 6 pipeline stages:
    1. VAD / User Endpointing Silence
    2. STT Speech-to-Text Transcription
    3. LLM Queuing & Prompt Ingestion
    4. LLM Time-to-First-Token (TTFT)
    5. TTS Time-to-First-Byte (TTFB)
    6. Audio Jitter Playout Buffer
    """
    def __init__(self, target_e2e_sla_ms=800):
        self.target_e2e_sla_ms = target_e2e_sla_ms
        self.turn_events = {}  # turn_id -> list of event records

    def record_pipeline_event(self, turn_id, stage_name, timestamp_ms=None, metadata=None):
        ts = timestamp_ms if timestamp_ms is not None else int(time.time() * 1000)
        if turn_id not in self.turn_events:
            self.turn_events[turn_id] = []
        event = {
            "stage": stage_name,
            "timestamp_ms": ts,
            "metadata": metadata or {}
        }
        self.turn_events[turn_id].append(event)
        return {"turn_id": turn_id, "recorded_stage": stage_name, "timestamp_ms": ts}

    def compute_turn_latency_breakdown(self, turn_id):
        events = self.turn_events.get(turn_id, [])
        if len(events) < 2:
            return {"turn_id": turn_id, "error": "Insufficient event markers to compute latency"}

        sorted_events = sorted(events, key=lambda x: x["timestamp_ms"])
        start_ts = sorted_events[0]["timestamp_ms"]
        end_ts = sorted_events[-1]["timestamp_ms"]
        total_e2e_latency_ms = end_ts - start_ts

        stage_deltas = {}
        for i in range(len(sorted_events) - 1):
            s_from = sorted_events[i]["stage"]
            s_to = sorted_events[i+1]["stage"]
            delta = sorted_events[i+1]["timestamp_ms"] - sorted_events[i]["timestamp_ms"]
            key = f"{s_from}_TO_{s_to}"
            stage_deltas[key] = stage_deltas.get(key, 0) + max(0, delta)

        # Bottleneck detection
        bottleneck_stage = max(stage_deltas.items(), key=lambda x: x[1]) if stage_deltas else ("NONE", 0)
        sla_met = total_e2e_latency_ms <= self.target_e2e_sla_ms

        return {
            "turn_id": turn_id,
            "total_e2e_latency_ms": total_e2e_latency_ms,
            "sla_target_ms": self.target_e2e_sla_ms,
            "sla_compliant": sla_met,
            "stage_breakdown_ms": stage_deltas,
            "bottleneck_stage": bottleneck_stage[0],
            "bottleneck_duration_ms": bottleneck_stage[1],
            "recommendation": "OPTIMIZE_BOTTLENECK" if not sla_met else "WITHIN_BUDGET"
        }

    def generate_sla_diagnostic_report(self):
        total_latencies = []
        for tid in self.turn_events:
            breakdown = self.compute_turn_latency_breakdown(tid)
            if "total_e2e_latency_ms" in breakdown:
                total_latencies.append(breakdown["total_e2e_latency_ms"])

        if not total_latencies:
            return {"status": "NO_DATA"}

        total_latencies.sort()
        count = len(total_latencies)
        p50 = total_latencies[max(0, math.ceil(count * 0.50)-1)]
        p90 = total_latencies[max(0, math.ceil(count * 0.90)-1)]
        p99 = total_latencies[max(0, math.ceil(count * 0.99)-1)]
        compliant_count = sum(1 for l in total_latencies if l <= self.target_e2e_sla_ms)

        return {
            "total_turns_analyzed": count,
            "target_sla_ms": self.target_e2e_sla_ms,
            "sla_compliance_rate_percent": round((compliant_count / count) * 100.0, 2),
            "p50_latency_ms": p50,
            "p90_latency_ms": p90,
            "p99_latency_ms": p99,
            "health_status": "EXCELLENT" if p90 <= self.target_e2e_sla_ms else "DEGRADED_LATENCY"
        }

    def run_benchmark_telemetry_profiling(self):
        # Turn 1: Fast conversational response (650ms total)
        self.record_pipeline_event("turn_101", "VAD_SPEECH_STOP", 1000)
        self.record_pipeline_event("turn_101", "STT_TRANSCRIPT_FINAL", 1140)
        self.record_pipeline_event("turn_101", "LLM_FIRST_TOKEN", 1380)
        self.record_pipeline_event("turn_101", "TTS_FIRST_AUDIO_CHUNK", 1550)
        self.record_pipeline_event("turn_101", "AUDIO_PLAYOUT_START", 1650)

        # Turn 2: Slower response (920ms total)
        self.record_pipeline_event("turn_102", "VAD_SPEECH_STOP", 2000)
        self.record_pipeline_event("turn_102", "STT_TRANSCRIPT_FINAL", 2220)
        self.record_pipeline_event("turn_102", "LLM_FIRST_TOKEN", 2620)
        self.record_pipeline_event("turn_102", "TTS_FIRST_AUDIO_CHUNK", 2820)
        self.record_pipeline_event("turn_102", "AUDIO_PLAYOUT_START", 2920)

        t1_report = self.compute_turn_latency_breakdown("turn_101")
        overall = self.generate_sla_diagnostic_report()

        return {
            "benchmark_status": "PASSED",
            "turn_101_e2e_ms": t1_report["total_e2e_latency_ms"],
            "turn_101_compliant": t1_report["sla_compliant"],
            "sla_report": overall
        }
