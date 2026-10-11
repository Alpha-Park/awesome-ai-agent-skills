# Awesome AI Agent Skills

A searchable, categorized index of **718 public GenPark skill repositories**.
Browse source code, examples and MCP integrations maintained by [GenPark](https://genpark.ai).

Repository visibility and names were checked against GitHub on **2026-09-28**.
This index does not certify every implementation as production-ready or registry-approved.
Dependencies and installation steps vary by repository.

## Installable Agent Skills

Ten self-contained skills include `SKILL.md` and local Python helpers. Python 3.9+; no runtime dependencies. Eight MCP-backed bundles include tool schemas and examples; two data-processing skills use direct Python helpers with regression tests. These installable bundles are distinct from the broader repository index below.

```sh
npx skills add Alpha-Park/awesome-ai-agent-skills
```

Choose individual skills interactively, or append `--skill genpark-ocr-table` to select one.

- [genpark-voice-vad](skills/genpark-voice-vad/SKILL.md): Energy and transcript heuristics for voice turn endpoint detection.
- [genpark-jitter-buffer](skills/genpark-jitter-buffer/SKILL.md): Packet ordering simulation and inter-arrival jitter telemetry.
- [genpark-financial-audit](skills/genpark-financial-audit/SKILL.md): Arithmetic consistency checks for supplied financial statement data.
- [genpark-ocr-table](skills/genpark-ocr-table/SKILL.md): Group supplied OCR text boxes into left-aligned table rows and columns. No image OCR is performed.
- [genpark-clause-references](skills/genpark-clause-references/SKILL.md): Extract English defined terms and explicit numbered references from supplied contract text; inspect dependency cycles. Regex heuristics, not legal analysis.
- [genpark-chart-coordinates](skills/genpark-chart-coordinates/SKILL.md): Calibrate linear chart axes and convert supplied bar or scatter pixel coordinates to values. No image recognition or logarithmic axes.
- [genpark-voice-latency](skills/genpark-voice-latency/SKILL.md): Record supplied voice pipeline timestamps in session memory and calculate latency, bottlenecks and nearest-rank percentiles. No automatic instrumentation.
- [genpark-barge-in](skills/genpark-barge-in/SKILL.md): Apply transcript, supplied echo score and duration rules to conversational interruptions; estimate playback truncation. No audio echo detection or playback control.
- [genpark-markdown-sections](skills/genpark-markdown-sections/SKILL.md): Split ATX Markdown sections with heading paths, fenced-code preservation and source line ranges.
- [genpark-json-record-dedup](skills/genpark-json-record-dedup/SKILL.md): Deduplicate JSON records by explicit identity fields with stable order and duplicate provenance.

## Start here

These three packages have focused regression tests and an official MCP client stdio integration check:

| Package | Purpose | Source and release |
| --- | --- | --- |
| `genpark-voice-vad` | Energy/transcript endpoint heuristics; accepts precomputed energies, not raw audio | [Voice endpoint detector](https://github.com/Alpha-Park/genpark-voice-turn-taking-endpoint-detector-skill) |
| `genpark-jitter-buffer` | Packet metadata ordering and jitter simulation; no audio codec or WebRTC transport | [Jitter buffer](https://github.com/Alpha-Park/genpark-audio-packet-jitter-resilience-buffer-skill) |
| `genpark-financial-audit` | Numeric statement consistency and cross-footing checks | [Financial validation](https://github.com/Alpha-Park/genpark-complex-financial-formula-audit-validator-skill) |

Install the wheel from the respective GitHub Release, or use its MCPB bundle with a compatible client.
PyPI publication and third-party registry acceptance are tracked independently in each repository.

## Published on Smithery

Eight local Python MCPB servers are published as of 2026-09-28. Each has regression tests and an official MCP SDK connection check. Python 3.9+ is required. These are downloadable local tools, not hosted services.

| Server | Tools | Actual scope |
| --- | --- | --- |
| [genpark-voice-vad](https://smithery.ai/servers/krispang1020/genpark-voice-vad) | 4 | Energy and transcript heuristics for voice turn endpoint detection. |
| [genpark-jitter-buffer](https://smithery.ai/servers/krispang1020/genpark-jitter-buffer) | 4 | Packet ordering simulation and inter-arrival jitter telemetry. |
| [genpark-financial-audit](https://smithery.ai/servers/krispang1020/genpark-financial-audit) | 4 | Arithmetic consistency checks for supplied financial statement data. |
| [genpark-ocr-table](https://smithery.ai/servers/krispang1020/genpark-ocr-table) | 3 | Group supplied OCR text boxes into left-aligned table rows and columns. No image OCR is performed. |
| [genpark-clause-references](https://smithery.ai/servers/krispang1020/genpark-clause-references) | 5 | Extract English defined terms and explicit numbered references from supplied contract text; inspect dependency cycles. Regex heuristics, not legal analysis. |
| [genpark-chart-coordinates](https://smithery.ai/servers/krispang1020/genpark-chart-coordinates) | 4 | Calibrate linear chart axes and convert supplied bar or scatter pixel coordinates to values. No image recognition or logarithmic axes. |
| [genpark-voice-latency](https://smithery.ai/servers/krispang1020/genpark-voice-latency) | 4 | Record supplied voice pipeline timestamps in session memory and calculate latency, bottlenecks and nearest-rank percentiles. No automatic instrumentation. |
| [genpark-barge-in](https://smithery.ai/servers/krispang1020/genpark-barge-in) | 4 | Apply transcript, supplied echo score and duration rules to conversational interruptions; estimate playback truncation. No audio echo detection or playback control. |

## Browse by category

- [Voice and audio](#voice-and-audio) (20)
- [Documents and financial data](#documents-and-financial-data) (21)
- [Security and permissions](#security-and-permissions) (13)
- [Memory and retrieval](#memory-and-retrieval) (43)
- [Vision and multimodal](#vision-and-multimodal) (27)
- [Personal productivity](#personal-productivity) (24)
- [Commerce and marketing](#commerce-and-marketing) (23)
- [Agent workflows and reliability](#agent-workflows-and-reliability) (547)

Download [catalog.json](catalog.json) to filter the full index programmatically.

## Voice and audio

- [Audio packet jitter resilience buffer](https://github.com/Alpha-Park/genpark-audio-packet-jitter-resilience-buffer-skill)
- [Conversational barge in interruption arbitrator](https://github.com/Alpha-Park/genpark-conversational-barge-in-interruption-arbitrator-skill)
- [Conversational filler audio latency masker](https://github.com/Alpha-Park/genpark-conversational-filler-audio-latency-masker-skill)
- [Gossip protocol epidemic information dissemination](https://github.com/Alpha-Park/genpark-gossip-protocol-epidemic-information-dissemination-skill)
- [Gossip protocol epidemic state sync](https://github.com/Alpha-Park/genpark-gossip-protocol-epidemic-state-sync-skill)
- [Label noise confident learning pruner](https://github.com/Alpha-Park/genpark-label-noise-confident-learning-pruner-skill)
- [Low latency prosody sentiment modulator](https://github.com/Alpha-Park/genpark-low-latency-prosody-sentiment-modulator-skill)
- [Multimodal audio emotion valence detector](https://github.com/Alpha-Park/genpark-multimodal-audio-emotion-valence-detector-skill)
- [Realtime jitter buffer audio packet scheduler](https://github.com/Alpha-Park/genpark-realtime-jitter-buffer-audio-packet-scheduler-skill)
- [Realtime voice agent latency telemetry](https://github.com/Alpha-Park/genpark-realtime-voice-agent-latency-telemetry-skill)
- [Realtime voice noise suppression gate](https://github.com/Alpha-Park/genpark-realtime-voice-noise-suppression-gate-skill)
- [Realtime voice turn taking orchestrator](https://github.com/Alpha-Park/genpark-realtime-voice-turn-taking-orchestrator-skill)
- [Speech filler word remover cleaner](https://github.com/Alpha-Park/genpark-speech-filler-word-remover-cleaner-skill)
- [Telephony silence latency vad calibrator](https://github.com/Alpha-Park/genpark-telephony-silence-latency-vad-calibrator-skill)
- [Voice call dtmf sip telephony router](https://github.com/Alpha-Park/genpark-voice-call-dtmf-sip-telephony-router-skill)
- [Voice call dtmf tone ivr navigator](https://github.com/Alpha-Park/genpark-voice-call-dtmf-tone-ivr-navigator-skill)
- [Voice telephony bargein interruption coordinator](https://github.com/Alpha-Park/genpark-voice-telephony-bargein-interruption-coordinator-skill)
- [Voice turn taking endpoint detector](https://github.com/Alpha-Park/genpark-voice-turn-taking-endpoint-detector-skill)
- [Voice turn taking endpointing detector](https://github.com/Alpha-Park/genpark-voice-turn-taking-endpointing-detector-skill)
- [Zero noise extrapolation zne](https://github.com/Alpha-Park/genpark-zero-noise-extrapolation-zne-skill)

## Documents and financial data

- [Chord dht finger table lookup](https://github.com/Alpha-Park/genpark-chord-dht-finger-table-lookup-skill)
- [Complex financial formula audit validator](https://github.com/Alpha-Park/genpark-complex-financial-formula-audit-validator-skill)
- [Contract net protocol cnp task clearing](https://github.com/Alpha-Park/genpark-contract-net-protocol-cnp-task-clearing-skill)
- [Document redaction pii scrubber](https://github.com/Alpha-Park/genpark-document-redaction-pii-scrubber-skill)
- [Document visual reading order topological sorter](https://github.com/Alpha-Park/genpark-document-visual-reading-order-topological-sorter-skill)
- [Evolutionary stable strategy replicator dynamics](https://github.com/Alpha-Park/genpark-evolutionary-stable-strategy-replicator-dynamics-skill)
- [Flatbuffers zero copy vtable serializer](https://github.com/Alpha-Park/genpark-flatbuffers-zero-copy-vtable-serializer-skill)
- [Gale shapley stable matching](https://github.com/Alpha-Park/genpark-gale-shapley-stable-matching-skill)
- [Genoffice document agent suite](https://github.com/Alpha-Park/genpark-genoffice-document-agent-suite-skill)
- [Hybrid bounding box ocr table reconstructor](https://github.com/Alpha-Park/genpark-hybrid-bounding-box-ocr-table-reconstructor-skill)
- [Kademlia dht routing table xor metric](https://github.com/Alpha-Park/genpark-kademlia-dht-routing-table-xor-metric-skill)
- [Legal clause cross reference resolver](https://github.com/Alpha-Park/genpark-legal-clause-cross-reference-resolver-skill)
- [Lsm tree compaction memtable engine](https://github.com/Alpha-Park/genpark-lsm-tree-compaction-memtable-engine-skill)
- [Lsm tree sstable compactor](https://github.com/Alpha-Park/genpark-lsm-tree-sstable-compactor-skill)
- [Multi table schema foreign key inferrer](https://github.com/Alpha-Park/genpark-multi-table-schema-foreign-key-inferrer-skill)
- [Multimodal vision table structural extractor](https://github.com/Alpha-Park/genpark-multimodal-vision-table-structural-extractor-skill)
- [Ocr confidence score spellcheck regularizer](https://github.com/Alpha-Park/genpark-ocr-confidence-score-spellcheck-regularizer-skill)
- [Pdf complex merged table bbox parser](https://github.com/Alpha-Park/genpark-pdf-complex-merged-table-bbox-parser-skill)
- [Scanned document skew orientation angle corrector](https://github.com/Alpha-Park/genpark-scanned-document-skew-orientation-angle-corrector-skill)
- [Smart contract reentrancy callgraph auditor](https://github.com/Alpha-Park/genpark-smart-contract-reentrancy-callgraph-auditor-skill)
- [Spreadsheet data sanitization normalizer](https://github.com/Alpha-Park/genpark-spreadsheet-data-sanitization-normalizer-skill)

## Security and permissions

- [Adversarial prompt jailbreak detector](https://github.com/Alpha-Park/genpark-adversarial-prompt-jailbreak-detector-skill)
- [Adversarial redteam prompt injection fuzzer](https://github.com/Alpha-Park/genpark-adversarial-redteam-prompt-injection-fuzzer-skill)
- [Agent ephemeral network egress firewall](https://github.com/Alpha-Park/genpark-agent-ephemeral-network-egress-firewall-skill)
- [Agent tool permission rbac validator](https://github.com/Alpha-Park/genpark-agent-tool-permission-rbac-validator-skill)
- [Autonomous honeypot canary sentinel](https://github.com/Alpha-Park/genpark-autonomous-honeypot-canary-sentinel-skill)
- [Canary honeytoken private key tripwire](https://github.com/Alpha-Park/genpark-canary-honeytoken-private-key-tripwire-skill)
- [Covert data exfiltration firewall](https://github.com/Alpha-Park/genpark-covert-data-exfiltration-firewall-skill)
- [Delegated agentic checkout guardrail](https://github.com/Alpha-Park/genpark-delegated-agentic-checkout-guardrail-skill)
- [Indirect prompt injection sanitizer](https://github.com/Alpha-Park/genpark-indirect-prompt-injection-sanitizer-skill)
- [Pii secret redaction masking](https://github.com/Alpha-Park/genpark-pii-secret-redaction-masking-skill)
- [Prompt injection jailbreak detector](https://github.com/Alpha-Park/genpark-prompt-injection-jailbreak-detector-skill)
- [Prompt injection jailbreak neutralizer](https://github.com/Alpha-Park/genpark-prompt-injection-jailbreak-neutralizer-skill)
- [Semgrep security ast pattern matcher](https://github.com/Alpha-Park/genpark-semgrep-security-ast-pattern-matcher-skill)

## Memory and retrieval

- [Agent context compaction deduplicator](https://github.com/Alpha-Park/genpark-agent-context-compaction-deduplicator-skill)
- [Agent context handoff state packer](https://github.com/Alpha-Park/genpark-agent-context-handoff-state-packer-skill)
- [Agent hierarchical context summarization condenser](https://github.com/Alpha-Park/genpark-agent-hierarchical-context-summarization-condenser-skill)
- [Agent long horizon context compactor](https://github.com/Alpha-Park/genpark-agent-long-horizon-context-compactor-skill)
- [Chaitin briggs graph coloring allocator](https://github.com/Alpha-Park/genpark-chaitin-briggs-graph-coloring-allocator-skill)
- [Chaitin briggs graph coloring register allocator](https://github.com/Alpha-Park/genpark-chaitin-briggs-graph-coloring-register-allocator-skill)
- [Congruence closure e graph](https://github.com/Alpha-Park/genpark-congruence-closure-e-graph-skill)
- [Contextual compression filter](https://github.com/Alpha-Park/genpark-contextual-compression-filter-skill)
- [Cross file symbol dependency graph](https://github.com/Alpha-Park/genpark-cross-file-symbol-dependency-graph-skill)
- [Deep research cross citation graph](https://github.com/Alpha-Park/genpark-deep-research-cross-citation-graph-skill)
- [Earley context free grammar parser](https://github.com/Alpha-Park/genpark-earley-context-free-grammar-parser-skill)
- [Episodic memory consolidation engine](https://github.com/Alpha-Park/genpark-episodic-memory-consolidation-engine-skill)
- [Gradient episodic memory gem projector](https://github.com/Alpha-Park/genpark-gradient-episodic-memory-gem-projector-skill)
- [Graph path random walk pagerank](https://github.com/Alpha-Park/genpark-graph-path-random-walk-pagerank-skill)
- [Graph random walk personalized pagerank](https://github.com/Alpha-Park/genpark-graph-random-walk-personalized-pagerank-skill)
- [Graph sparsification edge sampling](https://github.com/Alpha-Park/genpark-graph-sparsification-edge-sampling-skill)
- [Groth16 zero knowledge verifier pairing](https://github.com/Alpha-Park/genpark-groth16-zero-knowledge-verifier-pairing-skill)
- [Hierarchical memory consolidation compressor](https://github.com/Alpha-Park/genpark-hierarchical-memory-consolidation-compressor-skill)
- [Hierarchical navigable small world hnsw graph](https://github.com/Alpha-Park/genpark-hierarchical-navigable-small-world-hnsw-graph-skill)
- [Hyperbolic poincare embeddings](https://github.com/Alpha-Park/genpark-hyperbolic-poincare-embeddings-skill)
- [Icp firmographic matcher filter](https://github.com/Alpha-Park/genpark-icp-firmographic-matcher-filter-skill)
- [Knowledge distillation teacher student tracker](https://github.com/Alpha-Park/genpark-knowledge-distillation-teacher-student-tracker-skill)
- [Knowledge triplet subject predicate object extractor](https://github.com/Alpha-Park/genpark-knowledge-triplet-subject-predicate-object-extractor-skill)
- [Loopy belief propagation factor graph](https://github.com/Alpha-Park/genpark-loopy-belief-propagation-factor-graph-skill)
- [Lost in the middle context reordering](https://github.com/Alpha-Park/genpark-lost-in-the-middle-context-reordering-skill)
- [Max sum factor graph belief propagation](https://github.com/Alpha-Park/genpark-max-sum-factor-graph-belief-propagation-skill)
- [Memory decay forgetting curve auditor](https://github.com/Alpha-Park/genpark-memory-decay-forgetting-curve-auditor-skill)
- [Merkle tree cryptographic proof verifier](https://github.com/Alpha-Park/genpark-merkle-tree-cryptographic-proof-verifier-skill)
- [Opentelemetry span trace context propagator](https://github.com/Alpha-Park/genpark-opentelemetry-span-trace-context-propagator-skill)
- [Personal context memory graph synthesizer](https://github.com/Alpha-Park/genpark-personal-context-memory-graph-synthesizer-skill)
- [Searchable context telemetry retriever](https://github.com/Alpha-Park/genpark-searchable-context-telemetry-retriever-skill)
- [Slab buddy allocator memory pool](https://github.com/Alpha-Park/genpark-slab-buddy-allocator-memory-pool-skill)
- [Smart citation credibility scorer](https://github.com/Alpha-Park/genpark-smart-citation-credibility-scorer-skill)
- [Temporal knowledge graph edge validity](https://github.com/Alpha-Park/genpark-temporal-knowledge-graph-edge-validity-skill)
- [Temporal knowledge graph event triplet](https://github.com/Alpha-Park/genpark-temporal-knowledge-graph-event-triplet-skill)
- [Trans e knowledge graph embedding](https://github.com/Alpha-Park/genpark-trans-e-knowledge-graph-embedding-skill)
- [Vector graph hybrid reciprocal rank fusion](https://github.com/Alpha-Park/genpark-vector-graph-hybrid-reciprocal-rank-fusion-skill)
- [Virtual inmemory fs copy on write snapshotter](https://github.com/Alpha-Park/genpark-virtual-inmemory-fs-copy-on-write-snapshotter-skill)
- [Virtual inmemory module importer](https://github.com/Alpha-Park/genpark-virtual-inmemory-module-importer-skill)
- [W3c trace context span propagator](https://github.com/Alpha-Park/genpark-w3c-trace-context-span-propagator-skill)
- [Wait for graph deadlock detector](https://github.com/Alpha-Park/genpark-wait-for-graph-deadlock-detector-skill)
- [Weisfeiler lehman graph isomorphism](https://github.com/Alpha-Park/genpark-weisfeiler-lehman-graph-isomorphism-skill)
- [Zero knowledge schnorr protocol prover](https://github.com/Alpha-Park/genpark-zero-knowledge-schnorr-protocol-prover-skill)

## Vision and multimodal

- [Agent action trajectory video summarizer](https://github.com/Alpha-Park/genpark-agent-action-trajectory-video-summarizer-skill)
- [Agent belief revision contradiction pruner](https://github.com/Alpha-Park/genpark-agent-belief-revision-contradiction-pruner-skill)
- [Generative image spatial upscale tiler](https://github.com/Alpha-Park/genpark-generative-image-spatial-upscale-tiler-skill)
- [Geohash spatial dbscan clustering engine](https://github.com/Alpha-Park/genpark-geohash-spatial-dbscan-clustering-engine-skill)
- [Geohash spatial quadtree encoder](https://github.com/Alpha-Park/genpark-geohash-spatial-quadtree-encoder-skill)
- [Gui screen som coordinate mapper](https://github.com/Alpha-Park/genpark-gui-screen-som-coordinate-mapper-skill)
- [Image tagging agent](https://github.com/Alpha-Park/genpark-image-tagging-agent-skill)
- [Infinite canvas spatial clustering synthesizer](https://github.com/Alpha-Park/genpark-infinite-canvas-spatial-clustering-synthesizer-skill)
- [Multimodal aspect ratio smart reframe](https://github.com/Alpha-Park/genpark-multimodal-aspect-ratio-smart-reframe-skill)
- [Multimodal chart data point extractor](https://github.com/Alpha-Park/genpark-multimodal-chart-data-point-extractor-skill)
- [Multimodal hallucination factuality verifier](https://github.com/Alpha-Park/genpark-multimodal-hallucination-factuality-verifier-skill)
- [Multimodal visual hallucination verifier](https://github.com/Alpha-Park/genpark-multimodal-visual-hallucination-verifier-skill)
- [Nlp to geojson spatial feature compiler](https://github.com/Alpha-Park/genpark-nlp-to-geojson-spatial-feature-compiler-skill)
- [Octree 3d spatial partitioning indexer](https://github.com/Alpha-Park/genpark-octree-3d-spatial-partitioning-indexer-skill)
- [R star tree spatial indexer](https://github.com/Alpha-Park/genpark-r-star-tree-spatial-indexer-skill)
- [R tree spatial bounding box indexer](https://github.com/Alpha-Park/genpark-r-tree-spatial-bounding-box-indexer-skill)
- [R tree spatial index bounding box](https://github.com/Alpha-Park/genpark-r-tree-spatial-index-bounding-box-skill)
- [Spatial isochrone reachability analyzer](https://github.com/Alpha-Park/genpark-spatial-isochrone-reachability-analyzer-skill)
- [Spatial obstacle pointcloud voxel slicer](https://github.com/Alpha-Park/genpark-spatial-obstacle-pointcloud-voxel-slicer-skill)
- [Spatial relationship grounding evaluator](https://github.com/Alpha-Park/genpark-spatial-relationship-grounding-evaluator-skill)
- [Video keyframe camera motion path planner](https://github.com/Alpha-Park/genpark-video-keyframe-camera-motion-path-planner-skill)
- [Video silence jumpcut cadence analyzer](https://github.com/Alpha-Park/genpark-video-silence-jumpcut-cadence-analyzer-skill)
- [Vision web action bounding box grounder](https://github.com/Alpha-Park/genpark-vision-web-action-bounding-box-grounder-skill)
- [Visual grounding spec comparison](https://github.com/Alpha-Park/genpark-visual-grounding-spec-comparison-skill)
- [Visual shoppable look attribute parser](https://github.com/Alpha-Park/genpark-visual-shoppable-look-attribute-parser-skill)
- [Visual viewport element occlusion resolver](https://github.com/Alpha-Park/genpark-visual-viewport-element-occlusion-resolver-skill)
- [Welzl minimum bounding sphere solver](https://github.com/Alpha-Park/genpark-welzl-minimum-bounding-sphere-solver-skill)

## Personal productivity

- [Acyclic control flow dag scheduler](https://github.com/Alpha-Park/genpark-acyclic-control-flow-dag-scheduler-skill)
- [Acyclic instruction scheduler list scheduling](https://github.com/Alpha-Park/genpark-acyclic-instruction-scheduler-list-scheduling-skill)
- [Autonomous task dag decomposer](https://github.com/Alpha-Park/genpark-autonomous-task-dag-decomposer-skill)
- [Calendar timeblock conflict arbitrator](https://github.com/Alpha-Park/genpark-calendar-timeblock-conflict-arbitrator-skill)
- [Completely fair scheduler cfs rbtree](https://github.com/Alpha-Park/genpark-completely-fair-scheduler-cfs-rbtree-skill)
- [Distributed task idempotency deduplication](https://github.com/Alpha-Park/genpark-distributed-task-idempotency-deduplication-skill)
- [Flash attention tiling kernel](https://github.com/Alpha-Park/genpark-flash-attention-tiling-kernel-skill)
- [Hierarchical swarm task delegation governor](https://github.com/Alpha-Park/genpark-hierarchical-swarm-task-delegation-governor-skill)
- [Hierarchical task decomposition dag scheduler](https://github.com/Alpha-Park/genpark-hierarchical-task-decomposition-dag-scheduler-skill)
- [Hierarchical task network htn planner](https://github.com/Alpha-Park/genpark-hierarchical-task-network-htn-planner-skill)
- [Hyper personalized cold outreach synthesizer](https://github.com/Alpha-Park/genpark-hyper-personalized-cold-outreach-synthesizer-skill)
- [Kv cache attention sink eviction](https://github.com/Alpha-Park/genpark-kv-cache-attention-sink-eviction-skill)
- [Paged attention kv cache block allocator](https://github.com/Alpha-Park/genpark-paged-attention-kv-cache-block-allocator-skill)
- [Personal boundary auto negotiator](https://github.com/Alpha-Park/genpark-personal-boundary-auto-negotiator-skill)
- [Personal circadian energy scheduler](https://github.com/Alpha-Park/genpark-personal-circadian-energy-scheduler-skill)
- [Personal cognitive load balancer](https://github.com/Alpha-Park/genpark-personal-cognitive-load-balancer-skill)
- [Personal digital hoarding declutter agent](https://github.com/Alpha-Park/genpark-personal-digital-hoarding-declutter-agent-skill)
- [Personal habit streak anti fragility](https://github.com/Alpha-Park/genpark-personal-habit-streak-anti-fragility-skill)
- [Personal inbox cognitive triage](https://github.com/Alpha-Park/genpark-personal-inbox-cognitive-triage-skill)
- [Personal sleep recovery chronotype coach](https://github.com/Alpha-Park/genpark-personal-sleep-recovery-chronotype-coach-skill)
- [Personal spending impulse friction guard](https://github.com/Alpha-Park/genpark-personal-spending-impulse-friction-guard-skill)
- [Realtime storefront hero personalization engine](https://github.com/Alpha-Park/genpark-realtime-storefront-hero-personalization-engine-skill)
- [Split inbox triage priority scorer](https://github.com/Alpha-Park/genpark-split-inbox-triage-priority-scorer-skill)
- [Swarm task decomposition auctioneer](https://github.com/Alpha-Park/genpark-swarm-task-decomposition-auctioneer-skill)

## Commerce and marketing

- [Autonomous b2b procurement price negotiator](https://github.com/Alpha-Park/genpark-autonomous-b2b-procurement-price-negotiator-skill)
- [Autonomous price elasticity optimizer](https://github.com/Alpha-Park/genpark-autonomous-price-elasticity-optimizer-skill)
- [Avellaneda stoikov market maker](https://github.com/Alpha-Park/genpark-avellaneda-stoikov-market-maker-skill)
- [Bulletproofs inner product argument ipa](https://github.com/Alpha-Park/genpark-bulletproofs-inner-product-argument-ipa-skill)
- [Can content addressable network torus](https://github.com/Alpha-Park/genpark-can-content-addressable-network-torus-skill)
- [Competitor map price violation monitor](https://github.com/Alpha-Park/genpark-competitor-map-price-violation-monitor-skill)
- [Competitor price monitor](https://github.com/Alpha-Park/genpark-competitor-price-monitor-skill)
- [Content defined chunking cdc](https://github.com/Alpha-Park/genpark-content-defined-chunking-cdc-skill)
- [Conversational product discovery](https://github.com/Alpha-Park/genpark-conversational-product-discovery-skill)
- [Customer health credit burn tracker](https://github.com/Alpha-Park/genpark-customer-health-credit-burn-tracker-skill)
- [Evidence backed product comparison](https://github.com/Alpha-Park/genpark-evidence-backed-product-comparison-skill)
- [Influencer campaign brief builder](https://github.com/Alpha-Park/genpark-influencer-campaign-brief-builder-skill)
- [Influencer content performance analyzer](https://github.com/Alpha-Park/genpark-influencer-content-performance-analyzer-skill)
- [Influencer creator fit scoring](https://github.com/Alpha-Park/genpark-influencer-creator-fit-scoring-skill)
- [Marketing banner agent](https://github.com/Alpha-Park/genpark-marketing-banner-agent-skill)
- [Marketplace sku taxonomy transformer](https://github.com/Alpha-Park/genpark-marketplace-sku-taxonomy-transformer-skill)
- [Product comparison agent](https://github.com/Alpha-Park/genpark-product-comparison-agent-skill)
- [Product geoip currency tax nexus normalizer](https://github.com/Alpha-Park/genpark-product-geoip-currency-tax-nexus-normalizer-skill)
- [Product review sentiment analyzer](https://github.com/Alpha-Park/genpark-product-review-sentiment-analyzer-skill)
- [Product spec extractor](https://github.com/Alpha-Park/genpark-product-spec-extractor-skill)
- [Seo metadata agent](https://github.com/Alpha-Park/genpark-seo-metadata-agent-skill)
- [Vector svg brand geometry normalizer](https://github.com/Alpha-Park/genpark-vector-svg-brand-geometry-normalizer-skill)
- [Volume weighted average price vwap](https://github.com/Alpha-Park/genpark-volume-weighted-average-price-vwap-skill)

## Agent workflows and reliability

- [Abstract interpretation interval domain](https://github.com/Alpha-Park/genpark-abstract-interpretation-interval-domain-skill)
- [Actor critic entropy exploration](https://github.com/Alpha-Park/genpark-actor-critic-entropy-exploration-skill)
- [Actor mailbox beam supervisor](https://github.com/Alpha-Park/genpark-actor-mailbox-beam-supervisor-skill)
- [Actuator thermal torque throttle sentinel](https://github.com/Alpha-Park/genpark-actuator-thermal-torque-throttle-sentinel-skill)
- [Adamw decoupled weight decay](https://github.com/Alpha-Park/genpark-adamw-decoupled-weight-decay-skill)
- [Adaptive token rate limiter](https://github.com/Alpha-Park/genpark-adaptive-token-rate-limiter-skill)
- [Agent breakpoint checkpoint approval patcher](https://github.com/Alpha-Park/genpark-agent-breakpoint-checkpoint-approval-patcher-skill)
- [Agent budget rate limit throttle](https://github.com/Alpha-Park/genpark-agent-budget-rate-limit-throttle-skill)
- [Agent dag parallel branch fanout join](https://github.com/Alpha-Park/genpark-agent-dag-parallel-branch-fanout-join-skill)
- [Agent epistemic aleatoric uncertainty decomposer](https://github.com/Alpha-Park/genpark-agent-epistemic-aleatoric-uncertainty-decomposer-skill)
- [Agent execution checkpoint time travel](https://github.com/Alpha-Park/genpark-agent-execution-checkpoint-time-travel-skill)
- [Agent hierarchical delegation supervisor](https://github.com/Alpha-Park/genpark-agent-hierarchical-delegation-supervisor-skill)
- [Agent multi turn eval scorer](https://github.com/Alpha-Park/genpark-agent-multi-turn-eval-scorer-skill)
- [Agent opentelemetry span trace profiler](https://github.com/Alpha-Park/genpark-agent-opentelemetry-span-trace-profiler-skill)
- [Agent reputation credit ledger](https://github.com/Alpha-Park/genpark-agent-reputation-credit-ledger-skill)
- [Agent runtime hotpatch sandbox injector](https://github.com/Alpha-Park/genpark-agent-runtime-hotpatch-sandbox-injector-skill)
- [Agent runtime invariant assertion synthesizer](https://github.com/Alpha-Park/genpark-agent-runtime-invariant-assertion-synthesizer-skill)
- [Agent sandboxed file diff safety auditor](https://github.com/Alpha-Park/genpark-agent-sandboxed-file-diff-safety-auditor-skill)
- [Agent session compaction tokenizer](https://github.com/Alpha-Park/genpark-agent-session-compaction-tokenizer-skill)
- [Agent skill vector registry discovery](https://github.com/Alpha-Park/genpark-agent-skill-vector-registry-discovery-skill)
- [Agent speculative decoding orchestrator](https://github.com/Alpha-Park/genpark-agent-speculative-decoding-orchestrator-skill)
- [Agent step latency percentile tracker](https://github.com/Alpha-Park/genpark-agent-step-latency-percentile-tracker-skill)
- [Agent synthetic persona consensus engine](https://github.com/Alpha-Park/genpark-agent-synthetic-persona-consensus-engine-skill)
- [Agent to agent capability handshake negotiator](https://github.com/Alpha-Park/genpark-agent-to-agent-capability-handshake-negotiator-skill)
- [Agent tool call circuit breaker](https://github.com/Alpha-Park/genpark-agent-tool-call-circuit-breaker-skill)
- [Agent tool call self healing retry guard](https://github.com/Alpha-Park/genpark-agent-tool-call-self-healing-retry-guard-skill)
- [Agent toxicity sentiment drift monitor](https://github.com/Alpha-Park/genpark-agent-toxicity-sentiment-drift-monitor-skill)
- [Agent user coreference entity resolver](https://github.com/Alpha-Park/genpark-agent-user-coreference-entity-resolver-skill)
- [Agent verbal reinforcement reflexion loop](https://github.com/Alpha-Park/genpark-agent-verbal-reinforcement-reflexion-loop-skill)
- [Agentic bnpl installment credit optimizer](https://github.com/Alpha-Park/genpark-agentic-bnpl-installment-credit-optimizer-skill)
- [Agentic browser bot defense detector](https://github.com/Alpha-Park/genpark-agentic-browser-bot-defense-detector-skill)
- [Agentic cache semantic deduplicator](https://github.com/Alpha-Park/genpark-agentic-cache-semantic-deduplicator-skill)
- [Agentic hallucination cross examination debate](https://github.com/Alpha-Park/genpark-agentic-hallucination-cross-examination-debate-skill)
- [Agentic hallucination grounding checker](https://github.com/Alpha-Park/genpark-agentic-hallucination-grounding-checker-skill)
- [Agentic lead score velocity evaluator](https://github.com/Alpha-Park/genpark-agentic-lead-score-velocity-evaluator-skill)
- [Agentic workflow state checkpoint](https://github.com/Alpha-Park/genpark-agentic-workflow-state-checkpoint-skill)
- [Aho corasick multi pattern automaton](https://github.com/Alpha-Park/genpark-aho-corasick-multi-pattern-automaton-skill)
- [Annoy random projection forest](https://github.com/Alpha-Park/genpark-annoy-random-projection-forest-skill)
- [Anti bot fingerprint entropy neutralizer](https://github.com/Alpha-Park/genpark-anti-bot-fingerprint-entropy-neutralizer-skill)
- [Anti entropy merkle sync](https://github.com/Alpha-Park/genpark-anti-entropy-merkle-sync-skill)
- [Apache avro schema evolution resolver](https://github.com/Alpha-Park/genpark-apache-avro-schema-evolution-resolver-skill)
- [Aries wal crash recovery engine](https://github.com/Alpha-Park/genpark-aries-wal-crash-recovery-engine-skill)
- [Arithmetic coding entropy compression](https://github.com/Alpha-Park/genpark-arithmetic-coding-entropy-compression-skill)
- [Ast diff semantic pr reviewer](https://github.com/Alpha-Park/genpark-ast-diff-semantic-pr-reviewer-skill)
- [Ast taint source sink flow tracer](https://github.com/Alpha-Park/genpark-ast-taint-source-sink-flow-tracer-skill)
- [Ast unsafe call import blocker](https://github.com/Alpha-Park/genpark-ast-unsafe-call-import-blocker-skill)
- [Async unhandled promise rejection triager](https://github.com/Alpha-Park/genpark-async-unhandled-promise-rejection-triager-skill)
- [Asynchronous barrier snapshotting abs](https://github.com/Alpha-Park/genpark-asynchronous-barrier-snapshotting-abs-skill)
- [Asynchronous weak commitment search awcs](https://github.com/Alpha-Park/genpark-asynchronous-weak-commitment-search-awcs-skill)
- [Attribute normalizer](https://github.com/Alpha-Park/genpark-attribute-normalizer-skill)
- [Automated compliance policy evaluator](https://github.com/Alpha-Park/genpark-automated-compliance-policy-evaluator-skill)
- [Automated llm judge feedback evaluator](https://github.com/Alpha-Park/genpark-automated-llm-judge-feedback-evaluator-skill)
- [Automated program repair ast patcher](https://github.com/Alpha-Park/genpark-automated-program-repair-ast-patcher-skill)
- [Autonomous browser action planner](https://github.com/Alpha-Park/genpark-autonomous-browser-action-planner-skill)
- [Autonomous code skill synthesis evaluator](https://github.com/Alpha-Park/genpark-autonomous-code-skill-synthesis-evaluator-skill)
- [Autonomous form autofill resolver](https://github.com/Alpha-Park/genpark-autonomous-form-autofill-resolver-skill)
- [Autonomous openapi tool generator](https://github.com/Alpha-Park/genpark-autonomous-openapi-tool-generator-skill)
- [Autonomous refund dispute arbitrator](https://github.com/Alpha-Park/genpark-autonomous-refund-dispute-arbitrator-skill)
- [Autonomous test mutation coverage scorer](https://github.com/Alpha-Park/genpark-autonomous-test-mutation-coverage-scorer-skill)
- [B link tree concurrent indexing](https://github.com/Alpha-Park/genpark-b-link-tree-concurrent-indexing-skill)
- [Backdoor criterion confounder adjustment](https://github.com/Alpha-Park/genpark-backdoor-criterion-confounder-adjustment-skill)
- [Backtracking beam search reasoning explorer](https://github.com/Alpha-Park/genpark-backtracking-beam-search-reasoning-explorer-skill)
- [Bakery algorithm distributed mutex](https://github.com/Alpha-Park/genpark-bakery-algorithm-distributed-mutex-skill)
- [Bayesian network exact variable elimination](https://github.com/Alpha-Park/genpark-bayesian-network-exact-variable-elimination-skill)
- [Bb84 quantum key distribution simulator](https://github.com/Alpha-Park/genpark-bb84-quantum-key-distribution-simulator-skill)
- [Bbr congestion control pacer](https://github.com/Alpha-Park/genpark-bbr-congestion-control-pacer-skill)
- [Beam search autoregressive decoder](https://github.com/Alpha-Park/genpark-beam-search-autoregressive-decoder-skill)
- [Bgp4 path vector routing engine](https://github.com/Alpha-Park/genpark-bgp4-path-vector-routing-engine-skill)
- [Bidirectional human agent state sync coordinator](https://github.com/Alpha-Park/genpark-bidirectional-human-agent-state-sync-coordinator-skill)
- [Billing spend anomaly guard](https://github.com/Alpha-Park/genpark-billing-spend-anomaly-guard-skill)
- [Bimatrix nash equilibrium solver](https://github.com/Alpha-Park/genpark-bimatrix-nash-equilibrium-solver-skill)
- [Biquad iir filter cascade](https://github.com/Alpha-Park/genpark-biquad-iir-filter-cascade-skill)
- [Blind signature rsa chaum](https://github.com/Alpha-Park/genpark-blind-signature-rsa-chaum-skill)
- [Bm25 okapi lexical ranking engine](https://github.com/Alpha-Park/genpark-bm25-okapi-lexical-ranking-engine-skill)
- [Bm25 sparse lexical inverted indexer](https://github.com/Alpha-Park/genpark-bm25-sparse-lexical-inverted-indexer-skill)
- [Borda count condorcet social choice voting](https://github.com/Alpha-Park/genpark-borda-count-condorcet-social-choice-voting-skill)
- [Bpe byte pair encoding tokenizer](https://github.com/Alpha-Park/genpark-bpe-byte-pair-encoding-tokenizer-skill)
- [Bradley terry elo rating tournament](https://github.com/Alpha-Park/genpark-bradley-terry-elo-rating-tournament-skill)
- [Branch and bound integer programming](https://github.com/Alpha-Park/genpark-branch-and-bound-integer-programming-skill)
- [Bron kerbosch clique enumeration](https://github.com/Alpha-Park/genpark-bron-kerbosch-clique-enumeration-skill)
- [Browser computer use element anchor](https://github.com/Alpha-Park/genpark-browser-computer-use-element-anchor-skill)
- [Browser dom accessibility tree pruner](https://github.com/Alpha-Park/genpark-browser-dom-accessibility-tree-pruner-skill)
- [Bsp tree binary space partitioning](https://github.com/Alpha-Park/genpark-bsp-tree-binary-space-partitioning-skill)
- [Btree concurrent latch crabbing storage](https://github.com/Alpha-Park/genpark-btree-concurrent-latch-crabbing-storage-skill)
- [Bully election distributed leader](https://github.com/Alpha-Park/genpark-bully-election-distributed-leader-skill)
- [Burrows wheeler bwt fm index aligner](https://github.com/Alpha-Park/genpark-burrows-wheeler-bwt-fm-index-aligner-skill)
- [Burrows wheeler bwt fm index](https://github.com/Alpha-Park/genpark-burrows-wheeler-bwt-fm-index-skill)
- [Butterworth iir digital filter designer](https://github.com/Alpha-Park/genpark-butterworth-iir-digital-filter-designer-skill)
- [Byte pair encoding bpe tokenizer](https://github.com/Alpha-Park/genpark-byte-pair-encoding-bpe-tokenizer-skill)
- [Bytecode disassembler instruction auditor](https://github.com/Alpha-Park/genpark-bytecode-disassembler-instruction-auditor-skill)
- [Byzantine fault tolerant quorum validator](https://github.com/Alpha-Park/genpark-byzantine-fault-tolerant-quorum-validator-skill)
- [Byzantine fault tolerant quorum voting](https://github.com/Alpha-Park/genpark-byzantine-fault-tolerant-quorum-voting-skill)
- [Canonical doi bibtex crossref resolver](https://github.com/Alpha-Park/genpark-canonical-doi-bibtex-crossref-resolver-skill)
- [Capnproto word aligned message arena](https://github.com/Alpha-Park/genpark-capnproto-word-aligned-message-arena-skill)
- [Cascading router cost quality optimizer](https://github.com/Alpha-Park/genpark-cascading-router-cost-quality-optimizer-skill)
- [Cbor concise binary object representation](https://github.com/Alpha-Park/genpark-cbor-concise-binary-object-representation-skill)
- [Cdcl sat two watched literals](https://github.com/Alpha-Park/genpark-cdcl-sat-two-watched-literals-skill)
- [Chain of verification cove](https://github.com/Alpha-Park/genpark-chain-of-verification-cove-skill)
- [Chandy lamport distributed snapshot](https://github.com/Alpha-Park/genpark-chandy-lamport-distributed-snapshot-skill)
- [Chandy misra haas distributed deadlock](https://github.com/Alpha-Park/genpark-chandy-misra-haas-distributed-deadlock-skill)
- [Chase lev work stealing deque](https://github.com/Alpha-Park/genpark-chase-lev-work-stealing-deque-skill)
- [Cholesky decomposition spd solver](https://github.com/Alpha-Park/genpark-cholesky-decomposition-spd-solver-skill)
- [Chow liu tree bayesian structure learner](https://github.com/Alpha-Park/genpark-chow-liu-tree-bayesian-structure-learner-skill)
- [Cky probabilistic grammar parser](https://github.com/Alpha-Park/genpark-cky-probabilistic-grammar-parser-skill)
- [Claude code conversation archiver](https://github.com/Alpha-Park/genpark-claude-code-conversation-archiver-skill)
- [Clawverse autonomous pixel island simulator](https://github.com/Alpha-Park/genpark-clawverse-autonomous-pixel-island-simulator-skill)
- [Client side hydration runtime error triage](https://github.com/Alpha-Park/genpark-client-side-hydration-runtime-error-triage-skill)
- [Cocke younger kasami cyk pcfg parser](https://github.com/Alpha-Park/genpark-cocke-younger-kasami-cyk-pcfg-parser-skill)
- [Code execution timeout watchdog timer](https://github.com/Alpha-Park/genpark-code-execution-timeout-watchdog-timer-skill)
- [Codebase invariant assertion sentinel](https://github.com/Alpha-Park/genpark-codebase-invariant-assertion-sentinel-skill)
- [Columnar storage vectorized execution](https://github.com/Alpha-Park/genpark-columnar-storage-vectorized-execution-skill)
- [Commercial catchment area profiler](https://github.com/Alpha-Park/genpark-commercial-catchment-area-profiler-skill)
- [Concolic symbolic execution branch inverter](https://github.com/Alpha-Park/genpark-concolic-symbolic-execution-branch-inverter-skill)
- [Conformal prediction coverage guarantee](https://github.com/Alpha-Park/genpark-conformal-prediction-coverage-guarantee-skill)
- [Conjugate gradient krylov subspace solver](https://github.com/Alpha-Park/genpark-conjugate-gradient-krylov-subspace-solver-skill)
- [Consensus admm distributed trajectory](https://github.com/Alpha-Park/genpark-consensus-admm-distributed-trajectory-skill)
- [Consistent hash ring vnodes](https://github.com/Alpha-Park/genpark-consistent-hash-ring-vnodes-skill)
- [Consistent hashing virtual nodes ring](https://github.com/Alpha-Park/genpark-consistent-hashing-virtual-nodes-ring-skill)
- [Consistent hashing virtual nodes](https://github.com/Alpha-Park/genpark-consistent-hashing-virtual-nodes-skill)
- [Constraint satisfaction ac3 backtracking](https://github.com/Alpha-Park/genpark-constraint-satisfaction-ac3-backtracking-skill)
- [Continual fewshot exemplar distiller](https://github.com/Alpha-Park/genpark-continual-fewshot-exemplar-distiller-skill)
- [Contradiction detection belief updater](https://github.com/Alpha-Park/genpark-contradiction-detection-belief-updater-skill)
- [Conversation turn pruner information entropy](https://github.com/Alpha-Park/genpark-conversation-turn-pruner-information-entropy-skill)
- [Conversational sizing fit recommender](https://github.com/Alpha-Park/genpark-conversational-sizing-fit-recommender-skill)
- [Conversational sms abandoned browse recovery](https://github.com/Alpha-Park/genpark-conversational-sms-abandoned-browse-recovery-skill)
- [Cookie consent modal stealth dismissal](https://github.com/Alpha-Park/genpark-cookie-consent-modal-stealth-dismissal-skill)
- [Cooley tukey fast fourier transform fft](https://github.com/Alpha-Park/genpark-cooley-tukey-fast-fourier-transform-fft-skill)
- [Cooley tukey fft radix2](https://github.com/Alpha-Park/genpark-cooley-tukey-fft-radix2-skill)
- [Cooley tukey radix2 fft engine](https://github.com/Alpha-Park/genpark-cooley-tukey-radix2-fft-engine-skill)
- [Count min sketch frequency estimator](https://github.com/Alpha-Park/genpark-count-min-sketch-frequency-estimator-skill)
- [Counterfactual execution test generator](https://github.com/Alpha-Park/genpark-counterfactual-execution-test-generator-skill)
- [Counterfactual three step abduction prediction](https://github.com/Alpha-Park/genpark-counterfactual-three-step-abduction-prediction-skill)
- [Coupon recommendation](https://github.com/Alpha-Park/genpark-coupon-recommendation-skill)
- [Cpg island viterbi hmm detector](https://github.com/Alpha-Park/genpark-cpg-island-viterbi-hmm-detector-skill)
- [Crdt pn counter lww register](https://github.com/Alpha-Park/genpark-crdt-pn-counter-lww-register-skill)
- [Critique rubric multi criteria evaluator](https://github.com/Alpha-Park/genpark-critique-rubric-multi-criteria-evaluator-skill)
- [Crm bidirectional dedup sync resolver](https://github.com/Alpha-Park/genpark-crm-bidirectional-dedup-sync-resolver-skill)
- [Cross agent blackboard shared state sync](https://github.com/Alpha-Park/genpark-cross-agent-blackboard-shared-state-sync-skill)
- [Cross border duty customs tariff estimator](https://github.com/Alpha-Park/genpark-cross-border-duty-customs-tariff-estimator-skill)
- [Cross chain bridge invariant anomaly detector](https://github.com/Alpha-Park/genpark-cross-chain-bridge-invariant-anomaly-detector-skill)
- [Cross codebase api migration impact mapper](https://github.com/Alpha-Park/genpark-cross-codebase-api-migration-impact-mapper-skill)
- [Cross window persistent notes ledger](https://github.com/Alpha-Park/genpark-cross-window-persistent-notes-ledger-skill)
- [Css layout shift cls optimizer](https://github.com/Alpha-Park/genpark-css-layout-shift-cls-optimizer-skill)
- [Dapper distributed trace sampler](https://github.com/Alpha-Park/genpark-dapper-distributed-trace-sampler-skill)
- [Daubechies d4 wavelet transform](https://github.com/Alpha-Park/genpark-daubechies-d4-wavelet-transform-skill)
- [Dct type2 jpeg compression engine](https://github.com/Alpha-Park/genpark-dct-type2-jpeg-compression-engine-skill)
- [Dead code unreachable ast pruner](https://github.com/Alpha-Park/genpark-dead-code-unreachable-ast-pruner-skill)
- [Deep research consensus engine](https://github.com/Alpha-Park/genpark-deep-research-consensus-engine-skill)
- [Delaunay triangulation bowyer watson](https://github.com/Alpha-Park/genpark-delaunay-triangulation-bowyer-watson-skill)
- [Design token tailwind component palette builder](https://github.com/Alpha-Park/genpark-design-token-tailwind-component-palette-builder-skill)
- [Deutsch jozsa quantum oracle prover](https://github.com/Alpha-Park/genpark-deutsch-jozsa-quantum-oracle-prover-skill)
- [Dgim sliding window bit counter](https://github.com/Alpha-Park/genpark-dgim-sliding-window-bit-counter-skill)
- [Diffie hellman ratchet forward secrecy](https://github.com/Alpha-Park/genpark-diffie-hellman-ratchet-forward-secrecy-skill)
- [Diffie hellman ratchet signal](https://github.com/Alpha-Park/genpark-diffie-hellman-ratchet-signal-skill)
- [Dijkstra weakest precondition wp calculus](https://github.com/Alpha-Park/genpark-dijkstra-weakest-precondition-wp-calculus-skill)
- [Dinic maximum network flow](https://github.com/Alpha-Park/genpark-dinic-maximum-network-flow-skill)
- [Discrete wavelet transform haar daubechies](https://github.com/Alpha-Park/genpark-discrete-wavelet-transform-haar-daubechies-skill)
- [Distributed breakout algorithm dcop](https://github.com/Alpha-Park/genpark-distributed-breakout-algorithm-dcop-skill)
- [Dom semantic accessibility tree pruner](https://github.com/Alpha-Park/genpark-dom-semantic-accessibility-tree-pruner-skill)
- [Dominator tree ssa phi node placement](https://github.com/Alpha-Park/genpark-dominator-tree-ssa-phi-node-placement-skill)
- [Douglas peucker polyline simplification](https://github.com/Alpha-Park/genpark-douglas-peucker-polyline-simplification-skill)
- [Dpdk zero copy packet ring buffer](https://github.com/Alpha-Park/genpark-dpdk-zero-copy-packet-ring-buffer-skill)
- [Dpll sat solver boolean satisfiability](https://github.com/Alpha-Park/genpark-dpll-sat-solver-boolean-satisfiability-skill)
- [Dpll sat solver](https://github.com/Alpha-Park/genpark-dpll-sat-solver-skill)
- [Dpll sat solver unit propagation](https://github.com/Alpha-Park/genpark-dpll-sat-solver-unit-propagation-skill)
- [Dqn prioritized experience replay](https://github.com/Alpha-Park/genpark-dqn-prioritized-experience-replay-skill)
- [Dynamic ast transformer instrumentation](https://github.com/Alpha-Park/genpark-dynamic-ast-transformer-instrumentation-skill)
- [Dynamic bundle pricing maximizer](https://github.com/Alpha-Park/genpark-dynamic-bundle-pricing-maximizer-skill)
- [Dynamic jsonld rich snippet generator](https://github.com/Alpha-Park/genpark-dynamic-jsonld-rich-snippet-generator-skill)
- [Dynamic mixture of agents moa layer](https://github.com/Alpha-Park/genpark-dynamic-mixture-of-agents-moa-layer-skill)
- [Dynamic mock generator behavioral fuzzer](https://github.com/Alpha-Park/genpark-dynamic-mock-generator-behavioral-fuzzer-skill)
- [Dynamic pddl domain problem parser](https://github.com/Alpha-Park/genpark-dynamic-pddl-domain-problem-parser-skill)
- [Dynamic range compressor limiter](https://github.com/Alpha-Park/genpark-dynamic-range-compressor-limiter-skill)
- [Dynamic sparkpage layout synthesizer](https://github.com/Alpha-Park/genpark-dynamic-sparkpage-layout-synthesizer-skill)
- [Dynamic time warping dtw alignment](https://github.com/Alpha-Park/genpark-dynamic-time-warping-dtw-alignment-skill)
- [Dynamic tool dependency dag topological resolver](https://github.com/Alpha-Park/genpark-dynamic-tool-dependency-dag-topological-resolver-skill)
- [Dynamic tool parameter dependency resolver](https://github.com/Alpha-Park/genpark-dynamic-tool-parameter-dependency-resolver-skill)
- [Dynamo sloppy quorum hinted handoff](https://github.com/Alpha-Park/genpark-dynamo-sloppy-quorum-hinted-handoff-skill)
- [Ear clipping polygon triangulation](https://github.com/Alpha-Park/genpark-ear-clipping-polygon-triangulation-skill)
- [Ecvrf verifiable random function](https://github.com/Alpha-Park/genpark-ecvrf-verifiable-random-function-skill)
- [Edge case unit test coverage synthesizer](https://github.com/Alpha-Park/genpark-edge-case-unit-test-coverage-synthesizer-skill)
- [Edmonds blossom general matching](https://github.com/Alpha-Park/genpark-edmonds-blossom-general-matching-skill)
- [Eip712 typed signature phishing sanitizer](https://github.com/Alpha-Park/genpark-eip712-typed-signature-phishing-sanitizer-skill)
- [Elastic weight consolidation fisher reg](https://github.com/Alpha-Park/genpark-elastic-weight-consolidation-fisher-reg-skill)
- [Entity disambiguation clustering resolver](https://github.com/Alpha-Park/genpark-entity-disambiguation-clustering-resolver-skill)
- [Entity disambiguation ned](https://github.com/Alpha-Park/genpark-entity-disambiguation-ned-skill)
- [Erasure coding reed solomon](https://github.com/Alpha-Park/genpark-erasure-coding-reed-solomon-skill)
- [Evm flashloan arbitrage slippage guard](https://github.com/Alpha-Park/genpark-evm-flashloan-arbitrage-slippage-guard-skill)
- [Executive bi metric narrative synthesizer](https://github.com/Alpha-Park/genpark-executive-bi-metric-narrative-synthesizer-skill)
- [Experience replay reservoir sampling](https://github.com/Alpha-Park/genpark-experience-replay-reservoir-sampling-skill)
- [Faq semantic matcher](https://github.com/Alpha-Park/genpark-faq-semantic-matcher-skill)
- [Fictitious play iterative learning equilibrium](https://github.com/Alpha-Park/genpark-fictitious-play-iterative-learning-equilibrium-skill)
- [First order logic resolution prover](https://github.com/Alpha-Park/genpark-first-order-logic-resolution-prover-skill)
- [First order resolution refutation](https://github.com/Alpha-Park/genpark-first-order-resolution-refutation-skill)
- [Fix protocol parser engine](https://github.com/Alpha-Park/genpark-fix-protocol-parser-engine-skill)
- [Flajolet martin cardinality sketch](https://github.com/Alpha-Park/genpark-flajolet-martin-cardinality-sketch-skill)
- [Flaky test timing non determinism detector](https://github.com/Alpha-Park/genpark-flaky-test-timing-non-determinism-detector-skill)
- [Flat combining concurrent priority queue](https://github.com/Alpha-Park/genpark-flat-combining-concurrent-priority-queue-skill)
- [Form autofill multi step dependency filler](https://github.com/Alpha-Park/genpark-form-autofill-multi-step-dependency-filler-skill)
- [Fortune sweep line voronoi diagram](https://github.com/Alpha-Park/genpark-fortune-sweep-line-voronoi-diagram-skill)
- [Forward backward hmm smoother](https://github.com/Alpha-Park/genpark-forward-backward-hmm-smoother-skill)
- [Forward chaining rete inference engine](https://github.com/Alpha-Park/genpark-forward-chaining-rete-inference-engine-skill)
- [Fri low degree proximity](https://github.com/Alpha-Park/genpark-fri-low-degree-proximity-skill)
- [Fullstack env variable drift resolver](https://github.com/Alpha-Park/genpark-fullstack-env-variable-drift-resolver-skill)
- [Function call parameter type sanitizer](https://github.com/Alpha-Park/genpark-function-call-parameter-type-sanitizer-skill)
- [Gale shapley deferred acceptance matching](https://github.com/Alpha-Park/genpark-gale-shapley-deferred-acceptance-matching-skill)
- [Gguf tensor metadata header validator](https://github.com/Alpha-Park/genpark-gguf-tensor-metadata-header-validator-skill)
- [Git unified diff patch synthesizer](https://github.com/Alpha-Park/genpark-git-unified-diff-patch-synthesizer-skill)
- [Go work stealing m n runtime](https://github.com/Alpha-Park/genpark-go-work-stealing-m-n-runtime-skill)
- [Gpu warp divergence simulator](https://github.com/Alpha-Park/genpark-gpu-warp-divergence-simulator-skill)
- [Graham scan convex hull 2d](https://github.com/Alpha-Park/genpark-graham-scan-convex-hull-2d-skill)
- [Gram schmidt qr factorization](https://github.com/Alpha-Park/genpark-gram-schmidt-qr-factorization-skill)
- [Grover quantum search optimizer](https://github.com/Alpha-Park/genpark-grover-quantum-search-optimizer-skill)
- [Half edge mesh doubly connected](https://github.com/Alpha-Park/genpark-half-edge-mesh-doubly-connected-skill)
- [Hallucination fact grounding checker](https://github.com/Alpha-Park/genpark-hallucination-fact-grounding-checker-skill)
- [Hamming 7 4 syndrome decoder](https://github.com/Alpha-Park/genpark-hamming-7-4-syndrome-decoder-skill)
- [Harris lockfree linked list](https://github.com/Alpha-Park/genpark-harris-lockfree-linked-list-skill)
- [Haversine spherical geodesic distance](https://github.com/Alpha-Park/genpark-haversine-spherical-geodesic-distance-skill)
- [Haversine vincenty geodesic engine](https://github.com/Alpha-Park/genpark-haversine-vincenty-geodesic-engine-skill)
- [Hdr histogram percentile estimator](https://github.com/Alpha-Park/genpark-hdr-histogram-percentile-estimator-skill)
- [Headless delegated payment token vault](https://github.com/Alpha-Park/genpark-headless-delegated-payment-token-vault-skill)
- [Hidden markov model viterbi decoder](https://github.com/Alpha-Park/genpark-hidden-markov-model-viterbi-decoder-skill)
- [Hierarchical community leiden detector](https://github.com/Alpha-Park/genpark-hierarchical-community-leiden-detector-skill)
- [Hierarchical markdown chunker heading anchor](https://github.com/Alpha-Park/genpark-hierarchical-markdown-chunker-heading-anchor-skill)
- [Hilbert transform analytic signal](https://github.com/Alpha-Park/genpark-hilbert-transform-analytic-signal-skill)
- [Hindley milner algorithm w type inferencer](https://github.com/Alpha-Park/genpark-hindley-milner-algorithm-w-type-inferencer-skill)
- [Hindley milner type inference](https://github.com/Alpha-Park/genpark-hindley-milner-type-inference-skill)
- [Hnsw hierarchical navigable small world](https://github.com/Alpha-Park/genpark-hnsw-hierarchical-navigable-small-world-skill)
- [Hoare logic triplet verifier](https://github.com/Alpha-Park/genpark-hoare-logic-triplet-verifier-skill)
- [Hoare logic wp calculus](https://github.com/Alpha-Park/genpark-hoare-logic-wp-calculus-skill)
- [Hopcroft karp bipartite matching](https://github.com/Alpha-Park/genpark-hopcroft-karp-bipartite-matching-skill)
- [Hotstuff chained pipelined bft](https://github.com/Alpha-Park/genpark-hotstuff-chained-pipelined-bft-skill)
- [Huffman canonical prefix coding](https://github.com/Alpha-Park/genpark-huffman-canonical-prefix-coding-skill)
- [Human in the loop approval gate interrupt](https://github.com/Alpha-Park/genpark-human-in-the-loop-approval-gate-interrupt-skill)
- [Hungarian munkres assignment algorithm](https://github.com/Alpha-Park/genpark-hungarian-munkres-assignment-algorithm-skill)
- [Hybrid logical clock hlc causality](https://github.com/Alpha-Park/genpark-hybrid-logical-clock-hlc-causality-skill)
- [Hybrid rerank fusion retriever](https://github.com/Alpha-Park/genpark-hybrid-rerank-fusion-retriever-skill)
- [Hyperloglog cardinality estimator](https://github.com/Alpha-Park/genpark-hyperloglog-cardinality-estimator-skill)
- [Immersed boundary method ibm](https://github.com/Alpha-Park/genpark-immersed-boundary-method-ibm-skill)
- [Immix mark region garbage collector](https://github.com/Alpha-Park/genpark-immix-mark-region-garbage-collector-skill)
- [Inprocess python repl isolated namespace](https://github.com/Alpha-Park/genpark-inprocess-python-repl-isolated-namespace-skill)
- [Instruction selection max munch](https://github.com/Alpha-Park/genpark-instruction-selection-max-munch-skill)
- [Instrumental variable two stage estimator](https://github.com/Alpha-Park/genpark-instrumental-variable-two-stage-estimator-skill)
- [Intent signal buying propensity scorer](https://github.com/Alpha-Park/genpark-intent-signal-buying-propensity-scorer-skill)
- [Inter agent handshake negotiator](https://github.com/Alpha-Park/genpark-inter-agent-handshake-negotiator-skill)
- [Inventory low notifier](https://github.com/Alpha-Park/genpark-inventory-low-notifier-skill)
- [Inverse kinematics joint limit solver](https://github.com/Alpha-Park/genpark-inverse-kinematics-joint-limit-solver-skill)
- [Inverted file index ivf voronoi clusterer](https://github.com/Alpha-Park/genpark-inverted-file-index-ivf-voronoi-clusterer-skill)
- [Ising model gibbs sampler mrf](https://github.com/Alpha-Park/genpark-ising-model-gibbs-sampler-mrf-skill)
- [Iterative delta debugging minimizer](https://github.com/Alpha-Park/genpark-iterative-delta-debugging-minimizer-skill)
- [Iterative self rewarding prompt synthesizer](https://github.com/Alpha-Park/genpark-iterative-self-rewarding-prompt-synthesizer-skill)
- [Ivf flat vector quantization indexer](https://github.com/Alpha-Park/genpark-ivf-flat-vector-quantization-indexer-skill)
- [Izhikevich spiking neuron bursting](https://github.com/Alpha-Park/genpark-izhikevich-spiking-neuron-bursting-skill)
- [Jemalloc slab arena allocator](https://github.com/Alpha-Park/genpark-jemalloc-slab-arena-allocator-skill)
- [Json schema regex grammar constrainer](https://github.com/Alpha-Park/genpark-json-schema-regex-grammar-constrainer-skill)
- [Kahneman tversky kto utility loss](https://github.com/Alpha-Park/genpark-kahneman-tversky-kto-utility-loss-skill)
- [Kalman filter 1d state estimator](https://github.com/Alpha-Park/genpark-kalman-filter-1d-state-estimator-skill)
- [Karger randomized min cut](https://github.com/Alpha-Park/genpark-karger-randomized-min-cut-skill)
- [Key group consistent state partitioner](https://github.com/Alpha-Park/genpark-key-group-consistent-state-partitioner-skill)
- [Knaster tarski least fixpoint solver](https://github.com/Alpha-Park/genpark-knaster-tarski-least-fixpoint-solver-skill)
- [Kolmogorov complexity normalized compression distance](https://github.com/Alpha-Park/genpark-kolmogorov-complexity-normalized-compression-distance-skill)
- [Kzg10 polynomial commitment](https://github.com/Alpha-Park/genpark-kzg10-polynomial-commitment-skill)
- [L2 gradient clipping norm](https://github.com/Alpha-Park/genpark-l2-gradient-clipping-norm-skill)
- [L3 limit order book matcher](https://github.com/Alpha-Park/genpark-l3-limit-order-book-matcher-skill)
- [Lamport vector clock causality tracker](https://github.com/Alpha-Park/genpark-lamport-vector-clock-causality-tracker-skill)
- [Lattice boltzmann d2q9 fluid](https://github.com/Alpha-Park/genpark-lattice-boltzmann-d2q9-fluid-skill)
- [Ldpc belief propagation decoder](https://github.com/Alpha-Park/genpark-ldpc-belief-propagation-decoder-skill)
- [Leaky integrate and fire lif neuron](https://github.com/Alpha-Park/genpark-leaky-integrate-and-fire-lif-neuron-skill)
- [Least commitment partial order planner](https://github.com/Alpha-Park/genpark-least-commitment-partial-order-planner-skill)
- [Least to most subgoal planner](https://github.com/Alpha-Park/genpark-least-to-most-subgoal-planner-skill)
- [Lempel ziv welch lzw compression](https://github.com/Alpha-Park/genpark-lempel-ziv-welch-lzw-compression-skill)
- [Levenshtein damerau fuzzy string aligner](https://github.com/Alpha-Park/genpark-levenshtein-damerau-fuzzy-string-aligner-skill)
- [Linear sprint velocity cycle forecaster](https://github.com/Alpha-Park/genpark-linear-sprint-velocity-cycle-forecaster-skill)
- [Lion evolved sign momentum](https://github.com/Alpha-Park/genpark-lion-evolved-sign-momentum-skill)
- [Live artifact version diff tracker](https://github.com/Alpha-Park/genpark-live-artifact-version-diff-tracker-skill)
- [Llm gateway fallback circuit breaker](https://github.com/Alpha-Park/genpark-llm-gateway-fallback-circuit-breaker-skill)
- [Llm tool call repair fuzzy json parser](https://github.com/Alpha-Park/genpark-llm-tool-call-repair-fuzzy-json-parser-skill)
- [Lmax disruptor ring buffer](https://github.com/Alpha-Park/genpark-lmax-disruptor-ring-buffer-skill)
- [Locality sensitive hashing lsh cosine](https://github.com/Alpha-Park/genpark-locality-sensitive-hashing-lsh-cosine-skill)
- [Lock free treiber stack atomic cas](https://github.com/Alpha-Park/genpark-lock-free-treiber-stack-atomic-cas-skill)
- [Long horizon intent drift aligner](https://github.com/Alpha-Park/genpark-long-horizon-intent-drift-aligner-skill)
- [Lookahead k step optimizer](https://github.com/Alpha-Park/genpark-lookahead-k-step-optimizer-skill)
- [Loop invariant code motion licm](https://github.com/Alpha-Park/genpark-loop-invariant-code-motion-licm-skill)
- [Loop invariant induction prover](https://github.com/Alpha-Park/genpark-loop-invariant-induction-prover-skill)
- [Lost in transit shipping claim resolver](https://github.com/Alpha-Park/genpark-lost-in-transit-shipping-claim-resolver-skill)
- [Loyalty points redemption arbitrage calculator](https://github.com/Alpha-Park/genpark-loyalty-points-redemption-arbitrage-calculator-skill)
- [Ltl model checker buchi](https://github.com/Alpha-Park/genpark-ltl-model-checker-buchi-skill)
- [Lu factorization partial pivoting lup](https://github.com/Alpha-Park/genpark-lu-factorization-partial-pivoting-lup-skill)
- [Marching cubes isosurface extractor](https://github.com/Alpha-Park/genpark-marching-cubes-isosurface-extractor-skill)
- [Markov decision process value iteration](https://github.com/Alpha-Park/genpark-markov-decision-process-value-iteration-skill)
- [Marzullo clock synchronization](https://github.com/Alpha-Park/genpark-marzullo-clock-synchronization-skill)
- [Maximal marginal relevance mmr reranker](https://github.com/Alpha-Park/genpark-maximal-marginal-relevance-mmr-reranker-skill)
- [Mcp tool definition pydantic synthesizer](https://github.com/Alpha-Park/genpark-mcp-tool-definition-pydantic-synthesizer-skill)
- [Mel filterbank log spectrogram](https://github.com/Alpha-Park/genpark-mel-filterbank-log-spectrogram-skill)
- [Merkle mountain range mmr accumulator](https://github.com/Alpha-Park/genpark-merkle-mountain-range-mmr-accumulator-skill)
- [Merkle mountain range mmr](https://github.com/Alpha-Park/genpark-merkle-mountain-range-mmr-skill)
- [Message passing weisfeiler lehman](https://github.com/Alpha-Park/genpark-message-passing-weisfeiler-lehman-skill)
- [Michael scott lock free queue](https://github.com/Alpha-Park/genpark-michael-scott-lock-free-queue-skill)
- [Michael scott lockfree queue](https://github.com/Alpha-Park/genpark-michael-scott-lockfree-queue-skill)
- [Min cost max flow successive shortest path](https://github.com/Alpha-Park/genpark-min-cost-max-flow-successive-shortest-path-skill)
- [Minimax alpha beta adversarial search](https://github.com/Alpha-Park/genpark-minimax-alpha-beta-adversarial-search-skill)
- [Misra gries heavy hitters stream](https://github.com/Alpha-Park/genpark-misra-gries-heavy-hitters-stream-skill)
- [Modal temporal ltl model checker](https://github.com/Alpha-Park/genpark-modal-temporal-ltl-model-checker-skill)
- [Moller trumbore 3d ray triangle intersection](https://github.com/Alpha-Park/genpark-moller-trumbore-3d-ray-triangle-intersection-skill)
- [Monte carlo cfr poker engine](https://github.com/Alpha-Park/genpark-monte-carlo-cfr-poker-engine-skill)
- [Monte carlo tree search agent planner](https://github.com/Alpha-Park/genpark-monte-carlo-tree-search-agent-planner-skill)
- [Multi agent consensus voting protocol](https://github.com/Alpha-Park/genpark-multi-agent-consensus-voting-protocol-skill)
- [Multi agent debate consensus verifier](https://github.com/Alpha-Park/genpark-multi-agent-debate-consensus-verifier-skill)
- [Multi agent round robin turn orchestrator](https://github.com/Alpha-Park/genpark-multi-agent-round-robin-turn-orchestrator-skill)
- [Multi armed bandit ucb1 thompson sampling](https://github.com/Alpha-Park/genpark-multi-armed-bandit-ucb1-thompson-sampling-skill)
- [Multi candidate self consistency majority voter](https://github.com/Alpha-Park/genpark-multi-candidate-self-consistency-majority-voter-skill)
- [Multi cart shipping tax arbitrage optimizer](https://github.com/Alpha-Park/genpark-multi-cart-shipping-tax-arbitrage-optimizer-skill)
- [Multi gpu tensor parallel sharding planner](https://github.com/Alpha-Park/genpark-multi-gpu-tensor-parallel-sharding-planner-skill)
- [Multi model cost latency router](https://github.com/Alpha-Park/genpark-multi-model-cost-latency-router-skill)
- [Multi paxos distributed consensus state machine](https://github.com/Alpha-Park/genpark-multi-paxos-distributed-consensus-state-machine-skill)
- [Multi step function calling dag planner](https://github.com/Alpha-Park/genpark-multi-step-function-calling-dag-planner-skill)
- [Multi step web form fill orchestrator](https://github.com/Alpha-Park/genpark-multi-step-web-form-fill-orchestrator-skill)
- [Multi stop vehicle route tsp optimizer](https://github.com/Alpha-Park/genpark-multi-stop-vehicle-route-tsp-optimizer-skill)
- [Multi tenant agent isolation sandbox](https://github.com/Alpha-Park/genpark-multi-tenant-agent-isolation-sandbox-skill)
- [Multi touch ad attribution shapley resolver](https://github.com/Alpha-Park/genpark-multi-touch-ad-attribution-shapley-resolver-skill)
- [Multidimensional pricing matrix engine](https://github.com/Alpha-Park/genpark-multidimensional-pricing-matrix-engine-skill)
- [Multihop research query decomposer](https://github.com/Alpha-Park/genpark-multihop-research-query-decomposer-skill)
- [Multiversion timestamp ordering mvto](https://github.com/Alpha-Park/genpark-multiversion-timestamp-ordering-mvto-skill)
- [Mvcc snapshot isolation engine](https://github.com/Alpha-Park/genpark-mvcc-snapshot-isolation-engine-skill)
- [Mvcc snapshot isolation storage](https://github.com/Alpha-Park/genpark-mvcc-snapshot-isolation-storage-skill)
- [Nash equilibrium bimatrix support enumeration](https://github.com/Alpha-Park/genpark-nash-equilibrium-bimatrix-support-enumeration-skill)
- [Natural language cte sql synthesizer](https://github.com/Alpha-Park/genpark-natural-language-cte-sql-synthesizer-skill)
- [Needleman wunsch global aligner](https://github.com/Alpha-Park/genpark-needleman-wunsch-global-aligner-skill)
- [Needleman wunsch global sequence alignment](https://github.com/Alpha-Park/genpark-needleman-wunsch-global-sequence-alignment-skill)
- [Negative hypothesis failed patch indexer](https://github.com/Alpha-Park/genpark-negative-hypothesis-failed-patch-indexer-skill)
- [Neighbor joining phylogenetic tree](https://github.com/Alpha-Park/genpark-neighbor-joining-phylogenetic-tree-skill)
- [Neuro symbolic prolog unifier](https://github.com/Alpha-Park/genpark-neuro-symbolic-prolog-unifier-skill)
- [Omaha browser update orchestrator](https://github.com/Alpha-Park/genpark-omaha-browser-update-orchestrator-skill)
- [Openapi to mock service synthesizer](https://github.com/Alpha-Park/genpark-openapi-to-mock-service-synthesizer-skill)
- [Openclaw genteam agent channel runtime](https://github.com/Alpha-Park/genpark-openclaw-genteam-agent-channel-runtime-skill)
- [Optimistic concurrency control occ](https://github.com/Alpha-Park/genpark-optimistic-concurrency-control-occ-skill)
- [Or set crdt observed removed](https://github.com/Alpha-Park/genpark-or-set-crdt-observed-removed-skill)
- [Order flow imbalance ofi](https://github.com/Alpha-Park/genpark-order-flow-imbalance-ofi-skill)
- [Paillier partially homomorphic encryption](https://github.com/Alpha-Park/genpark-paillier-partially-homomorphic-encryption-skill)
- [Pairwise preference dpo loss tracker](https://github.com/Alpha-Park/genpark-pairwise-preference-dpo-loss-tracker-skill)
- [Particle filter monte carlo localization](https://github.com/Alpha-Park/genpark-particle-filter-monte-carlo-localization-skill)
- [Pastry prefix routing mesh](https://github.com/Alpha-Park/genpark-pastry-prefix-routing-mesh-skill)
- [Pbft practical byzantine fault tolerance](https://github.com/Alpha-Park/genpark-pbft-practical-byzantine-fault-tolerance-skill)
- [Pbft three phase consensus engine](https://github.com/Alpha-Park/genpark-pbft-three-phase-consensus-engine-skill)
- [Pedersen vector commitment homomorphic](https://github.com/Alpha-Park/genpark-pedersen-vector-commitment-homomorphic-skill)
- [Peephole optimizer pattern rewriter](https://github.com/Alpha-Park/genpark-peephole-optimizer-pattern-rewriter-skill)
- [Peephole window algebraic simplifier](https://github.com/Alpha-Park/genpark-peephole-window-algebraic-simplifier-skill)
- [Percolator distributed snapshot transactions](https://github.com/Alpha-Park/genpark-percolator-distributed-snapshot-transactions-skill)
- [Persistent homology vietoris rips](https://github.com/Alpha-Park/genpark-persistent-homology-vietoris-rips-skill)
- [Petri net reachability invariants](https://github.com/Alpha-Park/genpark-petri-net-reachability-invariants-skill)
- [Phonetic homophone stt disambiguator](https://github.com/Alpha-Park/genpark-phonetic-homophone-stt-disambiguator-skill)
- [Pitch synchronous overlap add psola](https://github.com/Alpha-Park/genpark-pitch-synchronous-overlap-add-psola-skill)
- [Plan repair dynamic re anchoring](https://github.com/Alpha-Park/genpark-plan-repair-dynamic-re-anchoring-skill)
- [Pn counter crdt distributed state](https://github.com/Alpha-Park/genpark-pn-counter-crdt-distributed-state-skill)
- [Poincare ball hyperbolic geometry](https://github.com/Alpha-Park/genpark-poincare-ball-hyperbolic-geometry-skill)
- [Polynomial vector commitment kzg](https://github.com/Alpha-Park/genpark-polynomial-vector-commitment-kzg-skill)
- [Poseidon prime sponge hash](https://github.com/Alpha-Park/genpark-poseidon-prime-sponge-hash-skill)
- [Post call crm action dispatcher](https://github.com/Alpha-Park/genpark-post-call-crm-action-dispatcher-skill)
- [Post purchase milestone exception predictor](https://github.com/Alpha-Park/genpark-post-purchase-milestone-exception-predictor-skill)
- [Potential field swarm navigation](https://github.com/Alpha-Park/genpark-potential-field-swarm-navigation-skill)
- [Ppo clipped surrogate engine](https://github.com/Alpha-Park/genpark-ppo-clipped-surrogate-engine-skill)
- [Pre purchase return fraud propensity scorer](https://github.com/Alpha-Park/genpark-pre-purchase-return-fraud-propensity-scorer-skill)
- [Predictive ltv churn reengagement trigger](https://github.com/Alpha-Park/genpark-predictive-ltv-churn-reengagement-trigger-skill)
- [Prefix caching kv state reuse](https://github.com/Alpha-Park/genpark-prefix-caching-kv-state-reuse-skill)
- [Presburger arithmetic linear integer solver](https://github.com/Alpha-Park/genpark-presburger-arithmetic-linear-integer-solver-skill)
- [Pricing model iteration simulator](https://github.com/Alpha-Park/genpark-pricing-model-iteration-simulator-skill)
- [Pricing tier agent](https://github.com/Alpha-Park/genpark-pricing-tier-agent-skill)
- [Process cgroup oom cpu quota arbiter](https://github.com/Alpha-Park/genpark-process-cgroup-oom-cpu-quota-arbiter-skill)
- [Prometheus exponential histogram bucket](https://github.com/Alpha-Park/genpark-prometheus-exponential-histogram-bucket-skill)
- [Prompt compression token pruning](https://github.com/Alpha-Park/genpark-prompt-compression-token-pruning-skill)
- [Prompt semantic cache similarity dedup](https://github.com/Alpha-Park/genpark-prompt-semantic-cache-similarity-dedup-skill)
- [Propensity score inverse probability weighting](https://github.com/Alpha-Park/genpark-propensity-score-inverse-probability-weighting-skill)
- [Protocol buffers varint wire encoder](https://github.com/Alpha-Park/genpark-protocol-buffers-varint-wire-encoder-skill)
- [Pull request breaking api change sentinel](https://github.com/Alpha-Park/genpark-pull-request-breaking-api-change-sentinel-skill)
- [Pull request semantic risk blast radius scorer](https://github.com/Alpha-Park/genpark-pull-request-semantic-risk-blast-radius-scorer-skill)
- [Q learning temporal difference rl](https://github.com/Alpha-Park/genpark-q-learning-temporal-difference-rl-skill)
- [Quadratic arithmetic program qap r1cs](https://github.com/Alpha-Park/genpark-quadratic-arithmetic-program-qap-r1cs-skill)
- [Quantum phase estimation qpe fourier](https://github.com/Alpha-Park/genpark-quantum-phase-estimation-qpe-fourier-skill)
- [Quantum shor period finding](https://github.com/Alpha-Park/genpark-quantum-shor-period-finding-skill)
- [Quantum state vector simulator](https://github.com/Alpha-Park/genpark-quantum-state-vector-simulator-skill)
- [Quantum statevector simulator](https://github.com/Alpha-Park/genpark-quantum-statevector-simulator-skill)
- [Quaternion rotation so3 manifold](https://github.com/Alpha-Park/genpark-quaternion-rotation-so3-manifold-skill)
- [Query intent router](https://github.com/Alpha-Park/genpark-query-intent-router-skill)
- [Quic multiplexed stream framing](https://github.com/Alpha-Park/genpark-quic-multiplexed-stream-framing-skill)
- [Raft distributed consensus state machine](https://github.com/Alpha-Park/genpark-raft-distributed-consensus-state-machine-skill)
- [Raft leader election heartbeat consensus](https://github.com/Alpha-Park/genpark-raft-leader-election-heartbeat-consensus-skill)
- [Raft log compaction snapshot](https://github.com/Alpha-Park/genpark-raft-log-compaction-snapshot-skill)
- [Raft state machine replication](https://github.com/Alpha-Park/genpark-raft-state-machine-replication-skill)
- [Ragas faithfulness answer relevance evaluator](https://github.com/Alpha-Park/genpark-ragas-faithfulness-answer-relevance-evaluator-skill)
- [Rank order temporal spike encoder](https://github.com/Alpha-Park/genpark-rank-order-temporal-spike-encoder-skill)
- [Raycast script command palette router](https://github.com/Alpha-Park/genpark-raycast-script-command-palette-router-skill)
- [Rdfs forward chaining reasoner](https://github.com/Alpha-Park/genpark-rdfs-forward-chaining-reasoner-skill)
- [Read copy update rcu grace period](https://github.com/Alpha-Park/genpark-read-copy-update-rcu-grace-period-skill)
- [Realtime ast code completion snippet ranker](https://github.com/Alpha-Park/genpark-realtime-ast-code-completion-snippet-ranker-skill)
- [Recursive descent ast parser](https://github.com/Alpha-Park/genpark-recursive-descent-ast-parser-skill)
- [Reed solomon error correction codec](https://github.com/Alpha-Park/genpark-reed-solomon-error-correction-codec-skill)
- [Reflexion verbal reinforcement](https://github.com/Alpha-Park/genpark-reflexion-verbal-reinforcement-skill)
- [Reinforcement fine tuning trajectory buffer](https://github.com/Alpha-Park/genpark-reinforcement-fine-tuning-trajectory-buffer-skill)
- [Related queries](https://github.com/Alpha-Park/genpark-related-queries-skill)
- [Reservoir computing echo state network](https://github.com/Alpha-Park/genpark-reservoir-computing-echo-state-network-skill)
- [Reservoir sampling algorithm r](https://github.com/Alpha-Park/genpark-reservoir-sampling-algorithm-r-skill)
- [Responsive wireframe component layout generator](https://github.com/Alpha-Park/genpark-responsive-wireframe-component-layout-generator-skill)
- [Review sentiment authenticity ftc detector](https://github.com/Alpha-Park/genpark-review-sentiment-authenticity-ftc-detector-skill)
- [Reviews sentiment agent](https://github.com/Alpha-Park/genpark-reviews-sentiment-agent-skill)
- [Reynolds boids flocking consensus](https://github.com/Alpha-Park/genpark-reynolds-boids-flocking-consensus-skill)
- [Riemannian manifold gradient descent](https://github.com/Alpha-Park/genpark-riemannian-manifold-gradient-descent-skill)
- [Ring token distributed election](https://github.com/Alpha-Park/genpark-ring-token-distributed-election-skill)
- [Robinson first order unification](https://github.com/Alpha-Park/genpark-robinson-first-order-unification-skill)
- [Robotics quadruped gait telemetry analyzer](https://github.com/Alpha-Park/genpark-robotics-quadruped-gait-telemetry-analyzer-skill)
- [Ros2 micro telemetry qos negotiator](https://github.com/Alpha-Park/genpark-ros2-micro-telemetry-qos-negotiator-skill)
- [Rubinstein alternating offers bargaining](https://github.com/Alpha-Park/genpark-rubinstein-alternating-offers-bargaining-skill)
- [Runtime variable diff state inspector](https://github.com/Alpha-Park/genpark-runtime-variable-diff-state-inspector-skill)
- [Safe tool execution isolation containment](https://github.com/Alpha-Park/genpark-safe-tool-execution-isolation-containment-skill)
- [Saga orchestrator compensating transaction](https://github.com/Alpha-Park/genpark-saga-orchestrator-compensating-transaction-skill)
- [Saga orchestrator compensating tx](https://github.com/Alpha-Park/genpark-saga-orchestrator-compensating-tx-skill)
- [Sandbox syscall seccomp policy generator](https://github.com/Alpha-Park/genpark-sandbox-syscall-seccomp-policy-generator-skill)
- [Scalar quantization sq8 vector compressor](https://github.com/Alpha-Park/genpark-scalar-quantization-sq8-vector-compressor-skill)
- [Schnorr threshold multisig musig2](https://github.com/Alpha-Park/genpark-schnorr-threshold-multisig-musig2-skill)
- [Scientific consensus ratio mapper](https://github.com/Alpha-Park/genpark-scientific-consensus-ratio-mapper-skill)
- [Se3 equivariant message passing](https://github.com/Alpha-Park/genpark-se3-equivariant-message-passing-skill)
- [Search analytics](https://github.com/Alpha-Park/genpark-search-analytics-skill)
- [Search auto suggest](https://github.com/Alpha-Park/genpark-search-auto-suggest-skill)
- [Search integration](https://github.com/Alpha-Park/genpark-search-integration-skill)
- [Search redirection](https://github.com/Alpha-Park/genpark-search-redirection-skill)
- [Search synonym agent](https://github.com/Alpha-Park/genpark-search-synonym-agent-skill)
- [Selective answering abstention gatekeeper](https://github.com/Alpha-Park/genpark-selective-answering-abstention-gatekeeper-skill)
- [Self consistency majority voter](https://github.com/Alpha-Park/genpark-self-consistency-majority-voter-skill)
- [Self healing dom semantic selector](https://github.com/Alpha-Park/genpark-self-healing-dom-semantic-selector-skill)
- [Selinger cost based optimizer](https://github.com/Alpha-Park/genpark-selinger-cost-based-optimizer-skill)
- [Semantic chunk boundary sliding window](https://github.com/Alpha-Park/genpark-semantic-chunk-boundary-sliding-window-skill)
- [Semantic chunk hierarchy re ranker](https://github.com/Alpha-Park/genpark-semantic-chunk-hierarchy-re-ranker-skill)
- [Semantic entropy hallucination estimator](https://github.com/Alpha-Park/genpark-semantic-entropy-hallucination-estimator-skill)
- [Seqlock sequential lock reader writer](https://github.com/Alpha-Park/genpark-seqlock-sequential-lock-reader-writer-skill)
- [Serializable snapshot isolation ssi](https://github.com/Alpha-Park/genpark-serializable-snapshot-isolation-ssi-skill)
- [Sgdr cosine annealing restarts](https://github.com/Alpha-Park/genpark-sgdr-cosine-annealing-restarts-skill)
- [Shamir secret sharing gf256](https://github.com/Alpha-Park/genpark-shamir-secret-sharing-gf256-skill)
- [Shamir secret sharing threshold scheme](https://github.com/Alpha-Park/genpark-shamir-secret-sharing-threshold-scheme-skill)
- [Shannon entropy huffman canonical coder](https://github.com/Alpha-Park/genpark-shannon-entropy-huffman-canonical-coder-skill)
- [Shannon entropy mutual information estimator](https://github.com/Alpha-Park/genpark-shannon-entropy-mutual-information-estimator-skill)
- [Shapley q value credit assignment](https://github.com/Alpha-Park/genpark-shapley-q-value-credit-assignment-skill)
- [Shapley value cooperative game allocator](https://github.com/Alpha-Park/genpark-shapley-value-cooperative-game-allocator-skill)
- [Shapley value cooperative game](https://github.com/Alpha-Park/genpark-shapley-value-cooperative-game-skill)
- [Shock capturing riemann roe](https://github.com/Alpha-Park/genpark-shock-capturing-riemann-roe-skill)
- [Short time fourier transform stft spectrogram](https://github.com/Alpha-Park/genpark-short-time-fourier-transform-stft-spectrogram-skill)
- [Shortform hook retention scorer](https://github.com/Alpha-Park/genpark-shortform-hook-retention-scorer-skill)
- [Simd vector lane engine](https://github.com/Alpha-Park/genpark-simd-vector-lane-engine-skill)
- [Simplex linear programming solver](https://github.com/Alpha-Park/genpark-simplex-linear-programming-solver-skill)
- [Simplex linear real arithmetic qflra](https://github.com/Alpha-Park/genpark-simplex-linear-real-arithmetic-qflra-skill)
- [Simplicial complex boundary operator](https://github.com/Alpha-Park/genpark-simplicial-complex-boundary-operator-skill)
- [Simulated annealing combinatorial optimizer](https://github.com/Alpha-Park/genpark-simulated-annealing-combinatorial-optimizer-skill)
- [Singular value decomposition svd power iteration](https://github.com/Alpha-Park/genpark-singular-value-decomposition-svd-power-iteration-skill)
- [Size recommendation](https://github.com/Alpha-Park/genpark-size-recommendation-skill)
- [Small step operational semantics evaluator](https://github.com/Alpha-Park/genpark-small-step-operational-semantics-evaluator-skill)
- [Smith waterman local aligner](https://github.com/Alpha-Park/genpark-smith-waterman-local-aligner-skill)
- [Smith waterman local sequence aligner](https://github.com/Alpha-Park/genpark-smith-waterman-local-sequence-aligner-skill)
- [Smoothed particle hydrodynamics sph](https://github.com/Alpha-Park/genpark-smoothed-particle-hydrodynamics-sph-skill)
- [Social post designer](https://github.com/Alpha-Park/genpark-social-post-designer-skill)
- [Spa network idle settlement waiter](https://github.com/Alpha-Park/genpark-spa-network-idle-settlement-waiter-skill)
- [Sparkle macos update appcast sentinel](https://github.com/Alpha-Park/genpark-sparkle-macos-update-appcast-sentinel-skill)
- [Sparkpage synthesis engine](https://github.com/Alpha-Park/genpark-sparkpage-synthesis-engine-skill)
- [Sparse conditional constant propagation sccp](https://github.com/Alpha-Park/genpark-sparse-conditional-constant-propagation-sccp-skill)
- [Sparse merkle tree smt exclusion](https://github.com/Alpha-Park/genpark-sparse-merkle-tree-smt-exclusion-skill)
- [Sparse spmm csr kernel](https://github.com/Alpha-Park/genpark-sparse-spmm-csr-kernel-skill)
- [Speculative decoding draft acceptance evaluator](https://github.com/Alpha-Park/genpark-speculative-decoding-draft-acceptance-evaluator-skill)
- [Speculative decoding draft verifier](https://github.com/Alpha-Park/genpark-speculative-decoding-draft-verifier-skill)
- [Spike timing dependent plasticity stdp](https://github.com/Alpha-Park/genpark-spike-timing-dependent-plasticity-stdp-skill)
- [Split shipment warehouse distance minimizer](https://github.com/Alpha-Park/genpark-split-shipment-warehouse-distance-minimizer-skill)
- [Sponge poseidon hash zk friendly](https://github.com/Alpha-Park/genpark-sponge-poseidon-hash-zk-friendly-skill)
- [Ssa dead code elimination](https://github.com/Alpha-Park/genpark-ssa-dead-code-elimination-skill)
- [Ssa destruction phi elimination](https://github.com/Alpha-Park/genpark-ssa-destruction-phi-elimination-skill)
- [Stack bytecode virtual machine](https://github.com/Alpha-Park/genpark-stack-bytecode-virtual-machine-skill)
- [Stack trace symbolic fault localizer](https://github.com/Alpha-Park/genpark-stack-trace-symbolic-fault-localizer-skill)
- [Stateful agent dag node executor](https://github.com/Alpha-Park/genpark-stateful-agent-dag-node-executor-skill)
- [Statistical anomaly zscore detector](https://github.com/Alpha-Park/genpark-statistical-anomaly-zscore-detector-skill)
- [Stoer wagner global min cut](https://github.com/Alpha-Park/genpark-stoer-wagner-global-min-cut-skill)
- [Strict two phase locking s2pl](https://github.com/Alpha-Park/genpark-strict-two-phase-locking-s2pl-skill)
- [Strict two phase locking ss2pl deadlock](https://github.com/Alpha-Park/genpark-strict-two-phase-locking-ss2pl-deadlock-skill)
- [Structural causal model dag interventional engine](https://github.com/Alpha-Park/genpark-structural-causal-model-dag-interventional-engine-skill)
- [Structured data diff patcher](https://github.com/Alpha-Park/genpark-structured-data-diff-patcher-skill)
- [Structured extract schema validator](https://github.com/Alpha-Park/genpark-structured-extract-schema-validator-skill)
- [Structured output regex grammar fence](https://github.com/Alpha-Park/genpark-structured-output-regex-grammar-fence-skill)
- [Study methodology bias detector](https://github.com/Alpha-Park/genpark-study-methodology-bias-detector-skill)
- [Subagent budget token quota sentinel](https://github.com/Alpha-Park/genpark-subagent-budget-token-quota-sentinel-skill)
- [Subscription churn mitigation frequency tuner](https://github.com/Alpha-Park/genpark-subscription-churn-mitigation-frequency-tuner-skill)
- [Surface code syndrome decoder](https://github.com/Alpha-Park/genpark-surface-code-syndrome-decoder-skill)
- [Sutherland hodgman polygon clipping](https://github.com/Alpha-Park/genpark-sutherland-hodgman-polygon-clipping-skill)
- [Swarm deadlock detector](https://github.com/Alpha-Park/genpark-swarm-deadlock-detector-skill)
- [Swarm state checkpoint rollback engine](https://github.com/Alpha-Park/genpark-swarm-state-checkpoint-rollback-engine-skill)
- [Sweep line bentley ottmann](https://github.com/Alpha-Park/genpark-sweep-line-bentley-ottmann-skill)
- [Synaptic intelligence path integral](https://github.com/Alpha-Park/genpark-synaptic-intelligence-path-integral-skill)
- [Synthetic persona interview simulator](https://github.com/Alpha-Park/genpark-synthetic-persona-interview-simulator-skill)
- [Synthetic tabular correlation copula aligner](https://github.com/Alpha-Park/genpark-synthetic-tabular-correlation-copula-aligner-skill)
- [Synthetic text ngram diversity entropy scorer](https://github.com/Alpha-Park/genpark-synthetic-text-ngram-diversity-entropy-scorer-skill)
- [Tapestry decentralized object location](https://github.com/Alpha-Park/genpark-tapestry-decentralized-object-location-skill)
- [Tar archive path traversal slip sanitizer](https://github.com/Alpha-Park/genpark-tar-archive-path-traversal-slip-sanitizer-skill)
- [Tcc try confirm cancel engine](https://github.com/Alpha-Park/genpark-tcc-try-confirm-cancel-engine-skill)
- [Tcmalloc thread cache span heap](https://github.com/Alpha-Park/genpark-tcmalloc-thread-cache-span-heap-skill)
- [Tcp reno cubic dual stack engine](https://github.com/Alpha-Park/genpark-tcp-reno-cubic-dual-stack-engine-skill)
- [Tdigest streaming quantile sketch](https://github.com/Alpha-Park/genpark-tdigest-streaming-quantile-sketch-skill)
- [Temperature scaling confidence calibrator](https://github.com/Alpha-Park/genpark-temperature-scaling-confidence-calibrator-skill)
- [Temporal plan simple temporal network stn](https://github.com/Alpha-Park/genpark-temporal-plan-simple-temporal-network-stn-skill)
- [Tensor core wmma emulator](https://github.com/Alpha-Park/genpark-tensor-core-wmma-emulator-skill)
- [Terminal session semantic history search](https://github.com/Alpha-Park/genpark-terminal-session-semantic-history-search-skill)
- [Test dual org](https://github.com/Alpha-Park/genpark-test-dual-org-skill)
- [Three phase commit non blocking](https://github.com/Alpha-Park/genpark-three-phase-commit-non-blocking-skill)
- [Threshold bls signature aggregation](https://github.com/Alpha-Park/genpark-threshold-bls-signature-aggregation-skill)
- [Timestamp ordering tso concurrency](https://github.com/Alpha-Park/genpark-timestamp-ordering-tso-concurrency-skill)
- [Token cost rate limit quota guard](https://github.com/Alpha-Park/genpark-token-cost-rate-limit-quota-guard-skill)
- [Tool usage telemetry efficiency profiler](https://github.com/Alpha-Park/genpark-tool-usage-telemetry-efficiency-profiler-skill)
- [Top trading cycles ttc](https://github.com/Alpha-Park/genpark-top-trading-cycles-ttc-skill)
- [Topical dialog boundary deflection router](https://github.com/Alpha-Park/genpark-topical-dialog-boundary-deflection-router-skill)
- [Tree of thoughts mcts evaluator](https://github.com/Alpha-Park/genpark-tree-of-thoughts-mcts-evaluator-skill)
- [Tumbling sliding session windowing](https://github.com/Alpha-Park/genpark-tumbling-sliding-session-windowing-skill)
- [Turn by turn conversational slot filler](https://github.com/Alpha-Park/genpark-turn-by-turn-conversational-slot-filler-skill)
- [Two handed clock page replacement](https://github.com/Alpha-Park/genpark-two-handed-clock-page-replacement-skill)
- [Two phase commit coordinator](https://github.com/Alpha-Park/genpark-two-phase-commit-coordinator-skill)
- [Two phase commit sink exactly once](https://github.com/Alpha-Park/genpark-two-phase-commit-sink-exactly-once-skill)
- [Two phase locking wound wait](https://github.com/Alpha-Park/genpark-two-phase-locking-wound-wait-skill)
- [Untyped lambda calculus beta reducer](https://github.com/Alpha-Park/genpark-untyped-lambda-calculus-beta-reducer-skill)
- [Upgma phylogenetic tree builder](https://github.com/Alpha-Park/genpark-upgma-phylogenetic-tree-builder-skill)
- [Usage based billing metering engine](https://github.com/Alpha-Park/genpark-usage-based-billing-metering-engine-skill)
- [Variable elimination bayesian network](https://github.com/Alpha-Park/genpark-variable-elimination-bayesian-network-skill)
- [Vcg auction truthful mechanism](https://github.com/Alpha-Park/genpark-vcg-auction-truthful-mechanism-skill)
- [Vector clock causal broadcast](https://github.com/Alpha-Park/genpark-vector-clock-causal-broadcast-skill)
- [Vector clock causality tracker](https://github.com/Alpha-Park/genpark-vector-clock-causality-tracker-skill)
- [Verifiable delay function vdf evaluator](https://github.com/Alpha-Park/genpark-verifiable-delay-function-vdf-evaluator-skill)
- [Verkle tree ipa commitment](https://github.com/Alpha-Park/genpark-verkle-tree-ipa-commitment-skill)
- [Vibe coding ast component patcher](https://github.com/Alpha-Park/genpark-vibe-coding-ast-component-patcher-skill)
- [Vickrey clarke groves vcg auction mechanism](https://github.com/Alpha-Park/genpark-vickrey-clarke-groves-vcg-auction-mechanism-skill)
- [Viewstamped replication vr consensus](https://github.com/Alpha-Park/genpark-viewstamped-replication-vr-consensus-skill)
- [Virtual structure formation control](https://github.com/Alpha-Park/genpark-virtual-structure-formation-control-skill)
- [Viterbi convolutional codec engine](https://github.com/Alpha-Park/genpark-viterbi-convolutional-codec-engine-skill)
- [Viterbi hidden markov cpg islands](https://github.com/Alpha-Park/genpark-viterbi-hidden-markov-cpg-islands-skill)
- [Volcano iterator query execution](https://github.com/Alpha-Park/genpark-volcano-iterator-query-execution-skill)
- [Voronoi coverage lloyd swarm](https://github.com/Alpha-Park/genpark-voronoi-coverage-lloyd-swarm-skill)
- [Vorticity streamfunction navier stokes](https://github.com/Alpha-Park/genpark-vorticity-streamfunction-navier-stokes-skill)
- [Waterfall enrichment orchestrator](https://github.com/Alpha-Park/genpark-waterfall-enrichment-orchestrator-skill)
- [Weight quantization kquants block packer](https://github.com/Alpha-Park/genpark-weight-quantization-kquants-block-packer-skill)
- [Weighted borda count preference aggregator](https://github.com/Alpha-Park/genpark-weighted-borda-count-preference-aggregator-skill)
- [Welch power spectral density](https://github.com/Alpha-Park/genpark-welch-power-spectral-density-skill)
- [Wesolowski vdf evaluator](https://github.com/Alpha-Park/genpark-wesolowski-vdf-evaluator-skill)
- [Workspace symbol semantic rename refactorer](https://github.com/Alpha-Park/genpark-workspace-symbol-semantic-rename-refactorer-skill)
- [Write ahead log aries recovery](https://github.com/Alpha-Park/genpark-write-ahead-log-aries-recovery-skill)
- [Write ahead log segment cleaner](https://github.com/Alpha-Park/genpark-write-ahead-log-segment-cleaner-skill)
- [Zab fast leader election zookeeper](https://github.com/Alpha-Park/genpark-zab-fast-leader-election-zookeeper-skill)
- [Zk rollup state transition circuit](https://github.com/Alpha-Park/genpark-zk-rollup-state-transition-circuit-skill)
- [Zx calculus circuit rewriter](https://github.com/Alpha-Park/genpark-zx-calculus-circuit-rewriter-skill)


### Phase 271: Computer Networking, Socket Protocols & Packet Filtering
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-tcp-ip-packet-checksum-parser-skill](https://github.com/Alpha-Park/genpark-tcp-ip-packet-checksum-parser-skill) | IPv4 header serialization, Internet checksum verification, and raw packet parsing engine | Service | [x] | Pure struct/socket |
| [genpark-leaky-bucket-token-bucket-rate-limiter-skill](https://github.com/Alpha-Park/genpark-leaky-bucket-token-bucket-rate-limiter-skill) | Token Bucket and Leaky Bucket traffic shaping, burst control, and API rate limiting engine | Service | [x] | Standard library |
| [genpark-sliding-window-flow-control-skill](https://github.com/Alpha-Park/genpark-sliding-window-flow-control-skill) | TCP sliding window flow control protocol with cumulative ACK and buffer management | Service | [x] | Standard library |
| [genpark-cidr-subnet-ip-routing-table-skill](https://github.com/Alpha-Park/genpark-cidr-subnet-ip-routing-table-skill) | CIDR IP prefix routing table with Longest Prefix Match (LPM) and subnet decomposition | Service | [x] | Standard library |
| [genpark-dns-wire-protocol-parser-skill](https://github.com/Alpha-Park/genpark-dns-wire-protocol-parser-skill) | DNS binary wire format packet builder, label compression reader, and header parser | Service | [x] | Pure struct |


### Phase 272: Information Theory, Lossless Data Compression & Entropy Coding
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-huffman-coding-entropy-tree-skill](https://github.com/Alpha-Park/genpark-huffman-coding-entropy-tree-skill) | Canonical Huffman coding tree generation, prefix-free binary bitstream packer, and Shannon entropy | Service | [x] | Pure math/heapq |
| [genpark-lzw-compression-dictionary-coder-skill](https://github.com/Alpha-Park/genpark-lzw-compression-dictionary-coder-skill) | Lempel-Ziv-Welch (LZW) dynamic dictionary lossless encoder and decoder | Service | [x] | Standard library |
| [genpark-arithmetic-coding-fractional-interval-skill](https://github.com/Alpha-Park/genpark-arithmetic-coding-fractional-interval-skill) | High-precision fractional range subdivision arithmetic compression encoder and decoder | Service | [x] | Standard library |
| [genpark-run-length-encoding-rle-delta-skill](https://github.com/Alpha-Park/genpark-run-length-encoding-rle-delta-skill) | Run-Length Encoding (RLE) and Delta-ZigZag differential integer serialization engine | Service | [x] | Standard library |
| [genpark-burrows-wheeler-transform-bwt-mtf-skill](https://github.com/Alpha-Park/genpark-burrows-wheeler-transform-bwt-mtf-skill) | Burrows-Wheeler Transform (BWT) and Move-To-Front (MTF) block sorting transformation | Service | [x] | Standard library |


### Phase 273: Numerical Linear Algebra, Matrix Decompositions & Eigenvalues
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-lu-decomposition-partial-pivoting-skill](https://github.com/Alpha-Park/genpark-lu-decomposition-partial-pivoting-skill) | Gaussian elimination with row partial pivoting (PLU decomposition) and linear system solver | Service | [x] | Standard library |
| [genpark-qr-decomposition-gram-schmidt-householder-skill](https://github.com/Alpha-Park/genpark-qr-decomposition-gram-schmidt-householder-skill) | QR matrix factorization via Gram-Schmidt orthogonalization for least-squares regression | Service | [x] | Pure math |
| [genpark-singular-value-decomposition-svd-truncated-skill](https://github.com/Alpha-Park/genpark-singular-value-decomposition-svd-truncated-skill) | Power iteration Truncated SVD for low-rank matrix approximation and latent embeddings | Service | [x] | Pure math |
| [genpark-cholesky-decomposition-spd-solver-skill](https://github.com/Alpha-Park/genpark-cholesky-decomposition-spd-solver-skill) | Cholesky factorization (A = L L^T) for symmetric positive-definite covariance matrices | Service | [x] | Pure math |
| [genpark-eigenvalue-power-iteration-jacobi-skill](https://github.com/Alpha-Park/genpark-eigenvalue-power-iteration-jacobi-skill) | Jacobi eigenvalue algorithm for real symmetric matrices and dominant eigenvector power iteration | Service | [x] | Pure math |


### Phase 274: Advanced Cryptography, Elliptic Curves & Zero-Knowledge Verification
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-elliptic-curve-secp256k1-point-math-skill](https://github.com/Alpha-Park/genpark-elliptic-curve-secp256k1-point-math-skill) | Weierstrass elliptic curve arithmetic, affine point addition, and double-and-add scalar multiplication | Service | [x] | Standard library |
| [genpark-shamir-secret-sharing-polynomial-skill](https://github.com/Alpha-Park/genpark-shamir-secret-sharing-polynomial-skill) | Shamir (k, n) threshold secret sharing via Lagrange polynomial interpolation over finite fields | Service | [x] | Pure secrets |
| [genpark-diffie-hellman-key-exchange-rfc3526-skill](https://github.com/Alpha-Park/genpark-diffie-hellman-key-exchange-rfc3526-skill) | Diffie-Hellman key agreement with RFC 3526 2048-bit MODP groups and HKDF derivation | Service | [x] | Pure hashlib/hmac |
| [genpark-schnorr-signature-discrete-log-skill](https://github.com/Alpha-Park/genpark-schnorr-signature-discrete-log-skill) | Schnorr signature scheme and non-interactive zero-knowledge identification verification | Service | [x] | Pure hashlib |
| [genpark-pedersen-commitment-homomorphic-skill](https://github.com/Alpha-Park/genpark-pedersen-commitment-homomorphic-skill) | Homomorphic cryptographic Pedersen commitments with blinding factors and additive verification | Service | [x] | Pure hashlib |


### Phase 275: Neural Network Architectures, Backpropagation & Automatic Differentiation
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-scalar-autograd-computational-graph-skill](https://github.com/Alpha-Park/genpark-scalar-autograd-computational-graph-skill) | Reverse-mode automatic differentiation engine with DAG tape and chain rule backpropagation | Service | [x] | Standard library |
| [genpark-dense-feedforward-mlp-backprop-skill](https://github.com/Alpha-Park/genpark-dense-feedforward-mlp-backprop-skill) | Dense multi-layer perceptron forward propagation, Xavier initialization, and gradient descent | Service | [x] | Standard library |
| [genpark-multi-head-scaled-dot-product-attention-skill](https://github.com/Alpha-Park/genpark-multi-head-scaled-dot-product-attention-skill) | Multi-head self-attention mechanism with scaled dot-product scoring and causal masking | Service | [x] | Standard library |
| [genpark-convolutional-2d-forward-backward-skill](https://github.com/Alpha-Park/genpark-convolutional-2d-forward-backward-skill) | 2D spatial convolution forward and backpropagation with kernel padding and strides | Service | [x] | Standard library |
| [genpark-layer-norm-rms-norm-regularization-skill](https://github.com/Alpha-Park/genpark-layer-norm-rms-norm-regularization-skill) | Layer normalization and RMSNorm regularization for transformer hidden representations | Service | [x] | Standard library |


### Phase 276: Robotics, Kinematics, Trajectory Planning & PID Control
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-forward-inverse-kinematics-dh-parameters-skill](https://github.com/Alpha-Park/genpark-forward-inverse-kinematics-dh-parameters-skill) | Denavit-Hartenberg coordinate frame transforms, forward kinematics, and analytical inverse kinematics | Service | [x] | Standard library |
| [genpark-pid-controller-anti-windup-derivative-filter-skill](https://github.com/Alpha-Park/genpark-pid-controller-anti-windup-derivative-filter-skill) | Industrial closed-loop PID controller with integrator anti-windup clamping and low-pass derivative filtering | Service | [x] | Standard library |
| [genpark-rapidly-exploring-random-tree-rrt-motion-planning-skill](https://github.com/Alpha-Park/genpark-rapidly-exploring-random-tree-rrt-motion-planning-skill) | Rapidly-exploring Random Tree (RRT) path and motion planner for collision-free robotic navigation in obstacle spaces | Service | [x] | Standard library |
| [genpark-dubins-path-nonholonomic-trajectory-generator-skill](https://github.com/Alpha-Park/genpark-dubins-path-nonholonomic-trajectory-generator-skill) | Nonholonomic Dubins curve trajectory planner for car-like vehicles with minimum turning radius constraints | Service | [x] | Standard library |
| [genpark-extended-kalman-filter-robot-localization-skill](https://github.com/Alpha-Park/genpark-extended-kalman-filter-robot-localization-skill) | Extended Kalman Filter (EKF) for non-linear mobile robot pose estimation and landmark sensor fusion | Service | [x] | Standard library |


### Phase 277: Formal Logic, SAT Solvers, DPLL & Automated Theorem Proving
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-dpll-sat-solver-cnf-backtracking-skill](https://github.com/Alpha-Park/genpark-dpll-sat-solver-cnf-backtracking-skill) | Davis-Putnam-Logemann-Loveland (DPLL) Boolean satisfiability solver with unit propagation and pure literal elimination | Service | [x] | Standard library |
| [genpark-binary-decision-diagram-bdd-canonicity-skill](https://github.com/Alpha-Park/genpark-binary-decision-diagram-bdd-canonicity-skill) | Reduced Ordered Binary Decision Diagram (ROBDD) engine with Shannon expansion and canonical ITE synthesis | Service | [x] | Standard library |
| [genpark-first-order-logic-resolution-refutation-skill](https://github.com/Alpha-Park/genpark-first-order-logic-resolution-refutation-skill) | First-Order Logic Robinson syntactic unifier with occurs-check and resolution refutation theorem prover | Service | [x] | Standard library |
| [genpark-horn-clause-forward-backward-chaining-skill](https://github.com/Alpha-Park/genpark-horn-clause-forward-backward-chaining-skill) | Definite Horn clause deductive engine supporting forward chaining fixpoint and goal-directed backward chaining | Service | [x] | Standard library |
| [genpark-sequent-calculus-proof-search-engine-skill](https://github.com/Alpha-Park/genpark-sequent-calculus-proof-search-engine-skill) | Gentzen propositional LK sequent calculus automated proof search engine for structural proof theory | Service | [x] | Standard library |


### Phase 278: Bioinformatics, Genomic Sequence Alignment & Molecular Geometry
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-smith-waterman-local-sequence-alignment-skill](https://github.com/Alpha-Park/genpark-smith-waterman-local-sequence-alignment-skill) | Smith-Waterman dynamic programming local genomic sequence alignment with gap penalties and score matrix traceback | Service | [x] | Standard library |
| [genpark-needleman-wunsch-global-sequence-alignment-skill](https://github.com/Alpha-Park/genpark-needleman-wunsch-global-sequence-alignment-skill) | Needleman-Wunsch dynamic programming algorithm for global biological sequence alignment and homological comparison | Service | [x] | Standard library |
| [genpark-burrows-wheeler-aligner-bwt-fm-index-skill](https://github.com/Alpha-Park/genpark-burrows-wheeler-aligner-bwt-fm-index-skill) | Ferragina-Manzini (FM-index) exact pattern matching and substring counting over genomic sequence collections | Service | [x] | Standard library |
| [genpark-protein-secondary-structure-chou-fasman-skill](https://github.com/Alpha-Park/genpark-protein-secondary-structure-chou-fasman-skill) | Chou-Fasman statistical conformational propensity predictor for protein secondary structure (helix, sheet, coil) | Service | [x] | Standard library |
| [genpark-molecular-distance-geometry-rmsd-superposition-skill](https://github.com/Alpha-Park/genpark-molecular-distance-geometry-rmsd-superposition-skill) | Kabsch algorithm for optimal 3D molecular coordinates alignment, rigid translation, and RMSD distance calculation | Service | [x] | Standard library |


### Phase 279: Convex Optimization, Quadratic Programming & Constrained Solvers
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-simplex-algorithm-linear-programming-skill](https://github.com/Alpha-Park/genpark-simplex-algorithm-linear-programming-skill) | Simplex tableau algorithm for primal linear programming (LP) with slack variables and pivot operations | Service | [x] | Standard library |
| [genpark-bfgs-quasi-newton-line-search-skill](https://github.com/Alpha-Park/genpark-bfgs-quasi-newton-line-search-skill) | Broyden-Fletcher-Goldfarb-Shanno (BFGS) quasi-Newton optimization with backtracking Armijo line search | Service | [x] | Standard library |
| [genpark-admm-distributed-consensus-optimization-skill](https://github.com/Alpha-Park/genpark-admm-distributed-consensus-optimization-skill) | Alternating Direction Method of Multipliers (ADMM) for Lasso sparse regression and distributed consensus optimization | Service | [x] | Standard library |
| [genpark-quadratic-programming-active-set-skill](https://github.com/Alpha-Park/genpark-quadratic-programming-active-set-skill) | Active-set Karush-Kuhn-Tucker (KKT) quadratic programming (QP) solver for quadratic costs with equality/inequality constraints | Service | [x] | Standard library |
| [genpark-interior-point-primal-dual-barrier-skill](https://github.com/Alpha-Park/genpark-interior-point-primal-dual-barrier-skill) | Logarithmic barrier interior-point method for non-linear inequality constrained convex optimization | Service | [x] | Standard library |


### Phase 280: Algorithmic Game Theory, Mechanism Design & Auction Mechanics
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-nash-equilibrium-lemke-howson-bimatrix-skill](https://github.com/Alpha-Park/genpark-nash-equilibrium-lemke-howson-bimatrix-skill) | Exact mixed-strategy Nash equilibrium solver for two-player strategic bimatrix normal-form games | Service | [x] | Standard library |
| [genpark-vickrey-clarke-groves-vcg-auction-mechanism-skill](https://github.com/Alpha-Park/genpark-vickrey-clarke-groves-vcg-auction-mechanism-skill) | Vickrey-Clarke-Groves (VCG) truthful, incentive-compatible combinatorial auction mechanism with Clarke pivot payments | Service | [x] | Standard library |
| [genpark-shapley-value-cooperative-game-attribution-skill](https://github.com/Alpha-Park/genpark-shapley-value-cooperative-game-attribution-skill) | Shapley value cooperative game attribution and coalitional marginal contribution calculation | Service | [x] | Standard library |
| [genpark-gale-shapley-deferred-acceptance-matching-skill](https://github.com/Alpha-Park/genpark-gale-shapley-deferred-acceptance-matching-skill) | Gale-Shapley deferred acceptance algorithm for stable two-sided matching and market design | Service | [x] | Standard library |
| [genpark-fictitious-play-regret-matching-game-skill](https://github.com/Alpha-Park/genpark-fictitious-play-regret-matching-game-skill) | Hart-Mas-Colell regret matching and fictitious play learning dynamics converging to correlated equilibria | Service | [x] | Standard library |


### Phase 281: Stochastic Calculus, Monte Carlo Simulation & SDEs
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-geometric-brownian-motion-euler-maruyama-skill](https://github.com/Alpha-Park/genpark-geometric-brownian-motion-euler-maruyama-skill) | Euler-Maruyama and Milstein numerical discretization solvers for Itô Stochastic Differential Equations (SDEs) | Service | [x] | Standard library |
| [genpark-ornstein-uhlenbeck-mean-reversion-process-skill](https://github.com/Alpha-Park/genpark-ornstein-uhlenbeck-mean-reversion-process-skill) | Ornstein-Uhlenbeck mean-reverting stochastic process with exact transition distributions and Vasicek calibration | Service | [x] | Standard library |
| [genpark-heston-stochastic-volatility-cir-process-skill](https://github.com/Alpha-Park/genpark-heston-stochastic-volatility-cir-process-skill) | Heston two-factor stochastic volatility model with Cox-Ingersoll-Ross (CIR) variance and Feller condition checking | Service | [x] | Standard library |
| [genpark-gillespie-stochastic-simulation-chemical-master-skill](https://github.com/Alpha-Park/genpark-gillespie-stochastic-simulation-chemical-master-skill) | Gillespie stochastic simulation algorithm (SSA / Direct Method) for jump Markov processes and chemical kinetics | Service | [x] | Standard library |
| [genpark-markov-chain-monte-carlo-metropolis-hastings-skill](https://github.com/Alpha-Park/genpark-markov-chain-monte-carlo-metropolis-hastings-skill) | Metropolis-Hastings Markov Chain Monte Carlo (MCMC) sampler with Gaussian proposals and diagnostic statistics | Service | [x] | Standard library |


### Phase 282: Geographic Information Systems (GIS), Geodesy & Spatial Indexing
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-geodesy-haversine-vincenty-distance-skill](https://github.com/Alpha-Park/genpark-geodesy-haversine-vincenty-distance-skill) | Geodesic ellipsoidal and spherical distance calculations via Haversine formula and Vincenty inverse solution on WGS-84 | Service | [x] | Standard library |
| [genpark-r-tree-spatial-indexing-bounding-box-skill](https://github.com/Alpha-Park/genpark-r-tree-spatial-indexing-bounding-box-skill) | 2D R-Tree spatial indexing with Minimum Bounding Boxes (MBR) and spatial range intersection queries | Service | [x] | Standard library |
| [genpark-geohash-spatial-encoding-decoding-skill](https://github.com/Alpha-Park/genpark-geohash-spatial-encoding-decoding-skill) | Geohash base32 hierarchical spatial grid encoding, decoding, and bounding box interval calculations | Service | [x] | Standard library |
| [genpark-ray-casting-polygon-point-in-polygon-skill](https://github.com/Alpha-Park/genpark-ray-casting-polygon-point-in-polygon-skill) | Jordan curve ray-casting point-in-polygon (PIP) test with polygon area and centroid Shoelace calculation | Service | [x] | Standard library |
| [genpark-utm-mgrs-coordinate-projection-skill](https://github.com/Alpha-Park/genpark-utm-mgrs-coordinate-projection-skill) | Universal Transverse Mercator (UTM) forward ellipsoidal map projection with central meridian convergence | Service | [x] | Standard library |


### Phase 283: Digital Signal Processing (DSP), Wavelets & Spectral Transforms
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-fast-fourier-transform-radix2-dit-skill](https://github.com/Alpha-Park/genpark-fast-fourier-transform-radix2-dit-skill) | Radix-2 Decimation-in-Time (DIT) Fast Fourier Transform (FFT) and Inverse FFT with twiddle factor tables | Service | [x] | Standard library |
| [genpark-discrete-wavelet-transform-haar-daubechies-skill](https://github.com/Alpha-Park/genpark-discrete-wavelet-transform-haar-daubechies-skill) | 1D Multi-level Discrete Wavelet Transform (DWT) and Inverse DWT using Haar orthogonal filter banks | Service | [x] | Standard library |
| [genpark-discrete-cosine-transform-dct2-jpeg-skill](https://github.com/Alpha-Park/genpark-discrete-cosine-transform-dct2-jpeg-skill) | Type-II Discrete Cosine Transform (DCT-II) and Inverse DCT (IDCT-III) with orthonormal scaling for spectral analysis | Service | [x] | Standard library |
| [genpark-iir-filter-butterworth-bilinear-transform-skill](https://github.com/Alpha-Park/genpark-iir-filter-butterworth-bilinear-transform-skill) | 2nd-Order Butterworth Infinite Impulse Response (IIR) digital biquad filter via bilinear z-transform | Service | [x] | Standard library |
| [genpark-fir-filter-windowed-sinc-design-skill](https://github.com/Alpha-Park/genpark-fir-filter-windowed-sinc-design-skill) | Finite Impulse Response (FIR) low-pass filter design using truncated sinc and Hamming/Blackman windowing | Service | [x] | Standard library |


### Phase 284: Computational Geometry, Voronoi & Spatial Triangulation
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-convex-hull-andrew-monotone-chain-skill](https://github.com/Alpha-Park/genpark-convex-hull-andrew-monotone-chain-skill) | Andrew's Monotone Chain 2D convex hull algorithm with cross-product orientation test and polygon geometry | Service | [x] | Standard library |
| [genpark-delaunay-triangulation-bowyer-watson-skill](https://github.com/Alpha-Park/genpark-delaunay-triangulation-bowyer-watson-skill) | Bowyer-Watson incremental 2D Delaunay triangulation with circumcircle tests and cavity retriangulation | Service | [x] | Standard library |
| [genpark-voronoi-diagram-delaunay-dual-skill](https://github.com/Alpha-Park/genpark-voronoi-diagram-delaunay-dual-skill) | Voronoi diagram generator via dual graph extraction of Delaunay triangulation with circumcenter vertices | Service | [x] | Standard library |
| [genpark-kd-tree-nearest-neighbor-spatial-search-skill](https://github.com/Alpha-Park/genpark-kd-tree-nearest-neighbor-spatial-search-skill) | k-Dimensional Tree (KD-Tree) spatial index with median partitioning and k-NN branch-and-bound queries | Service | [x] | Standard library |
| [genpark-half-edge-mesh-dcel-topology-skill](https://github.com/Alpha-Park/genpark-half-edge-mesh-dcel-topology-skill) | Doubly Connected Edge List (DCEL) Half-Edge mesh topology with vertex incident cycles and Euler characteristic | Service | [x] | Standard library |


### Phase 285: Computational Physics, Navier-Stokes & Multibody Simulation
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-navier-stokes-2d-fluid-solver-skill](https://github.com/Alpha-Park/genpark-navier-stokes-2d-fluid-solver-skill) | Incompressible 2D Navier-Stokes fluid dynamics grid solver with pressure Poisson Chorin projection | Service | [x] | Standard library |
| [genpark-lattice-boltzmann-d2q9-fluid-flow-skill](https://github.com/Alpha-Park/genpark-lattice-boltzmann-d2q9-fluid-flow-skill) | D2Q9 Lattice Boltzmann Method (LBM) fluid solver with BGK collision and obstacle boundary conditions | Service | [x] | Standard library |
| [genpark-barnes-hut-nbody-gravity-simulation-skill](https://github.com/Alpha-Park/genpark-barnes-hut-nbody-gravity-simulation-skill) | Barnes-Hut hierarchical quadtree N-body gravitational simulation with multipole acceptance criteria | Service | [x] | Standard library |
| [genpark-verlet-cloth-spring-mass-simulation-skill](https://github.com/Alpha-Park/genpark-verlet-cloth-spring-mass-simulation-skill) | Verlet integration cloth and spring-mass dynamics simulation with iterative distance constraint relaxation | Service | [x] | Standard library |
| [genpark-rigid-body-2d-impulse-collision-resolver-skill](https://github.com/Alpha-Park/genpark-rigid-body-2d-impulse-collision-resolver-skill) | 2D Rigid body dynamics engine with Separating Axis Theorem (SAT) collision detection and contact impulse resolution | Service | [x] | Standard library |


### Phase 286: Error-Correcting Codes, Channel Coding & Viterbi Decoding
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-reed-solomon-error-correcting-code-skill](https://github.com/Alpha-Park/genpark-reed-solomon-error-correcting-code-skill) | Galois Field GF(2^8) Reed-Solomon systematic error-correcting encoder and syndrome evaluation | Service | [x] | Standard library |
| [genpark-hamming-secded-error-correction-code-skill](https://github.com/Alpha-Park/genpark-hamming-secded-error-correction-code-skill) | Hamming (7, 4) linear block code and extended (8, 4) SECDED single-error correction double-error detection | Service | [x] | Standard library |
| [genpark-viterbi-convolutional-decoder-skill](https://github.com/Alpha-Park/genpark-viterbi-convolutional-decoder-skill) | Rate 1/2 constraint-length 3 convolutional encoder and Viterbi trellis maximum-likelihood path decoder | Service | [x] | Standard library |
| [genpark-ldpc-tanner-graph-belief-propagation-skill](https://github.com/Alpha-Park/genpark-ldpc-tanner-graph-belief-propagation-skill) | Low-Density Parity-Check (LDPC) Tanner graph belief propagation decoder with sum-product LLR message passing | Service | [x] | Standard library |
| [genpark-shannon-entropy-channel-capacity-awgn-skill](https://github.com/Alpha-Park/genpark-shannon-entropy-channel-capacity-awgn-skill) | Shannon-Hartley AWGN channel capacity theorem, mutual information, and binary symmetric channel limits | Service | [x] | Standard library |


### Phase 287: Asynchronous Runtimes, Actor Systems & Lock-Free Concurrency
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-async-event-loop-reactor-scheduler-skill](https://github.com/Alpha-Park/genpark-async-event-loop-reactor-scheduler-skill) | Cooperative asynchronous event loop with microtask queues, timer heaps, Future/Task resolution, and task cancellation | Service | [x] | Standard library |
| [genpark-actor-model-supervision-tree-skill](https://github.com/Alpha-Park/genpark-actor-model-supervision-tree-skill) | Erlang/OTP-style GenServer Actor model with isolated mailboxes, synchronous call, and one-for-one supervisor restart | Service | [x] | Standard library |
| [genpark-csp-channel-multiplexing-pipeline-skill](https://github.com/Alpha-Park/genpark-csp-channel-multiplexing-pipeline-skill) | Communicating Sequential Processes (CSP) Go-style channel pipeline with nonblocking select multiplexing | Service | [x] | Standard library |
| [genpark-disruptor-lock-free-ring-buffer-skill](https://github.com/Alpha-Park/genpark-disruptor-lock-free-ring-buffer-skill) | LMAX Disruptor-inspired lock-free high-throughput ring buffer with sequence barriers and multi-consumer gating | Service | [x] | Standard library |
| [genpark-work-stealing-thread-pool-deque-skill](https://github.com/Alpha-Park/genpark-work-stealing-thread-pool-deque-skill) | Chase-Lev work-stealing deque scheduler for parallel task decomposition with local LIFO and remote FIFO stealing | Service | [x] | Standard library |


### Phase 288: Time Series Forecasting, Decomposition & Anomaly Detection
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-holt-winters-exponential-smoothing-skill](https://github.com/Alpha-Park/genpark-holt-winters-exponential-smoothing-skill) | Triple exponential smoothing Holt-Winters additive level, trend, and seasonal forecasting model | Service | [x] | Standard library |
| [genpark-arima-autoregressive-integrated-predictor-skill](https://github.com/Alpha-Park/genpark-arima-autoregressive-integrated-predictor-skill) | ARIMA(1, d, 0) autoregressive integrated time series predictor with sample autocorrelation estimation | Service | [x] | Standard library |
| [genpark-dynamic-time-warping-dtw-alignment-skill](https://github.com/Alpha-Park/genpark-dynamic-time-warping-dtw-alignment-skill) | Dynamic Time Warping (DTW) non-linear temporal sequence alignment with Sakoe-Chiba window constraint | Service | [x] | Standard library |
| [genpark-seasonal-trend-decomposition-stl-skill](https://github.com/Alpha-Park/genpark-seasonal-trend-decomposition-stl-skill) | Classical additive time-series decomposition separating trend, seasonal pattern, and residuals | Service | [x] | Standard library |
| [genpark-matrix-profile-discord-anomaly-detector-skill](https://github.com/Alpha-Park/genpark-matrix-profile-discord-anomaly-detector-skill) | Matrix Profile 1D subsequence distance profile and top discord anomaly detection | Service | [x] | Standard library |


### Phase 289: Graph Representation Learning, Community Detection & Network Science
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-louvain-modularity-community-detection-skill](https://github.com/Alpha-Park/genpark-louvain-modularity-community-detection-skill) | Louvain method for greedy modularity maximization community detection on weighted graphs | Service | [x] | Standard library |
| [genpark-node2vec-biased-random-walk-embedding-skill](https://github.com/Alpha-Park/genpark-node2vec-biased-random-walk-embedding-skill) | Node2Vec 2nd-order biased random walk generator with return (p) and in-out (q) hyperparameters | Service | [x] | Standard library |
| [genpark-graph-convolutional-network-gcn-layer-skill](https://github.com/Alpha-Park/genpark-graph-convolutional-network-gcn-layer-skill) | Spectral Graph Convolutional Network (GCN) layer with self-loop renormalization and forward propagation | Service | [x] | Standard library |
| [genpark-weisfeiler-lehman-graph-isomorphism-skill](https://github.com/Alpha-Park/genpark-weisfeiler-lehman-graph-isomorphism-skill) | 1-dimensional Weisfeiler-Lehman (WL) graph coloring kernel for graph isomorphism testing | Service | [x] | Standard library |
| [genpark-label-propagation-semi-supervised-graph-skill](https://github.com/Alpha-Park/genpark-label-propagation-semi-supervised-graph-skill) | Semi-supervised Label Propagation Algorithm (LPA) for graph node classification and community clustering | Service | [x] | Standard library |


### Phase 290: Deep Reinforcement Learning, Policy Gradients & Actor-Critic
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-reinforce-policy-gradient-baseline-skill](https://github.com/Alpha-Park/genpark-reinforce-policy-gradient-baseline-skill) | REINFORCE Monte Carlo policy gradient algorithm with running baseline advantage subtraction | Service | [x] | Standard library |
| [genpark-ppo-clipped-surrogate-objective-skill](https://github.com/Alpha-Park/genpark-ppo-clipped-surrogate-objective-skill) | Proximal Policy Optimization (PPO) clipped surrogate objective evaluator and policy ratio limiter | Service | [x] | Standard library |
| [genpark-dqn-replay-buffer-target-network-skill](https://github.com/Alpha-Park/genpark-dqn-replay-buffer-target-network-skill) | Deep Q-Network experience replay buffer and Polyak target network averaging engine | Service | [x] | Standard library |
| [genpark-gae-generalized-advantage-estimation-skill](https://github.com/Alpha-Park/genpark-gae-generalized-advantage-estimation-skill) | Generalized Advantage Estimation (GAE-Lambda) exponentially weighted temporal difference calculator | Service | [x] | Standard library |
| [genpark-sac-maximum-entropy-rl-evaluator-skill](https://github.com/Alpha-Park/genpark-sac-maximum-entropy-rl-evaluator-skill) | Soft Actor-Critic (SAC) maximum entropy policy value and soft Bellman target evaluator | Service | [x] | Standard library |


### Phase 291: Distributed Storage, Percolator Transactions & Consistent Hashing
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-percolator-distributed-transaction-protocol-skill](https://github.com/Alpha-Park/genpark-percolator-distributed-transaction-protocol-skill) | Percolator snapshot-isolated distributed transaction protocol with primary-lock two-phase commit | Service | [x] | Standard library |
| [genpark-consistent-hashing-vnodes-replication-skill](https://github.com/Alpha-Park/genpark-consistent-hashing-vnodes-replication-skill) | Consistent hashing ring with virtual nodes (vnodes) and configurable replica distribution | Service | [x] | Standard library |
| [genpark-two-phase-commit-2pc-coordinator-skill](https://github.com/Alpha-Park/genpark-two-phase-commit-2pc-coordinator-skill) | Two-Phase Commit (2PC) distributed atomic transaction coordinator with failure rollback | Service | [x] | Standard library |
| [genpark-mvcc-snapshot-isolation-engine-skill](https://github.com/Alpha-Park/genpark-mvcc-snapshot-isolation-engine-skill) | Multi-Version Concurrency Control (MVCC) snapshot isolation engine with epoch vacuuming | Service | [x] | Standard library |
| [genpark-counting-bloom-filter-safe-deletion-skill](https://github.com/Alpha-Park/genpark-counting-bloom-filter-safe-deletion-skill) | Counting Bloom Filter supporting item insertion, safe deletion, and membership testing without false negatives | Service | [x] | Standard library |


### Phase 292: Autonomous Agents, Tool Calling, Planning & Reflection
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-react-agent-reasoning-interleaved-tool-engine-skill](https://github.com/Alpha-Park/genpark-react-agent-reasoning-interleaved-tool-engine-skill) | ReAct (Reasoning + Acting) execution engine with step-by-step observation injection and scratchpad history tracking | Service | [x] | Standard library |
| [genpark-plan-and-solve-hierarchical-decomposer-skill](https://github.com/Alpha-Park/genpark-plan-and-solve-hierarchical-decomposer-skill) | Plan-and-Solve agent framework decomposing complex multi-step queries into a directed dependency plan | Service | [x] | Standard library |
| [genpark-self-refine-iterative-critique-optimization-skill](https://github.com/Alpha-Park/genpark-self-refine-iterative-critique-optimization-skill) | Self-Refine iterative critique-and-refinement loop evaluating constraint adherence and applying structured revisions | Service | [x] | Standard library |
| [genpark-reflexion-episodic-memory-evaluator-skill](https://github.com/Alpha-Park/genpark-reflexion-episodic-memory-evaluator-skill) | Reflexion architecture maintaining episodic failure memories and verbal reinforcement learning signals | Service | [x] | Standard library |
| [genpark-tree-of-thoughts-beam-search-reasoner-skill](https://github.com/Alpha-Park/genpark-tree-of-thoughts-beam-search-reasoner-skill) | Tree of Thoughts (ToT) reasoning engine exploring multi-branch decision states via breadth-first beam search | Service | [x] | Standard library |


### Phase 293: Symbolic Execution, Program Synthesis & Static Analysis
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-symbolic-execution-path-explorer-skill](https://github.com/Alpha-Park/genpark-symbolic-execution-path-explorer-skill) | Forward symbolic execution engine with path condition tracking, branch bifurcation, and state exploration | Service | [x] | Standard library |
| [genpark-abstract-interpretation-interval-domain-skill](https://github.com/Alpha-Park/genpark-abstract-interpretation-interval-domain-skill) | Static program analysis abstract interpretation engine over the interval domain with widening | Service | [x] | Standard library |
| [genpark-cegis-counterexample-program-synthesizer-skill](https://github.com/Alpha-Park/genpark-cegis-counterexample-program-synthesizer-skill) | Counterexample-Guided Inductive Synthesis (CEGIS) loop generating code expressions matching specifications | Service | [x] | Standard library |
| [genpark-hoare-logic-axiomatic-verifier-skill](https://github.com/Alpha-Park/genpark-hoare-logic-axiomatic-verifier-skill) | Axiomatic Hoare logic verification condition generator (VCG) for imperative programs with loop invariants | Service | [x] | Standard library |
| [genpark-hindley-milner-type-inference-skill](https://github.com/Alpha-Park/genpark-hindley-milner-type-inference-skill) | Hindley-Milner Algorithm W polymorphic type inference engine with unification and constraint solving | Service | [x] | Standard library |


### Phase 294: Memory Management, Allocators & Garbage Collection
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-slab-allocator-kernel-memory-cache-skill](https://github.com/Alpha-Park/genpark-slab-allocator-kernel-memory-cache-skill) | Kernel-style Slab memory allocator with fixed-size cache pools, freelists, and slab expansion | Service | [x] | Standard library |
| [genpark-buddy-memory-allocator-binary-tree-skill](https://github.com/Alpha-Park/genpark-buddy-memory-allocator-binary-tree-skill) | Binary buddy system memory allocator managing power-of-two blocks, coalescing, and split operations | Service | [x] | Standard library |
| [genpark-mark-sweep-tri-color-gc-skill](https://github.com/Alpha-Park/genpark-mark-sweep-tri-color-gc-skill) | Tri-color abstraction mark-and-sweep garbage collection engine with worklist traversal | Service | [x] | Standard library |
| [genpark-refcount-cycle-detection-bacon-rajan-skill](https://github.com/Alpha-Park/genpark-refcount-cycle-detection-bacon-rajan-skill) | Reference counting engine with Bacon-Rajan trial deletion cycle collection | Service | [x] | Standard library |
| [genpark-generational-garbage-collector-card-table-skill](https://github.com/Alpha-Park/genpark-generational-garbage-collector-card-table-skill) | Generational GC with nursery and mature generations using write-barrier card table tracking | Service | [x] | Standard library |


### Phase 295: Distributed Consensus, Paxos & Byzantine Fault Tolerance
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-multi-paxos-log-replication-engine-skill](https://github.com/Alpha-Park/genpark-multi-paxos-log-replication-engine-skill) | Multi-Paxos log replication consensus engine with leader lease optimization and slot agreement | Service | [x] | Standard library |
| [genpark-pbft-practical-byzantine-fault-tolerance-skill](https://github.com/Alpha-Park/genpark-pbft-practical-byzantine-fault-tolerance-skill) | Practical Byzantine Fault Tolerance (PBFT) state machine replication engine with 3-phase view consensus | Service | [x] | Standard library |
| [genpark-raft-joint-consensus-membership-reconfiguration-skill](https://github.com/Alpha-Park/genpark-raft-joint-consensus-membership-reconfiguration-skill) | Raft joint consensus dynamic membership transition protocol avoiding split-brain configurations | Service | [x] | Standard library |
| [genpark-raft-snapshot-compaction-install-skill](https://github.com/Alpha-Park/genpark-raft-snapshot-compaction-install-skill) | Raft state machine log compaction and incremental chunked InstallSnapshot synchronization | Service | [x] | Standard library |
| [genpark-vector-clock-causal-order-tracker-skill](https://github.com/Alpha-Park/genpark-vector-clock-causal-order-tracker-skill) | Distributed vector clocks tracking causal concurrency, happens-before relations, and concurrent events | Service | [x] | Standard library |


### Phase 296: Advanced Graph Algorithms & Network Flows
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-dinics-max-flow-network-algorithm-skill](https://github.com/Alpha-Park/genpark-dinics-max-flow-network-algorithm-skill) | Dinic's blocking flow algorithm with level graphs and dead-end pruning for maximum network flow | Service | [x] | Standard library |
| [genpark-push-relabel-fifo-max-flow-skill](https://github.com/Alpha-Park/genpark-push-relabel-fifo-max-flow-skill) | Goldberg-Tarjan Push-Relabel maximum flow algorithm with FIFO vertex discharge and height relabeling | Service | [x] | Standard library |
| [genpark-min-cost-max-flow-successive-shortest-path-skill](https://github.com/Alpha-Park/genpark-min-cost-max-flow-successive-shortest-path-skill) | Minimum-Cost Maximum-Flow (MCMF) engine using successive shortest path with SPFA residual tracking | Service | [x] | Standard library |
| [genpark-edmonds-karp-bfs-max-flow-skill](https://github.com/Alpha-Park/genpark-edmonds-karp-bfs-max-flow-skill) | Edmonds-Karp BFS shortest augmenting path algorithm with residual capacity updates | Service | [x] | Standard library |
| [genpark-tarjan-dominator-tree-cfg-skill](https://github.com/Alpha-Park/genpark-tarjan-dominator-tree-cfg-skill) | Dominator tree construction and immediate dominator calculation over directed control-flow graphs | Service | [x] | Standard library |


### Phase 297: Distributed Cryptography & Verifiable Commitments
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-shamir-secret-sharing-polynomial-recovery-skill](https://github.com/Alpha-Park/genpark-shamir-secret-sharing-polynomial-recovery-skill) | Shamir's (k, n) threshold secret sharing scheme with Lagrange polynomial interpolation over prime fields | Service | [x] | Standard library |
| [genpark-pedersen-commitment-homomorphic-hiding-skill](https://github.com/Alpha-Park/genpark-pedersen-commitment-homomorphic-hiding-skill) | Additively homomorphic Pedersen commitment scheme ensuring perfect hiding and computational binding | Service | [x] | Standard library |
| [genpark-merkle-mountain-range-mmr-accumulator-skill](https://github.com/Alpha-Park/genpark-merkle-mountain-range-mmr-accumulator-skill) | Append-only Merkle Mountain Range (MMR) peak accumulator with logarithmic inclusion proofs | Service | [x] | Standard library |
| [genpark-verifiable-random-function-vrf-hash-skill](https://github.com/Alpha-Park/genpark-verifiable-random-function-vrf-hash-skill) | Verifiable Random Function (VRF) generating deterministic pseudorandom output with verifiable non-interactive proof | Service | [x] | Standard library |
| [genpark-feldman-verifiable-secret-sharing-vss-skill](https://github.com/Alpha-Park/genpark-feldman-verifiable-secret-sharing-vss-skill) | Feldman's Verifiable Secret Sharing (VSS) broadcasting public commitments to verify share consistency | Service | [x] | Standard library |


### Phase 298: Computational Geometry & Collision Detection
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-gjk-convex-collision-detection-skill](https://github.com/Alpha-Park/genpark-gjk-convex-collision-detection-skill) | Gilbert-Johnson-Keerthi (GJK) convex polytope collision detector using Minkowski difference support mappings | Service | [x] | Standard library |
| [genpark-epa-penetration-depth-vector-skill](https://github.com/Alpha-Park/genpark-epa-penetration-depth-vector-skill) | Expanding Polytope Algorithm (EPA) calculating contact normal and minimum penetration depth vectors | Service | [x] | Standard library |
| [genpark-sweep-and-prune-broadphase-collision-skill](https://github.com/Alpha-Park/genpark-sweep-and-prune-broadphase-collision-skill) | Sweep-and-Prune broadphase collision algorithm sorting axis-aligned bounding boxes (AABBs) | Service | [x] | Standard library |
| [genpark-quadtree-spatial-partitioning-engine-skill](https://github.com/Alpha-Park/genpark-quadtree-spatial-partitioning-engine-skill) | Recursive 2D Quadtree spatial decomposition partitioning points into quadrants with range queries | Service | [x] | Standard library |
| [genpark-bvh-bounding-volume-hierarchy-ray-tracer-skill](https://github.com/Alpha-Park/genpark-bvh-bounding-volume-hierarchy-ray-tracer-skill) | Bounding Volume Hierarchy (BVH) ray-box intersection engine using slab method for fast ray tracing | Service | [x] | Standard library |


### Phase 299: Zero-Knowledge Proofs & Algebraic Circuits
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-qap-quadratic-arithmetic-program-groth16-skill](https://github.com/Alpha-Park/genpark-qap-quadratic-arithmetic-program-groth16-skill) | Quadratic Arithmetic Program (QAP) reduction transforming R1CS constraints into polynomial divisibility statements | Service | [x] | Standard library |
| [genpark-plonk-permutation-argument-grand-product-skill](https://github.com/Alpha-Park/genpark-plonk-permutation-argument-grand-product-skill) | Plonk grand product copy-constraint permutation argument tracking wire routing equality | Service | [x] | Standard library |
| [genpark-kzg-polynomial-commitment-trusted-setup-skill](https://github.com/Alpha-Park/genpark-kzg-polynomial-commitment-trusted-setup-skill) | Kate-Zaverucha-Goldberg (KZG) polynomial commitment evaluator with evaluation proofs | Service | [x] | Standard library |
| [genpark-poseidon-algebraic-hash-zk-friendly-skill](https://github.com/Alpha-Park/genpark-poseidon-algebraic-hash-zk-friendly-skill) | Poseidon algebraic hash function for STARK/SNARK circuits with S-box power permutations and MDS matrices | Service | [x] | Standard library |
| [genpark-fiat-shamir-heuristic-interactive-to-nizk-skill](https://github.com/Alpha-Park/genpark-fiat-shamir-heuristic-interactive-to-nizk-skill) | Fiat-Shamir heuristic transformation converting interactive proof transcripts into non-interactive zero-knowledge arguments | Service | [x] | Standard library |


### Phase 300: TRICENTENNIAL MILESTONE - Quantum Computing, Circuits & Information
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-quantum-statevector-circuit-simulator-skill](https://github.com/Alpha-Park/genpark-quantum-statevector-circuit-simulator-skill) | Full n-qubit complex statevector simulator supporting Hadamard, CNOT, Phase, and Pauli gates with unitary evolution | Service | [x] | Standard library |
| [genpark-quantum-fourier-transform-qft-circuit-skill](https://github.com/Alpha-Park/genpark-quantum-fourier-transform-qft-circuit-skill) | Exact Quantum Fourier Transform (QFT) circuit generator and inverse QFT over n-qubit registers | Service | [x] | Standard library |
| [genpark-grovers-search-amplitude-amplification-skill](https://github.com/Alpha-Park/genpark-grovers-search-amplitude-amplification-skill) | Grover's quantum search algorithm with phase inversion oracle and diffusion reflection operator | Service | [x] | Standard library |
| [genpark-quantum-teleportation-entanglement-protocol-skill](https://github.com/Alpha-Park/genpark-quantum-teleportation-entanglement-protocol-skill) | 3-qubit quantum teleportation protocol utilizing Bell state entanglement and classical feedforward correction | Service | [x] | Standard library |
| [genpark-pauli-algebra-stabilizer-measurement-skill](https://github.com/Alpha-Park/genpark-pauli-algebra-stabilizer-measurement-skill) | Pauli group algebra matrices with tensor products, commutation relations, and stabilizer projection | Service | [x] | Standard library |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Submit a public repository with a clear purpose,
installation instructions, license, and meaningful examples or tests. State limitations and dependencies.
MCP integrations must expose initialize, tools/list schemas, and callable tools; a filename alone is insufficient.

## Distribution channels

- [Official MCP Registry](https://registry.modelcontextprotocol.io/) lists published MCP servers.
- [Smithery publishing](https://smithery.ai/docs/build/publish) supports remote servers and local MCPB bundles.
- [PulseMCP](https://www.pulsemcp.com/servers) reported new submissions paused on 2026-09-28.

These links are discovery channels, not endorsements or proof of listing.
GitHub Trending placement, traffic, and stars depend on community interest and are not guaranteed.

MIT license. Individual repositories retain their own licenses.



### 💳 8. Autonomous FinTech, Webhooks & Double-Entry Ledger (Phase 250)
Cryptographic payment webhook verification, mathematical double-entry general ledger, smart dunning churn prevention, automated treasury sweep, and high-velocity card-testing fraud defense.

| Skill Name | Description | Python Client |
|:---|:---|:---|
| [`genpark-fintech-webhook-idempotent-replay-guard-skill`](https://github.com/Alpha-Park/genpark-fintech-webhook-idempotent-replay-guard-skill) | Cryptographic payment webhook ingestion guard enforcing HMAC-SHA256 signatures, sliding replay tolerance, and atomic idempotency locking. | `FintechWebhookIdempotentGuard` |
| [`genpark-immutable-double-entry-ledger-kernel-skill`](https://github.com/Alpha-Park/genpark-immutable-double-entry-ledger-kernel-skill) | Mathematical double-entry general ledger kernel enforcing Debits == Credits invariant and hash-chained audit blocks. | `ImmutableDoubleEntryLedger` |
| [`genpark-smart-dunning-churn-prevention-strategist-skill`](https://github.com/Alpha-Park/genpark-smart-dunning-churn-prevention-strategist-skill) | Autonomous SaaS billing recovery engine optimizing retry cadences for soft vs hard payment declines. | `SmartDunningChurnStrategist` |
| [`genpark-automated-treasury-cash-sweep-optimizer-skill`](https://github.com/Alpha-Park/genpark-automated-treasury-cash-sweep-optimizer-skill) | Multi-account treasury liquidity manager calculating target operating buffers and yield sweep operations. | `AutomatedTreasuryCashSweepOptimizer` |
| [`genpark-fintech-transaction-velocity-fraud-sentinel-skill`](https://github.com/Alpha-Park/genpark-fintech-transaction-velocity-fraud-sentinel-skill) | Real-time sliding window fraud and card-testing velocity sentinel scoring transactional risk anomalies. | `FintechTransactionVelocityFraudSentinel` |

---



### 🧠 9. Agentic Memory, Vector Search & Graph RAG (Phase 251)
Hierarchical episodic memory with recency decay, zero-dependency BM25 & Cosine Reciprocal Rank Fusion, knowledge graph triplet extraction, high-throughput semantic query cache, and lost-in-the-middle context reordering.

| Skill Name | Description | Python Client |
|:---|:---|:---|
| [`genpark-agent-hierarchical-episodic-memory-skill`](https://github.com/Alpha-Park/genpark-agent-hierarchical-episodic-memory-skill) | Cognitive multi-tier memory kernel managing working scratchpad, sliding dialogue buffer, and episodic memories with exponential recency decay. | `AgentHierarchicalEpisodicMemory` |
| [`genpark-cosine-bm25-reciprocal-rank-fusion-skill`](https://github.com/Alpha-Park/genpark-cosine-bm25-reciprocal-rank-fusion-skill) | Zero-dependency hybrid retrieval engine fusing sparse lexical BM25 Okapi and dense Cosine vector similarities via Reciprocal Rank Fusion. | `CosineBM25ReciprocalRankFusion` |
| [`genpark-knowledge-graph-entity-relation-triplet-extractor-skill`](https://github.com/Alpha-Park/genpark-knowledge-graph-entity-relation-triplet-extractor-skill) | Entity-relation-object triplet extractor and multi-hop path reasoning kernel with Cypher and JSON-LD graph generation. | `KnowledgeGraphTripletExtractor` |
| [`genpark-agent-semantic-cache-similarity-deduplicator-skill`](https://github.com/Alpha-Park/genpark-agent-semantic-cache-similarity-deduplicator-skill) | High-throughput semantic query cache and approximate deduplicator combining exact SHA-256 and cosine similarity threshold matching with LRU eviction. | `AgentSemanticCacheDeduplicator` |
| [`genpark-context-window-lost-in-middle-reorderer-skill`](https://github.com/Alpha-Park/genpark-context-window-lost-in-middle-reorderer-skill) | Context window attention optimizer reordering retrieved documents to place critical evidence at prompt boundaries, mitigating lost-in-the-middle degradation. | `ContextWindowLostInMiddleReorderer` |

---



### 🛡️ 10. Autonomous Agent Safety, Sandbox & Execution Guardrails (Phase 252)
Bash command AST sandbox guard, multi-vector prompt injection & jailbreak sentinel, real-time token spend circuit breaker, differential privacy noise injector, and deadlock infinite loop detector.

| Skill Name | Description | Python Client |
|:---|:---|:---|
| [`genpark-agent-bash-command-sandbox-guard-skill`](https://github.com/Alpha-Park/genpark-agent-bash-command-sandbox-guard-skill) | Zero-dependency AST & heuristic bash command sandbox guard blocking destructive system mutations, path traversals, and reverse shells. | `AgentBashCommandSandboxGuard` |
| [`genpark-agent-prompt-injection-jailbreak-sentinel-skill`](https://github.com/Alpha-Park/genpark-agent-prompt-injection-jailbreak-sentinel-skill) | Multi-vector heuristic prompt injection and jailbreak detector analyzing system overrides, delimiter breakouts, and base64 payload evasion. | `AgentPromptInjectionJailbreakSentinel` |
| [`genpark-agent-budget-token-spend-circuit-breaker-skill`](https://github.com/Alpha-Park/genpark-agent-budget-token-spend-circuit-breaker-skill) | Autonomous financial circuit breaker tracking real-time token burn and cost velocity with automated throttling and emergency freeze. | `AgentBudgetTokenSpendCircuitBreaker` |
| [`genpark-agent-synthetic-data-differential-privacy-guard-skill`](https://github.com/Alpha-Park/genpark-agent-synthetic-data-differential-privacy-guard-skill) | Differential privacy epsilon-noise generator and quasi-identifier redaction kernel protecting tabular data releases from re-identification. | `AgentSyntheticDataDifferentialPrivacyGuard` |
| [`genpark-agent-deadlock-liveloss-loop-detector-skill`](https://github.com/Alpha-Park/genpark-agent-deadlock-liveloss-loop-detector-skill) | Trajectory state entropy and cyclic repetition detector identifying autonomous agent infinite tool loops and planning deadlocks. | `AgentDeadlockLivelossLoopDetector` |

---



### 🌐 11. Autonomous Web Browsing & DOM Semantic Extraction (Phase 253)
DOM semantic tree pruner with 80%+ token reduction, form input schema auto-mapper, synthetic execution trajectory evaluator, anti-crawler trap URL canonicalizer, and type-inferred Markdown-to-JSON transformer.

| Skill Name | Description | Python Client |
|:---|:---|:---|
| [`genpark-html-dom-semantic-tree-pruner-skill`](https://github.com/Alpha-Park/genpark-html-dom-semantic-tree-pruner-skill) | Zero-dependency HTML DOM semantic tree pruner compressing web markup into accessibility-friendly clean trees with 80%+ token reduction. | `HtmlDomSemanticTreePruner` |
| [`genpark-web-form-input-schema-auto-mapper-skill`](https://github.com/Alpha-Park/genpark-web-form-input-schema-auto-mapper-skill) | Autonomous web form inspector and schema auto-mapper matching input attributes, autocomplete hints, and regex validations to agent state. | `WebFormInputSchemaAutoMapper` |
| [`genpark-agent-synthetic-trajectory-evaluator-skill`](https://github.com/Alpha-Park/genpark-agent-synthetic-trajectory-evaluator-skill) | Execution trajectory evaluator computing action-level precision, recall, and Levenshtein sequence edit distance against gold benchmarks. | `AgentSyntheticTrajectoryEvaluator` |
| [`genpark-url-canonicalization-anti-crawler-trap-skill`](https://github.com/Alpha-Park/genpark-url-canonicalization-anti-crawler-trap-skill) | Web URL canonicalization and anti-crawler trap detector identifying circular paths, infinite paginations, and tracking parameter bloat. | `UrlCanonicalizationAntiCrawlerTrap` |
| [`genpark-markdown-table-to-json-transformer-skill`](https://github.com/Alpha-Park/genpark-markdown-table-to-json-transformer-skill) | Zero-dependency Markdown table to structured JSON transformer with automated column type inference and format normalization. | `MarkdownTableToJsonTransformer` |

---



### 📊 12. Data Science, Statistics & Time-Series Anomaly Detection (Phase 254)
Holt linear exponential smoothing trend forecaster, multi-strategy Z-score & Tukey IQR anomaly detector, multivariate gradient descent linear regression, Welch's two-sample t-test evaluator, and Power Iteration SVD/PCA dimensionality reducer.

| Skill Name | Description | Python Client |
|:---|:---|:---|
| [`genpark-time-series-exponential-smoothing-forecaster-skill`](https://github.com/Alpha-Park/genpark-time-series-exponential-smoothing-forecaster-skill) | Zero-dependency Holt linear exponential smoothing engine forecasting numerical trends with multi-step horizon and variance confidence bands. | `TimeSeriesExponentialSmoothingForecaster` |
| [`genpark-statistical-zscore-iqr-anomaly-detector-skill`](https://github.com/Alpha-Park/genpark-statistical-zscore-iqr-anomaly-detector-skill) | Multi-strategy anomaly detector computing standard Z-score, modified median absolute deviation (MAD), and Tukey IQR fences on numerical streams. | `StatisticalZscoreIqrAnomalyDetector` |
| [`genpark-linear-regression-gradient-descent-engine-skill`](https://github.com/Alpha-Park/genpark-linear-regression-gradient-descent-engine-skill) | Multivariate linear regression engine computing MSE loss, analytical gradient descent weights, and R-squared coefficient of determination. | `LinearRegressionGradientDescentEngine` |
| [`genpark-hypothesis-welch-t-test-statistical-evaluator-skill`](https://github.com/Alpha-Park/genpark-hypothesis-welch-t-test-statistical-evaluator-skill) | Two-sample Welch's t-test hypothesis evaluator computing Satterthwaite degrees of freedom and two-tailed p-values for A/B testing. | `HypothesisWelchTTestEvaluator` |
| [`genpark-data-matrix-svd-pca-dimensionality-reducer-skill`](https://github.com/Alpha-Park/genpark-data-matrix-svd-pca-dimensionality-reducer-skill) | Zero-dependency Power Iteration PCA dimensionality reducer projecting high-dimensional feature vectors into principal component representations. | `DataMatrixSvdPcaDimensionalityReducer` |

---
\n
### ⚡ Edge AI, Quantization & On-Device Model Acceleration Agent Skills (Phase 255)
- **[genpark-int8-symmetric-per-tensor-quantizer-skill](https://github.com/alphaparkinc/genpark-int8-symmetric-per-tensor-quantizer-skill)**: Symmetric INT8 per-tensor and per-channel quantization engine for LLM weights and activations, with SNR and MSE reconstruction telemetry.
- **[genpark-kv-cache-paged-attention-allocator-skill](https://github.com/alphaparkinc/genpark-kv-cache-paged-attention-allocator-skill)**: Virtual paged attention KV-cache memory manager with logical block mapping, non-contiguous physical page allocation, and zero-copy fragmentation tracking.
- **[genpark-speculative-decoding-verifier-skill](https://github.com/alphaparkinc/genpark-speculative-decoding-verifier-skill)**: Draft-target model speculative decoding verification engine with rejection sampling, acceptance rate telemetry, and dynamic speedup ratio estimation.
- **[genpark-dynamic-prompt-prefix-cache-skill](https://github.com/alphaparkinc/genpark-dynamic-prompt-prefix-cache-skill)**: Radix trie-based prompt prefix cache optimizer matching longest common prompt token prefixes to eliminate redundant prefill computation and reduce TTFT.
- **[genpark-edge-inference-latency-telemetry-skill](https://github.com/alphaparkinc/genpark-edge-inference-latency-telemetry-skill)**: High-precision edge and on-device LLM inference profiler calculating TTFT, TPOT, tokens/second throughput, and percentile jitter distributions (P50/P90/P99).
\n
### 🌐 Distributed Multi-Agent Consensus, Swarm Coordination & CRDT Synchronization Agent Skills (Phase 256)
- **[genpark-crdt-lww-element-set-sync-skill](https://github.com/alphaparkinc/genpark-crdt-lww-element-set-sync-skill)**: Conflict-free Replicated Data Type (CRDT) Last-Write-Wins element set with Lamport timestamps and deterministic two-way state merge.
- **[genpark-raft-leader-election-consensus-kernel-skill](https://github.com/alphaparkinc/genpark-raft-leader-election-consensus-kernel-skill)**: Raft consensus state machine managing election timers, randomized backoff, candidate vote counting, and leader quorum transition.
- **[genpark-vector-clock-causal-ordering-skill](https://github.com/alphaparkinc/genpark-vector-clock-causal-ordering-skill)**: Vector clock implementation for tracking causal event ordering, distributed concurrency, and happens-before relations across agent networks.
- **[genpark-multi-agent-token-bucket-gossip-protocol-skill](https://github.com/alphaparkinc/genpark-multi-agent-token-bucket-gossip-protocol-skill)**: Peer-to-peer epidemic gossip protocol engine with token-bucket rate limiting for bounded network dissemination in autonomous agent swarms.
- **[genpark-distributed-two-phase-commit-coordinator-skill](https://github.com/alphaparkinc/genpark-distributed-two-phase-commit-coordinator-skill)**: Distributed Two-Phase Commit (2PC) transaction coordinator with prepare/vote phase, unanimous consensus commit/abort logic, and failure recovery.
\n
### 🔐 Cyber Security, Cryptographic Attestation & Zero-Knowledge Proofs Agent Skills (Phase 257)
- **[genpark-merkle-tree-state-proof-verifier-skill](https://github.com/alphaparkinc/genpark-merkle-tree-state-proof-verifier-skill)**: Cryptographic Merkle tree constructor and inclusion proof generator/verifier with SHA-256 state leaves for immutable agent state attestation.
- **[genpark-jwt-hmac-sha256-token-attestation-skill](https://github.com/alphaparkinc/genpark-jwt-hmac-sha256-token-attestation-skill)**: Cryptographic JSON Web Token (JWT) engine with RFC 7519 HMAC-SHA256 signature verification, claims validation, and expiration enforcement.
- **[genpark-schnorr-zero-knowledge-prover-skill](https://github.com/alphaparkinc/genpark-schnorr-zero-knowledge-prover-skill)**: Interactive Schnorr Zero-Knowledge Identification (ZKP) protocol proving private key knowledge via 3-pass commitment, challenge, and response.
- **[genpark-constant-time-crypto-validator-skill](https://github.com/alphaparkinc/genpark-constant-time-crypto-validator-skill)**: Side-channel timing attack defense primitive providing constant-time bitwise and string digest comparison for agent security credentials.
- **[genpark-nonce-replay-attack-guard-skill](https://github.com/alphaparkinc/genpark-nonce-replay-attack-guard-skill)**: Sliding-window nonce ledger and replay attack detector invalidating duplicated agent API requests and token reflections.
\n
### 📈 Quantitative Finance, Black-Scholes Greeks & Monte Carlo Risk Modeling Agent Skills (Phase 258)
- **[genpark-black-scholes-merton-greeks-engine-skill](https://github.com/alphaparkinc/genpark-black-scholes-merton-greeks-engine-skill)**: Black-Scholes-Merton European option analytical pricing and first/second-order Greeks (Delta, Gamma, Vega, Theta, Rho) engine.
- **[genpark-monte-carlo-geometric-brownian-motion-skill](https://github.com/alphaparkinc/genpark-monte-carlo-geometric-brownian-motion-skill)**: Geometric Brownian Motion (GBM) Monte Carlo stochastic path simulation engine with normal Box-Muller variates and tail percentile bounds.
- **[genpark-value-at-risk-cvar-expected-shortfall-skill](https://github.com/alphaparkinc/genpark-value-at-risk-cvar-expected-shortfall-skill)**: Portfolio Value-at-Risk (VaR) and Conditional VaR (Expected Shortfall) engine calculating tail risk across parametric and historical loss distributions.
- **[genpark-bond-convexity-modified-duration-calculator-skill](https://github.com/alphaparkinc/genpark-bond-convexity-modified-duration-calculator-skill)**: Fixed-income bond pricing engine computing cash flow present values, Macaulay duration, modified duration, and price convexity.
- **[genpark-yield-curve-nelson-siegel-interpolator-skill](https://github.com/alphaparkinc/genpark-yield-curve-nelson-siegel-interpolator-skill)**: Nelson-Siegel parametric zero-coupon yield curve modeling engine fitting spot rates, decay factor, level, slope, and curvature components.
\n
### 🕸️ Graph Theory, Pathfinding & Network Flow Agent Skills (Phase 259)
- **[genpark-graph-dijkstra-astar-pathfinder-skill](https://github.com/alphaparkinc/genpark-graph-dijkstra-astar-pathfinder-skill)**: Graph pathfinding engine implementing Dijkstra's shortest path and A* heuristic routing with priority queues for agent planning.
- **[genpark-topological-sorter-tarjan-scc-skill](https://github.com/alphaparkinc/genpark-topological-sorter-tarjan-scc-skill)**: Directed acyclic graph (DAG) topological sorting and Tarjan's strongly connected components (SCC) engine for agent dependency resolution.
- **[genpark-maximum-flow-edmonds-karp-network-skill](https://github.com/alphaparkinc/genpark-maximum-flow-edmonds-karp-network-skill)**: Edmonds-Karp network flow engine with BFS augmenting paths computing maximum flow and minimum cut bottlenecks for multi-agent routing.
- **[genpark-minimum-spanning-tree-kruskal-prim-skill](https://github.com/alphaparkinc/genpark-minimum-spanning-tree-kruskal-prim-skill)**: Minimum Spanning Tree (MST) solver using Kruskal's disjoint-set union-find for optimal multi-agent communications backbones.
- **[genpark-page-rank-power-iteration-centrality-skill](https://github.com/alphaparkinc/genpark-page-rank-power-iteration-centrality-skill)**: PageRank random walk and power iteration centrality engine scoring authority and influence across interconnected agent networks.
\n
### ⚛️ Quantum Computing Simulation, Qubit State Vectors & Quantum Gates Agent Skills (Phase 260)
- **[genpark-quantum-qubit-state-vector-simulator-skill](https://github.com/alphaparkinc/genpark-quantum-qubit-state-vector-simulator-skill)**: Multi-qubit complex state vector simulator calculating superposition amplitudes, state fidelity, and probability distributions.
- **[genpark-quantum-gate-hadamard-pauli-cnot-engine-skill](https://github.com/alphaparkinc/genpark-quantum-gate-hadamard-pauli-cnot-engine-skill)**: Quantum unitary gate engine applying single-qubit (Hadamard, Pauli-X/Y/Z) and two-qubit entangling (CNOT) matrix operators.
- **[genpark-quantum-measurement-born-rule-sampler-skill](https://github.com/alphaparkinc/genpark-quantum-measurement-born-rule-sampler-skill)**: Projective quantum measurement engine sampling qubit collapses via Born's rule with Monte Carlo shot histograms.
- **[genpark-quantum-teleportation-entanglement-circuit-skill](https://github.com/alphaparkinc/genpark-quantum-teleportation-entanglement-circuit-skill)**: EPR Bell state generator creating maximally entangled qubit pairs (|Phi+>) for quantum communications and teleportation protocols.
- **[genpark-quantum-grover-search-oracle-amplifier-skill](https://github.com/alphaparkinc/genpark-quantum-grover-search-oracle-amplifier-skill)**: Grover's quantum search amplitude amplification engine demonstrating quadratic speedup for unstructured database queries via phase inversion oracles.


### Phase 261: Multi-Modal Audio Signal DSP, Psychoacoustics & Waveform Synthesis
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-stft-spectrogram-mel-filterbank-skill](https://github.com/Alpha-Park/genpark-stft-spectrogram-mel-filterbank-skill) | STFT Hann windowing & triangular Mel-filterbank energy extraction | Service | [x] | Pure math/cmath |
| [genpark-adsr-envelope-wavetable-synth-skill](https://github.com/Alpha-Park/genpark-adsr-envelope-wavetable-synth-skill) | ADSR envelope generator & wavetable multi-waveform synthesis | Service | [x] | Pure math |
| [genpark-biquad-iir-filter-dsp-skill](https://github.com/Alpha-Park/genpark-biquad-iir-filter-dsp-skill) | 2nd-order Direct Form IIR filter with Bode frequency response | Service | [x] | Pure math/cmath |
| [genpark-dynamic-range-compressor-limiter-skill](https://github.com/Alpha-Park/genpark-dynamic-range-compressor-limiter-skill) | Soft-knee dynamic range compressor & peak ballistics limiter | Service | [x] | Pure math |
| [genpark-voice-pitch-yin-autocorrelation-skill](https://github.com/Alpha-Park/genpark-voice-pitch-yin-autocorrelation-skill) | Fundamental frequency (F0) pitch detector using YIN algorithm | Service | [x] | Pure math |


### Phase 262: Computer Vision, Morphological Image Processing & Edge Detection
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-sobel-canny-edge-detector-skill](https://github.com/Alpha-Park/genpark-sobel-canny-edge-detector-skill) | Sobel 2D convolution & Canny hysteresis edge detection engine | Service | [x] | Pure math |
| [genpark-morphology-dilation-erosion-skill](https://github.com/Alpha-Park/genpark-morphology-dilation-erosion-skill) | Mathematical morphology dilation, erosion, opening & closing | Service | [x] | Standard library |
| [genpark-harris-corner-feature-detector-skill](https://github.com/Alpha-Park/genpark-harris-corner-feature-detector-skill) | Harris corner & interest point autocorrelation detector | Service | [x] | Standard library |
| [genpark-hough-transform-line-circle-skill](https://github.com/Alpha-Park/genpark-hough-transform-line-circle-skill) | Hough Transform parametric space voting accumulator | Service | [x] | Pure math |
| [genpark-image-connected-components-labeling-skill](https://github.com/Alpha-Park/genpark-image-connected-components-labeling-skill) | Two-pass CCL image segmenter with disjoint-set Union-Find | Service | [x] | Standard library |


### Phase 263: Natural Language Tokenization, Byte-Pair Encoding & Text Similarity
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-bpe-tokenizer-byte-pair-encoder-skill](https://github.com/Alpha-Park/genpark-bpe-tokenizer-byte-pair-encoder-skill) | Byte-Pair Encoding (BPE) subword tokenizer trainer and encoder | Service | [x] | Standard library |
| [genpark-tfidf-vectorizer-cosine-similarity-skill](https://github.com/Alpha-Park/genpark-tfidf-vectorizer-cosine-similarity-skill) | TF-IDF smooth vectorizer & pairwise cosine similarity engine | Service | [x] | Pure math/re |
| [genpark-bm25-okapi-document-ranker-skill](https://github.com/Alpha-Park/genpark-bm25-okapi-document-ranker-skill) | Okapi BM25 relevance scorer with document length normalization | Service | [x] | Pure math/re |
| [genpark-levenshtein-damerau-fuzzy-matcher-skill](https://github.com/Alpha-Park/genpark-levenshtein-damerau-fuzzy-matcher-skill) | Damerau-Levenshtein transposition distance & candidate ranker | Service | [x] | Standard library |
| [genpark-minhash-lsh-document-deduplicator-skill](https://github.com/Alpha-Park/genpark-minhash-lsh-document-deduplicator-skill) | MinHash & LSH near-duplicate Jaccard similarity estimator | Service | [x] | Pure re/hash |


### Phase 264: Reinforcement Learning, Multi-Armed Bandits & Value Iteration
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-multi-armed-bandit-ucb1-thompson-skill](https://github.com/Alpha-Park/genpark-multi-armed-bandit-ucb1-thompson-skill) | Multi-armed bandit with UCB1 exploration and Bayesian Thompson sampling | Service | [x] | Pure math/random |
| [genpark-markov-decision-process-value-iteration-skill](https://github.com/Alpha-Park/genpark-markov-decision-process-value-iteration-skill) | Finite MDP solver with Bellman optimality value iteration | Service | [x] | Standard library |
| [genpark-q-learning-temporal-difference-agent-skill](https://github.com/Alpha-Park/genpark-q-learning-temporal-difference-agent-skill) | Tabular Q-learning agent with epsilon-greedy policy & TD updates | Service | [x] | Pure random |
| [genpark-actor-critic-advantage-td-error-skill](https://github.com/Alpha-Park/genpark-actor-critic-advantage-td-error-skill) | Advantage Actor-Critic (A2C) with TD error and softmax policy | Service | [x] | Pure math |
| [genpark-mcts-monte-carlo-tree-search-skill](https://github.com/Alpha-Park/genpark-mcts-monte-carlo-tree-search-skill) | Upper Confidence Bounds for Trees (UCT / MCTS) planning engine | Service | [x] | Pure math |


### Phase 265: Evolutionary Computation, Genetic Algorithms & Swarm Optimization
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-genetic-algorithm-crossover-mutation-skill](https://github.com/Alpha-Park/genpark-genetic-algorithm-crossover-mutation-skill) | Genetic algorithm with tournament selection, crossover & mutation | Service | [x] | Pure random |
| [genpark-particle-swarm-optimization-pso-skill](https://github.com/Alpha-Park/genpark-particle-swarm-optimization-pso-skill) | Continuous Particle Swarm Optimization with cognitive & social velocity | Service | [x] | Pure random |
| [genpark-simulated-annealing-metropolis-skill](https://github.com/Alpha-Park/genpark-simulated-annealing-metropolis-skill) | Thermodynamic Simulated Annealing with Metropolis acceptance criterion | Service | [x] | Pure math/random |
| [genpark-differential-evolution-vector-optimizer-skill](https://github.com/Alpha-Park/genpark-differential-evolution-vector-optimizer-skill) | Differential Evolution (DE/rand/1/bin) continuous vector optimizer | Service | [x] | Pure random |
| [genpark-ant-colony-optimization-tsp-skill](https://github.com/Alpha-Park/genpark-ant-colony-optimization-tsp-skill) | Ant Colony Optimization (ACO) for travelling salesperson problem | Service | [x] | Pure random |


### Phase 266: Compiler Design, Lexing, AST Parsing & Bytecode Virtual Machines
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-lexer-regex-tokenizer-engine-skill](https://github.com/Alpha-Park/genpark-lexer-regex-tokenizer-engine-skill) | Deterministic regex lexer & tokenizer with source line/column tracking | Service | [x] | Pure re |
| [genpark-recursive-descent-ast-parser-skill](https://github.com/Alpha-Park/genpark-recursive-descent-ast-parser-skill) | Recursive descent AST parser with precedence climbing & JSON tree | Service | [x] | Standard library |
| [genpark-stack-bytecode-virtual-machine-skill](https://github.com/Alpha-Park/genpark-stack-bytecode-virtual-machine-skill) | Stack-based bytecode virtual machine interpreter & operand stack | Service | [x] | Standard library |
| [genpark-lisp-scheme-s-expression-evaluator-skill](https://github.com/Alpha-Park/genpark-lisp-scheme-s-expression-evaluator-skill) | Minimalist Lisp / Scheme S-expression reader & environment frames | Service | [x] | Pure math |
| [genpark-type-checker-hindley-milner-skill](https://github.com/Alpha-Park/genpark-type-checker-hindley-milner-skill) | Hindley-Milner type inference engine with Algorithm W unification | Service | [x] | Standard library |


### Phase 267: Database Internals, B-Tree Indexes & Write-Ahead Logging (WAL)
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-b-tree-disk-storage-index-skill](https://github.com/Alpha-Park/genpark-b-tree-disk-storage-index-skill) | B+ Tree indexing engine with leaf pagination & range queries | Service | [x] | Pure bisect |
| [genpark-wal-write-ahead-log-recovery-skill](https://github.com/Alpha-Park/genpark-wal-write-ahead-log-recovery-skill) | ARIES-style Write-Ahead Logging (WAL) crash redo/undo recovery | Service | [x] | Standard library |
| [genpark-lsm-tree-sstable-compaction-skill](https://github.com/Alpha-Park/genpark-lsm-tree-sstable-compaction-skill) | LSM Tree storage engine with in-memory MemTable & SSTable flush | Service | [x] | Standard library |
| [genpark-mvcc-transaction-isolation-engine-skill](https://github.com/Alpha-Park/genpark-mvcc-transaction-isolation-engine-skill) | Multi-Version Concurrency Control (MVCC) snapshot isolation | Service | [x] | Standard library |
| [genpark-cost-based-query-optimizer-skill](https://github.com/Alpha-Park/genpark-cost-based-query-optimizer-skill) | Cost-based relational query optimizer evaluating join algorithms | Service | [x] | Standard library |


### Phase 268: Operating Systems Internals, CPU Scheduling & Memory Page Replacement
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-cpu-scheduler-round-robin-cfs-skill](https://github.com/Alpha-Park/genpark-cpu-scheduler-round-robin-cfs-skill) | Preemptive CPU scheduling simulator with Round-Robin & quantum slicing | Service | [x] | Pure collections |
| [genpark-page-replacement-lru-clock-lfu-skill](https://github.com/Alpha-Park/genpark-page-replacement-lru-clock-lfu-skill) | Virtual memory page replacement simulation (LRU & Second-Chance Clock) | Service | [x] | Standard library |
| [genpark-deadlock-detector-banker-resource-graph-skill](https://github.com/Alpha-Park/genpark-deadlock-detector-banker-resource-graph-skill) | Dijkstra's Banker's algorithm for safe resource state & deadlock avoidance | Service | [x] | Standard library |
| [genpark-virtual-memory-tlb-page-table-skill](https://github.com/Alpha-Park/genpark-virtual-memory-tlb-page-table-skill) | Virtual memory address translation simulator with TLB caching | Service | [x] | Pure collections |
| [genpark-disk-arm-scheduler-elevator-scan-skill](https://github.com/Alpha-Park/genpark-disk-arm-scheduler-elevator-scan-skill) | Hard disk head scheduling algorithms (SCAN / Elevator algorithm) | Service | [x] | Standard library |


### Phase 269: Computer Graphics, 3D Geometry, Ray Tracing & Quaternion Rotations
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-ray-tracer-sphere-plane-shading-skill](https://github.com/Alpha-Park/genpark-ray-tracer-sphere-plane-shading-skill) | 3D Whitted ray tracer with sphere/plane intersections & Phong shading | Service | [x] | Pure math |
| [genpark-quaternion-rotation-slerp-skill](https://github.com/Alpha-Park/genpark-quaternion-rotation-slerp-skill) | Unit quaternion 3D rotation, Hamiltonian products & SLERP interpolation | Service | [x] | Pure math |
| [genpark-mesh-obj-reader-poly-triangulator-skill](https://github.com/Alpha-Park/genpark-mesh-obj-reader-poly-triangulator-skill) | 3D mesh processor with Wavefront OBJ reader & polygon triangulation | Service | [x] | Standard library |
| [genpark-matrix4x4-perspective-projection-pipeline-skill](https://github.com/Alpha-Park/genpark-matrix4x4-perspective-projection-pipeline-skill) | Homogeneous 4x4 matrix pipeline with perspective frustum projection | Service | [x] | Pure math |
| [genpark-bezier-curve-surface-evaluator-skill](https://github.com/Alpha-Park/genpark-bezier-curve-surface-evaluator-skill) | Parametric polynomial curves with de Casteljau's algorithm | Service | [x] | Standard library |


### Phase 270: Autonomous Multi-Agent Swarm Orchestration, Task DAG Scheduling & Blackboard Architecture
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-blackboard-architecture-shared-memory-skill](https://github.com/Alpha-Park/genpark-blackboard-architecture-shared-memory-skill) | Blackboard pattern coordination with Knowledge Sources & agenda | Service | [x] | Standard library |
| [genpark-task-dag-critical-path-scheduler-skill](https://github.com/Alpha-Park/genpark-task-dag-critical-path-scheduler-skill) | Directed Acyclic Graph (DAG) scheduler with Critical Path Method (CPM) | Service | [x] | Pure collections |
| [genpark-contract-net-protocol-task-auctioneer-skill](https://github.com/Alpha-Park/genpark-contract-net-protocol-task-auctioneer-skill) | FIPA Contract Net Protocol (CNP) multi-agent auction coordinator | Service | [x] | Standard library |
| [genpark-subsumption-architecture-behavior-arbitration-skill](https://github.com/Alpha-Park/genpark-subsumption-architecture-behavior-arbitration-skill) | Brooks' Subsumption Architecture behavior priority arbitration | Service | [x] | Standard library |
| [genpark-bdi-belief-desire-intention-agent-skill](https://github.com/Alpha-Park/genpark-bdi-belief-desire-intention-agent-skill) | Belief-Desire-Intention (BDI) deliberative agent architecture | Service | [x] | Standard library |

### Phase 301: Autonomous Workplace Agent Capabilities & Multi-Agent Collaboration
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-agent-meeting-intelligence-action-extractor-skill](https://github.com/Alpha-Park/genpark-agent-meeting-intelligence-action-extractor-skill) | Autonomous executive meeting intelligence parser extracting structured action items, owner assignments, deadlines, and dependency risk scores | Service | [x] | Standard library |
| [genpark-agent-executive-briefing-dossier-synthesizer-skill](https://github.com/Alpha-Park/genpark-agent-executive-briefing-dossier-synthesizer-skill) | Cross-departmental executive briefing and morning dossier synthesizer aggregating Slack, email threads, and Jira updates into structured KPI summaries and risk signals | Service | [x] | Standard library |
| [genpark-agent-b2b-contract-negotiation-copilot-skill](https://github.com/Alpha-Park/genpark-agent-b2b-contract-negotiation-copilot-skill) | Autonomous B2B contract negotiation copilot analyzing counterparty concession velocity, contractual leverage, and generating strategic counter-offers | Service | [x] | Standard library |
| [genpark-agent-cross-doc-knowledge-mesh-validator-skill](https://github.com/Alpha-Park/genpark-agent-cross-doc-knowledge-mesh-validator-skill) | Multi-document enterprise knowledge mesh synthesizer detecting contradictions, outdated spec clauses, and missing dependencies across PRDs, RFCs, and wikis | Service | [x] | Standard library |
| [genpark-agent-sprint-velocity-capacity-forecaster-skill](https://github.com/Alpha-Park/genpark-agent-sprint-velocity-capacity-forecaster-skill) | Agile engineering sprint capacity and bottleneck forecaster simulating commitment feasibility, PTO impact, and technical debt risk distribution | Service | [x] | Standard library |


### Phase 306 — Messaging-Native Personal AI Agents & Autonomous Execution (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-messaging-agent-proactive-nudge-scheduler-skill`](https://github.com/Alpha-Park/genpark-messaging-agent-proactive-nudge-scheduler-skill) | Proactive contextual nudge scheduler for messaging-native personal agents with urgency decay and quiet-hours filtering | `proactive-agent`, `nudge-scheduler`, `messaging-agent`, `imessage` |
| [`genpark-agent-virtual-identity-proxy-sandbox-skill`](https://github.com/Alpha-Park/genpark-agent-virtual-identity-proxy-sandbox-skill) | Ephemeral virtual identity and credential proxy sandbox for personal agents with scoped tokens and budget bounds | `virtual-identity`, `agent-proxy`, `identity-isolation`, `privacy-sandbox` |
| [`genpark-autonomous-errand-action-dispatcher-skill`](https://github.com/Alpha-Park/genpark-autonomous-errand-action-dispatcher-skill) | Autonomous life-admin errand action dispatcher with finite state machine transitions and audit trail | `errand-dispatcher`, `life-admin`, `state-machine`, `autonomous-execution` |
| [`genpark-messaging-recipe-automation-workflow-skill`](https://github.com/Alpha-Park/genpark-messaging-recipe-automation-workflow-skill) | Declarative recipe automation engine for messaging personal agents parsing trigger-filter-action pipelines | `recipe-automation`, `workflow-engine`, `event-trigger`, `rule-dsl` |
| [`genpark-cloud-sandbox-task-delegation-coordinator-skill`](https://github.com/Alpha-Park/genpark-cloud-sandbox-task-delegation-coordinator-skill) | Cloud sandbox long-running task delegation coordinator with asynchronous state checkpointing and messaging heartbeats | `task-delegation`, `cloud-sandbox`, `async-coordinator`, `long-running-agent` |


### Phase 302 — AI Safety, LLM Guardrails & Prompt Injection Defense (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-prompt-injection-jailbreak-detector-skill`](https://github.com/Alpha-Park/genpark-prompt-injection-jailbreak-detector-skill) | Multi-stage regex and semantic pattern scanner detecting prompt injections, jailbreaks, and system prompt override attacks | `prompt-injection`, `jailbreak-detector`, `ai-safety`, `llm-guardrails` |
| [`genpark-pii-anonymizer-credential-scrubber-skill`](https://github.com/Alpha-Park/genpark-pii-anonymizer-credential-scrubber-skill) | High-performance PII and API secret token scrubber for prompt anonymization and data sanitization | `pii-scrubber`, `anonymizer`, `data-sanitization`, `secret-scanner` |
| [`genpark-canary-token-leak-sentinel-skill`](https://github.com/Alpha-Park/genpark-canary-token-leak-sentinel-skill) | HMAC-authenticated canary token generator and secret exfiltration leak detection sentinel | `canary-tokens`, `leak-detection`, `tripwire`, `ai-safety` |
| [`genpark-hallucination-factual-grounding-checker-skill`](https://github.com/Alpha-Park/genpark-hallucination-factual-grounding-checker-skill) | Factual grounding and citation overlap verifier measuring claim support against retrieved passages | `hallucination-detector`, `factual-grounding`, `faithfulness`, `ai-safety` |
| [`genpark-agent-output-schema-enforcer-guardrail-skill`](https://github.com/Alpha-Park/genpark-agent-output-schema-enforcer-guardrail-skill) | Strict JSON schema validator with streaming partial JSON repair, missing field filling, and sanitization | `schema-enforcer`, `json-guardrail`, `llm-guardrails`, `json-repair` |


### Phase 303 — Multi-Agent Swarms, Consensus & Collaborative Debate (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-multi-agent-debate-consensus-engine-skill`](https://github.com/Alpha-Park/genpark-multi-agent-debate-consensus-engine-skill) | Multi-agent adversarial debate engine with iterative rebuttals, scoring matrices, and consensus synthesis | `multi-agent`, `agent-debate`, `consensus`, `swarm-intelligence` |
| [`genpark-blackboard-shared-scratchpad-swarm-skill`](https://github.com/Alpha-Park/genpark-blackboard-shared-scratchpad-swarm-skill) | Centralized blackboard pattern for multi-agent swarm task posting, condition watching, and state accumulation | `blackboard-pattern`, `shared-memory`, `swarm-coordination`, `scratchpad` |
| [`genpark-contract-net-protocol-task-allocation-skill`](https://github.com/Alpha-Park/genpark-contract-net-protocol-task-allocation-skill) | FIPA Contract Net Protocol (CNP) multi-agent market mechanism for task bidding, evaluation, and awarding | `contract-net-protocol`, `task-allocation`, `market-mechanism`, `auction-theory` |
| [`genpark-agent-message-bus-topic-router-skill`](https://github.com/Alpha-Park/genpark-agent-message-bus-topic-router-skill) | Asynchronous pub/sub message bus with hierarchical wildcard topic matching and priority routing | `message-bus`, `topic-router`, `pub-sub`, `event-driven` |
| [`genpark-swarm-majority-voting-verifier-skill`](https://github.com/Alpha-Park/genpark-swarm-majority-voting-verifier-skill) | Multi-agent ensemble voting with Borda count, Condorcet analysis, and confidence-weighted majority resolution | `majority-voting`, `swarm-verifier`, `self-consistency`, `ensemble-ai` |


### Phase 304 — Code Intelligence, Autonomous Repair & AST Synthesis (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-ast-static-code-analyzer-linter-skill`](https://github.com/Alpha-Park/genpark-ast-static-code-analyzer-linter-skill) | Python AST visitor analyzing cyclomatic complexity, code smells, missing docstrings, and dangerous builtins | `ast-analyzer`, `static-analysis`, `code-linter`, `cyclomatic-complexity` |
| [`genpark-automated-code-patch-diff-synthesizer-skill`](https://github.com/Alpha-Park/genpark-automated-code-patch-diff-synthesizer-skill) | Unified diff generator and patch application engine using difflib with hunk matching and rollback | `code-patcher`, `unified-diff`, `difflib`, `git-patch` |
| [`genpark-autonomous-test-suite-fuzz-generator-skill`](https://github.com/Alpha-Park/genpark-autonomous-test-suite-fuzz-generator-skill) | Type-directed test case and boundary value fuzz input synthesizer for automated function testing | `fuzz-testing`, `test-generator`, `boundary-values`, `type-directed` |
| [`genpark-code-call-graph-dependency-extractor-skill`](https://github.com/Alpha-Park/genpark-code-call-graph-dependency-extractor-skill) | Static function call graph and module import dependency analyzer using Python AST inspection | `call-graph`, `dependency-analysis`, `ast-parser`, `code-intelligence` |
| [`genpark-git-conventional-commit-changelog-generator-skill`](https://github.com/Alpha-Park/genpark-git-conventional-commit-changelog-generator-skill) | Semantic code diff analyzer generating conventional commit messages and automated markdown changelogs | `conventional-commits`, `changelog-generator`, `git-tools`, `diff-analyzer` |


### Phase 305 — Agent Hierarchical Memory & Episodic State Management (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-hierarchical-tiered-memory-manager-skill`](https://github.com/Alpha-Park/genpark-hierarchical-tiered-memory-manager-skill) | MemGPT-inspired tiered memory system with working memory, archival storage, and automated context paging | `tiered-memory`, `memgpt`, `working-memory`, `archival-storage` |
| [`genpark-bm25-lexical-retrieval-memory-buffer-skill`](https://github.com/Alpha-Park/genpark-bm25-lexical-retrieval-memory-buffer-skill) | Pure Python BM25 Okapi lexical retrieval engine with document frequency inverted index for agent memory | `bm25`, `lexical-retrieval`, `inverted-index`, `vectorless-search` |
| [`genpark-episodic-memory-temporal-decay-manager-skill`](https://github.com/Alpha-Park/genpark-episodic-memory-temporal-decay-manager-skill) | Ebbinghaus forgetting curve memory decay with access recency, frequency weighting, and consolidation | `memory-decay`, `ebbinghaus-forgetting`, `episodic-memory`, `memory-consolidation` |
| [`genpark-agent-persona-entity-state-tracker-skill`](https://github.com/Alpha-Park/genpark-agent-persona-entity-state-tracker-skill) | Persistent user profile and entity relation state tracker with slot filling and contradiction resolution | `persona-tracker`, `user-modeling`, `entity-state`, `slot-filling` |
| [`genpark-conversation-summarizer-sliding-window-skill`](https://github.com/Alpha-Park/genpark-conversation-summarizer-sliding-window-skill) | Hierarchical conversational sliding window compressor with dialogue condensation and key decision preservation | `dialogue-summarizer`, `sliding-window`, `conversation-compression`, `context-engineering` |


### Phase 307 — Web Scraping, DOM Pruning & Content Distillation for Agents (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-html-to-markdown-semantic-converter-skill`](https://github.com/Alpha-Park/genpark-html-to-markdown-semantic-converter-skill) | Pure Python semantic HTML-to-markdown converter preserving headers, links, lists, and formatting | `html-to-markdown`, `markdown-converter`, `web-scraper`, `content-distillation` |
| [`genpark-dom-readability-boilerplate-remover-skill`](https://github.com/Alpha-Park/genpark-dom-readability-boilerplate-remover-skill) | Readability-inspired heuristic algorithm stripping navigation, footers, ads, and sidebars | `readability`, `boilerplate-removal`, `dom-pruning`, `content-extraction` |
| [`genpark-web-table-to-structured-json-parser-skill`](https://github.com/Alpha-Park/genpark-web-table-to-structured-json-parser-skill) | HTML table matrix parser extracting column headers and cell rows into structured JSON list of dicts | `table-parser`, `html-table`, `data-extraction`, `structured-data` |
| [`genpark-robots-txt-crawl-delay-policy-evaluator-skill`](https://github.com/Alpha-Park/genpark-robots-txt-crawl-delay-policy-evaluator-skill) | RFC 9309 robots.txt parser with path permissions, Disallow/Allow rules, and crawl delay compliance | `robots-txt`, `web-crawler`, `rfc-9309`, `crawl-delay` |
| [`genpark-url-canonicalization-deduplication-filter-skill`](https://github.com/Alpha-Park/genpark-url-canonicalization-deduplication-filter-skill) | URL normalizer sorting query parameters, stripping tracking UTM tokens, and deduplicating visited URLs | `url-canonicalization`, `url-normalizer`, `deduplication`, `tracking-stripper` |


### Phase 308 — Agent Evaluation, Benchmark Metrics & LLM-as-a-Judge (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-agent-trajectory-pass-fail-evaluator-skill`](https://github.com/Alpha-Park/genpark-agent-trajectory-pass-fail-evaluator-skill) | Step-by-step agent trajectory evaluator comparing execution traces against golden tool call sequences | `trajectory-evaluator`, `agent-benchmarks`, `evaluation`, `tool-call-eval` |
| [`genpark-llm-as-a-judge-rubric-scoring-engine-skill`](https://github.com/Alpha-Park/genpark-llm-as-a-judge-rubric-scoring-engine-skill) | Structured rubric evaluator calculating weighted composite Likert scores across quality criteria | `llm-as-a-judge`, `rubric-scoring`, `evaluation`, `quality-assurance` |
| [`genpark-rouge-bleu-lexical-overlap-metrics-skill`](https://github.com/Alpha-Park/genpark-rouge-bleu-lexical-overlap-metrics-skill) | Pure Python ROUGE-L and BLEU n-gram lexical overlap precision, recall, and F1 metrics calculation | `rouge-metric`, `bleu-metric`, `lexical-overlap`, `text-eval` |
| [`genpark-context-precision-recall-rag-metric-skill`](https://github.com/Alpha-Park/genpark-context-precision-recall-rag-metric-skill) | RAG context precision and context recall evaluator measuring retrieved chunk relevance and rank quality | `context-precision`, `context-recall`, `rag-evaluation`, `relevance` |
| [`genpark-tool-call-argument-accuracy-validator-skill`](https://github.com/Alpha-Park/genpark-tool-call-argument-accuracy-validator-skill) | Strict type, range, and semantic key validator for agent tool call invocations | `tool-call-validator`, `argument-validation`, `schema-compliance`, `agent-testing` |


### Phase 309 — Synthetic Data Generation, Prompt Distillation & Dataset Preparation (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-evol-instruct-prompt-complexity-enhancer-skill`](https://github.com/Alpha-Park/genpark-evol-instruct-prompt-complexity-enhancer-skill) | Evolutionary prompt mutation algorithm adding constraints, deepening reasoning, and increasing problem complexity | `evol-instruct`, `synthetic-data`, `prompt-engineering`, `complexity-enhancer` |
| [`genpark-dpo-preference-pair-dataset-generator-skill`](https://github.com/Alpha-Park/genpark-dpo-preference-pair-dataset-generator-skill) | Direct Preference Optimization (DPO) and RLHF dataset constructor pairing prompt, chosen, and rejected responses | `dpo-dataset`, `rlhf-preference`, `preference-pairs`, `reward-modeling` |
| [`genpark-alpaca-sharegpt-format-converter-skill`](https://github.com/Alpha-Park/genpark-alpaca-sharegpt-format-converter-skill) | Bidirectional dataset format converter and schema validator between Alpaca and ShareGPT formats | `format-converter`, `alpaca-format`, `sharegpt-format`, `dataset-prep` |
| [`genpark-prompt-token-length-budget-packager-skill`](https://github.com/Alpha-Park/genpark-prompt-token-length-budget-packager-skill) | Bin-packing optimizer grouping variable-length training examples into fixed context window token budgets | `token-budget-packager`, `bin-packing`, `context-window`, `optimization` |
| [`genpark-synthetic-qa-pair-corpus-extractor-skill`](https://github.com/Alpha-Park/genpark-synthetic-qa-pair-corpus-extractor-skill) | Rule-based and heuristic question-answer pair generator extracting factual and definitional training tuples from raw text | `qa-corpus-extractor`, `synthetic-qa`, `corpus-mining`, `data-synthesis` |


### Phase 310 — Real-Time Streaming, Token Chunking & SSE Protocol Handlers (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-sse-server-sent-events-protocol-parser-skill`](https://github.com/Alpha-Park/genpark-sse-server-sent-events-protocol-parser-skill) | RFC-compliant Server-Sent Events (SSE) streaming frame parser handling data, events, ids, and multi-line payloads | `sse-parser`, `server-sent-events`, `streaming`, `event-stream` |
| [`genpark-streaming-token-delimiter-chunker-skill`](https://github.com/Alpha-Park/genpark-streaming-token-delimiter-chunker-skill) | Smooth streaming tokenizer grouping raw token deltas into natural word and sentence boundaries for UI rendering | `token-chunker`, `streaming`, `delimiter-chunking`, `ui-smoothing` |
| [`genpark-token-bucket-rate-limiter-burst-controller-skill`](https://github.com/Alpha-Park/genpark-token-bucket-rate-limiter-burst-controller-skill) | High-precision token bucket rate limiter with burst capability for LLM token quotas and TPM enforcement | `rate-limiter`, `token-bucket`, `burst-controller`, `traffic-shaping` |
| [`genpark-streaming-markdown-code-block-tracker-skill`](https://github.com/Alpha-Park/genpark-streaming-markdown-code-block-tracker-skill) | State-machine tracker detecting unclosed code blocks and formatting tags in live streaming LLM output | `markdown-tracker`, `streaming-markdown`, `code-block-parser`, `syntax-highlighting` |
| [`genpark-sliding-window-moving-throughput-monitor-skill`](https://github.com/Alpha-Park/genpark-sliding-window-moving-throughput-monitor-skill) | Sliding window time-series monitor measuring real-time token throughput (TPS), TTFT, and inter-token latency percentiles | `throughput-monitor`, `tps-monitor`, `ttft-metric`, `latency-tracker` |


### Phase 311 — Multi-Modal Vision & Image Processing for Autonomous Agents (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-base64-image-mime-dimension-analyzer-skill`](https://github.com/Alpha-Park/genpark-base64-image-mime-dimension-analyzer-skill) | Zero-dependency binary image header parser extracting dimensions, aspect ratios, byte sizes, and MIME types | `image-analyzer`, `vision-tools`, `base64-image`, `image-dimensions` |
| [`genpark-bounding-box-iou-coordinate-normalizer-skill`](https://github.com/Alpha-Park/genpark-bounding-box-iou-coordinate-normalizer-skill) | 2D bounding box normalizer, IoU calculator, and Non-Maximum Suppression (NMS) engine for vision agents | `bounding-box`, `iou-calculator`, `nms-filter`, `coordinate-normalizer` |
| [`genpark-ascii-art-visual-terminal-rasterizer-skill`](https://github.com/Alpha-Park/genpark-ascii-art-visual-terminal-rasterizer-skill) | Grayscale pixel array rasterizer creating ASCII terminal representations and visual heatmaps for CLI agents | `ascii-rasterizer`, `terminal-vision`, `image-preview`, `cli-visualization` |
| [`genpark-image-token-cost-calculator-skill`](https://github.com/Alpha-Park/genpark-image-token-cost-calculator-skill) | Multi-modal vision token cost and tile decomposition calculator for OpenAI, Anthropic, and Google architectures | `vision-token-calculator`, `token-budget`, `image-pricing`, `multimodal-llm` |
| [`genpark-spatial-grid-anchor-point-mapper-skill`](https://github.com/Alpha-Park/genpark-spatial-grid-anchor-point-mapper-skill) | Continuous viewport to discrete UI grid cell and center click coordinate mapper for computer-use agents | `spatial-grid-mapper`, `anchor-points`, `ui-automation`, `computer-use` |


### Phase 312 — Agent Workflow Graph & Directed Acyclic Graph (DAG) Execution Engines (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-dag-topological-sort-dependency-resolver-skill`](https://github.com/Alpha-Park/genpark-dag-topological-sort-dependency-resolver-skill) | Directed Acyclic Graph dependency validator, Kahn topological sort algorithm, and cycle detection for agent tasks | `dag-resolver`, `topological-sort`, `workflow-engine`, `dependency-graph` |
| [`genpark-parallel-subtask-wavefront-scheduler-skill`](https://github.com/Alpha-Park/genpark-parallel-subtask-wavefront-scheduler-skill) | Wavefront level scheduler grouping independent DAG tasks into parallel execution stages | `wavefront-scheduler`, `parallel-execution`, `task-partitioner`, `concurrency` |
| [`genpark-conditional-branch-router-state-evaluator-skill`](https://github.com/Alpha-Park/genpark-conditional-branch-router-state-evaluator-skill) | Dynamic predicate evaluator over agent state dictionaries for dynamic workflow branch routing | `branch-router`, `state-evaluator`, `workflow-graph`, `decision-tree` |
| [`genpark-workflow-checkpoint-state-serializer-skill`](https://github.com/Alpha-Park/genpark-workflow-checkpoint-state-serializer-skill) | Workflow execution state graph snapshot serializer with delta compression and undo/redo journaling | `checkpoint-serializer`, `state-snapshot`, `journaling`, `undo-redo` |
| [`genpark-compensation-saga-rollback-orchestrator-skill`](https://github.com/Alpha-Park/genpark-compensation-saga-rollback-orchestrator-skill) | Distributed Saga transaction orchestrator executing forward actions and compensating reverse rollbacks | `saga-orchestrator`, `compensation-rollback`, `distributed-transactions`, `failure-recovery` |


### Phase 313 — Vector Quantization, Inverted File Index & Approximate Nearest Neighbors (ANN) (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-hierarchical-navigable-small-world-hnsw-graph-skill`](https://github.com/Alpha-Park/genpark-hierarchical-navigable-small-world-hnsw-graph-skill) | Pure Python Hierarchical Navigable Small World (HNSW) proximity graph for fast vector approximate nearest neighbor search | `hnsw-graph`, `ann-search`, `vector-index`, `nearest-neighbors` |
| [`genpark-product-quantization-compression-engine-skill`](https://github.com/Alpha-Park/genpark-product-quantization-compression-engine-skill) | Product Quantization (PQ) vector compression engine partitioning embeddings into discrete codebook indices | `product-quantization`, `vector-compression`, `codebook-quantizer`, `quantization` |
| [`genpark-locality-sensitive-hashing-lsh-cosine-index-skill`](https://github.com/Alpha-Park/genpark-locality-sensitive-hashing-lsh-cosine-index-skill) | Random hyperplane Locality-Sensitive Hashing (LSH) for sub-linear cosine similarity candidate generation | `lsh-cosine`, `locality-sensitive-hashing`, `hyperplane-hashing`, `cosine-similarity` |
| [`genpark-inverted-file-ivf-centroid-clusterer-skill`](https://github.com/Alpha-Park/genpark-inverted-file-ivf-centroid-clusterer-skill) | Inverted File (IVF) index routing vectors to Voronoi cell centroids for pruned sub-linear retrieval | `ivf-index`, `inverted-file`, `voronoi-cells`, `centroid-clustering` |
| [`genpark-vector-similarity-exact-and-topk-heap-selector-skill`](https://github.com/Alpha-Park/genpark-vector-similarity-exact-and-topk-heap-selector-skill) | Bounded Min-Heap Top-K cosine similarity and Euclidean distance selector for vector retrieval | `topk-heap`, `cosine-similarity`, `euclidean-distance`, `heap-selector` |


### Phase 314 — Agent Self-Correction, Reflexion & Iterative Refinement Loops (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-reflexion-episodic-critique-memory-buffer-skill`](https://github.com/Alpha-Park/genpark-reflexion-episodic-critique-memory-buffer-skill) | Reflexion episodic failure memory buffer accumulating self-critiques and trial corrective plans | `reflexion`, `self-correction`, `critique-memory`, `episodic-buffer` |
| [`genpark-self-consistency-majority-voting-aggregator-skill`](https://github.com/Alpha-Park/genpark-self-consistency-majority-voting-aggregator-skill) | Self-Consistency majority voting aggregator computing consensus answers, confidence scores, and Shannon entropy | `self-consistency`, `majority-voting`, `consensus`, `confidence-score` |
| [`genpark-critic-code-lint-test-feedback-synthesizer-skill`](https://github.com/Alpha-Park/genpark-critic-code-lint-test-feedback-synthesizer-skill) | Distills compilation errors, exceptions, and linter diagnostics into prioritized self-healing instructions | `lint-synthesizer`, `code-critic`, `test-feedback`, `self-healing` |
| [`genpark-iterative-refinement-convergence-detector-skill`](https://github.com/Alpha-Park/genpark-iterative-refinement-convergence-detector-skill) | Sequential code revision similarity and edit distance monitor detecting convergence and cyclic oscillation | `convergence-detector`, `refinement-loop`, `edit-distance`, `sequence-matcher` |
| [`genpark-backtracking-tree-search-pruning-controller-skill`](https://github.com/Alpha-Park/genpark-backtracking-tree-search-pruning-controller-skill) | MCTS and Tree of Thoughts backtracking controller scoring intermediate reasoning states and pruning low-value branches | `tree-search`, `backtracking`, `branch-pruning`, `tree-of-thoughts` |


### Phase 315 — Structured Output Generation & Context-Free Grammar (CFG) Masking (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-cfg-grammar-token-mask-generator-skill`](https://github.com/Alpha-Park/genpark-cfg-grammar-token-mask-generator-skill) | State-machine computing allowable next character/token masks from Context-Free Grammars (EBNF) for structured output | `cfg-grammar`, `token-masking`, `ebnf-parser`, `structured-generation` |
| [`genpark-partial-json-parser-stream-completer-skill`](https://github.com/Alpha-Park/genpark-partial-json-parser-stream-completer-skill) | Resilient streaming JSON completer repairing truncated in-flight JSON tokens into valid parse trees | `partial-json`, `stream-completer`, `json-parser`, `streaming-json` |
| [`genpark-json-schema-to-regex-converter-skill`](https://github.com/Alpha-Park/genpark-json-schema-to-regex-converter-skill) | Compiles JSON Schema definitions into regular expression patterns for regex-constrained decoding | `schema-to-regex`, `regex-constrained`, `json-schema`, `structured-decoding` |
| [`genpark-enum-and-type-choice-constrained-decoder-skill`](https://github.com/Alpha-Park/genpark-enum-and-type-choice-constrained-decoder-skill) | Filters model outputs to strictly valid enumerable tool actions and parameter choices, preventing hallucination | `constrained-decoder`, `enum-matcher`, `action-filter`, `type-constraints` |
| [`genpark-sql-syntax-abstract-syntax-tree-validator-skill`](https://github.com/Alpha-Park/genpark-sql-syntax-abstract-syntax-tree-validator-skill) | In-memory recursive SQL query validator checking syntax safety and blocking dangerous DDL/DML injection commands | `sql-validator`, `ast-parser`, `sql-safety`, `injection-guard` |

### Phase 316: Reinforcement Learning from Human Feedback (RLHF) & Reward Modeling
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-pairwise-bradley-terry-reward-model-skill](https://github.com/Alpha-Park/genpark-pairwise-bradley-terry-reward-model-skill) | Bradley-Terry pairwise preference ranking and log-likelihood reward model scoring engine for alignment | Service | [x] | Standard library |
| [genpark-ppo-clipped-surrogate-loss-evaluator-skill](https://github.com/Alpha-Park/genpark-ppo-clipped-surrogate-loss-evaluator-skill) | Evaluates Proximal Policy Optimization (PPO) clipped surrogate loss objective and policy gradient ratio | Service | [x] | Standard library |
| [genpark-generalized-advantage-estimation-gae-skill](https://github.com/Alpha-Park/genpark-generalized-advantage-estimation-gae-skill) | Calculates Generalized Advantage Estimation (GAE-lambda) temporal difference residuals across rollout trajectories | Service | [x] | Standard library |
| [genpark-kullback-leibler-divergence-drift-monitor-skill](https://github.com/Alpha-Park/genpark-kullback-leibler-divergence-drift-monitor-skill) | Tracks KL-divergence drift between active policy and frozen reference policy to prevent reward hacking | Service | [x] | Standard library |
| [genpark-length-bias-penalty-reward-calibrator-skill](https://github.com/Alpha-Park/genpark-length-bias-penalty-reward-calibrator-skill) | Normalizes verbose completion reward hacking via character-length penalty discounting and calibrated score adjustment | Service | [x] | Standard library |

### Phase 316: Autonomous Presentation Synthesis, Layout Engineering & In-Place Canvas Agent Skills
| Repository | Description | Category | MCP Ready | Python Standard Lib |
|---|---|---|---|---|
| [genpark-agent-presentation-slide-deck-synthesizer-skill](https://github.com/Alpha-Park/genpark-agent-presentation-slide-deck-synthesizer-skill) | Post-trained consultant-grade presentation generator structuring business topics into cohesive slide decks with golden pyramid layouts | Service | [x] | Standard library |
| [genpark-agent-in-place-canvas-ast-patcher-skill](https://github.com/Alpha-Park/genpark-agent-in-place-canvas-ast-patcher-skill) | Fine-grained block AST patcher for in-place canvas editing allowing surgical node updates without full document rebuild | Service | [x] | Standard library |
| [genpark-agent-executive-chart-visual-compiler-skill](https://github.com/Alpha-Park/genpark-agent-executive-chart-visual-compiler-skill) | Compiles raw metrics and financial datasets into boardroom-ready SVG/JSON chart configurations optimized for presentation slides | Service | [x] | Standard library |
| [genpark-agent-second-brain-episodic-memory-mesh-skill](https://github.com/Alpha-Park/genpark-agent-second-brain-episodic-memory-mesh-skill) | Persistent episodic memory mesh extractor building cross-session entity relationship graphs and decision logs | Service | [x] | Standard library |
| [genpark-agent-extended-thinking-verification-critic-skill](https://github.com/Alpha-Park/genpark-agent-extended-thinking-verification-critic-skill) | Multi-round extended thinking critic performing backtracking, hypothesis testing, and factual ground checks | Service | [x] | Standard library |


### Phase 322 — Social Workflow, Swarm Orchestration & Dynamic Personalization Suite (Product Hunt October 2026 Top Winners)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-autonomous-cross-platform-social-workflow-scheduler-skill`](https://github.com/Alpha-Park/genpark-autonomous-cross-platform-social-workflow-scheduler-skill) | Adapts core content into platform-native formats and computes optimal posting windows across social channels | `social-media-agent`, `content-scheduler`, `cross-platform-publishing`, `workflow-automation` |
| [`genpark-automated-social-engagement-and-brand-audit-engine-skill`](https://github.com/Alpha-Park/genpark-automated-social-engagement-and-brand-audit-engine-skill) | Audits brand social metrics, engagement velocity, and identifies content gaps automatically | `social-audit`, `brand-analytics`, `engagement-velocity`, `competitor-benchmarking` |
| [`genpark-dynamic-landing-page-personalization-and-ab-optimizer-skill`](https://github.com/Alpha-Park/genpark-dynamic-landing-page-personalization-and-ab-optimizer-skill) | Dynamically tailors hero copy, social proof, and CTA variants based on visitor UTM referrer and ICP segment | `landing-page-optimizer`, `dynamic-personalization`, `ab-testing`, `conversion-optimization` |
| [`genpark-agent-swarm-task-decomposer-and-consensus-aggregator-skill`](https://github.com/Alpha-Park/genpark-agent-swarm-task-decomposer-and-consensus-aggregator-skill) | Decomposes complex goals into parallel worker subtasks and aggregates consensus outputs | `agent-swarm`, `task-decomposition`, `consensus-aggregator`, `multi-agent-orchestration` |
| [`genpark-cross-app-event-trigger-and-state-machine-orchestrator-skill`](https://github.com/Alpha-Park/genpark-cross-app-event-trigger-and-state-machine-orchestrator-skill) | Evaluates incoming webhook events and advances deterministic cross-app workflow states | `state-machine`, `event-orchestrator`, `cross-app-automation`, `webhook-router` |

### Phase 321 — Model Routing, Cost Governance & Agentic Browser Runtime Suite (Product Hunt October 2026 Distillation)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-dynamic-llm-router-cost-latency-optimizer-skill`](https://github.com/Alpha-Park/genpark-dynamic-llm-router-cost-latency-optimizer-skill) | Selects optimal model endpoint based on query complexity, budget, and latency tolerance | `model-router`, `cost-optimizer`, `latency-router`, `llm-gateway` |
| [`genpark-agentic-operational-cost-and-token-auditor-skill`](https://github.com/Alpha-Park/genpark-agentic-operational-cost-and-token-auditor-skill) | Tracks token consumption, calculates exact cloud costs, and identifies budget anomalies for agent sessions | `cost-auditor`, `token-tracking`, `agent-observability`, `finops-ai` |
| [`genpark-agent-api-governance-and-rbac-policy-proxy-skill`](https://github.com/Alpha-Park/genpark-agent-api-governance-and-rbac-policy-proxy-skill) | Enforces fine-grained permissions on agent tool calls and data access scopes | `api-governance`, `rbac-proxy`, `agent-security`, `policy-enforcement` |
| [`genpark-agentic-browser-dom-snapshot-and-console-monitor-skill`](https://github.com/Alpha-Park/genpark-agentic-browser-dom-snapshot-and-console-monitor-skill) | Captures structured accessibility tree snapshots and intercepts runtime console logs for browser agents | `browser-runtime`, `dom-snapshot`, `console-monitor`, `web-agent` |
| [`genpark-multi-agent-workspace-state-lock-and-broadcast-skill`](https://github.com/Alpha-Park/genpark-multi-agent-workspace-state-lock-and-broadcast-skill) | Manages distributed locks on resources and broadcasts change events to peer agents in shared workspaces | `workspace-state`, `multi-agent-sync`, `distributed-lock`, `state-broadcast` |

### Phase 320 — Multimodal Media, Executive Triage & Autonomous CX Suite (Product Hunt Top Monthly Distillation)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-multimodal-video-clip-semantic-segmentation-skill`](https://github.com/Alpha-Park/genpark-multimodal-video-clip-semantic-segmentation-skill) | Extracts timestamp boundaries, semantic scenes, and viral clip candidate segments from long-form video transcripts | `video-segmentation`, `semantic-clips`, `video-editor`, `multimodal-agent` |
| [`genpark-proactive-executive-calendar-and-action-item-prioritizer-skill`](https://github.com/Alpha-Park/genpark-proactive-executive-calendar-and-action-item-prioritizer-skill) | Triages meeting requests, detects conflicting commitments, and assigns priority tiers for executive calendars | `executive-assistant`, `calendar-prioritizer`, `action-item-triage`, `productivity-agent` |
| [`genpark-high-converting-ad-copy-hook-and-cta-synthesizer-skill`](https://github.com/Alpha-Park/genpark-high-converting-ad-copy-hook-and-cta-synthesizer-skill) | Formulates psychology-driven advertising hooks, primary body copy, and CTA variants for marketing campaigns | `ad-copy-generator`, `marketing-hooks`, `conversion-rate-optimization`, `cta-synthesizer` |
| [`genpark-autonomous-software-ui-clickpath-and-macro-executor-skill`](https://github.com/Alpha-Park/genpark-autonomous-software-ui-clickpath-and-macro-executor-skill) | Models user journey sequences, conditional decision branches, and execution action trees for autonomous software navigation | `ui-automation`, `clickpath-planner`, `self-driving-software`, `macro-executor` |
| [`genpark-self-improving-cx-ticket-sentiment-and-resolution-matcher-skill`](https://github.com/Alpha-Park/genpark-self-improving-cx-ticket-sentiment-and-resolution-matcher-skill) | Analyzes customer ticket emotional urgency, maps matching resolution playbooks, and templates responses | `cx-automation`, `sentiment-analysis`, `ticket-resolution`, `support-agent` |

### Phase 319 — Autonomous Infrastructure, GEO & Incident Resilience Suite (Product Hunt October 2026 Distillation)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-mcp-unified-context-compaction-and-rate-limiter-skill`](https://github.com/Alpha-Park/genpark-mcp-unified-context-compaction-and-rate-limiter-skill) | Manages MCP tool execution rate limits and compresses bloated tool response context payloads | `context-compaction`, `rate-limiter`, `token-optimization`, `payload-compression` |
| [`genpark-natural-language-saas-action-controller-skill`](https://github.com/Alpha-Park/genpark-natural-language-saas-action-controller-skill) | Translates high-level natural language phrases into deterministic SaaS API schema payloads | `saas-automation`, `action-controller`, `natural-language-api`, `intent-parser` |
| [`genpark-generative-engine-optimization-and-citation-scorer-skill`](https://github.com/Alpha-Park/genpark-generative-engine-optimization-and-citation-scorer-skill) | Analyzes digital content for AI search engine citation visibility, factual definitions, and structured metrics | `geo`, `generative-engine-optimization`, `citation-scorer`, `ai-search-optimization` |
| [`genpark-proactive-production-incident-remediation-skill`](https://github.com/Alpha-Park/genpark-proactive-production-incident-remediation-skill) | Observes telemetry errors, maps root causes, and generates safe executable runbooks for production incident mitigation | `incident-remediation`, `sre-agent`, `root-cause-analysis`, `runbook-generator` |
| [`genpark-episodic-agent-memory-indexer-and-decay-retriever-skill`](https://github.com/Alpha-Park/genpark-episodic-agent-memory-indexer-and-decay-retriever-skill) | Stores agent episodic memories with semantic tag indexes and time-decay relevance calculation | `agent-memory`, `episodic-memory`, `memory-retriever`, `time-decay` |

### Phase 318 — Autonomous Growth, Demo & Agentic Engineering Suite (Product Hunt Top Monthly Distillation)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-autonomous-lead-scoring-and-outreach-synthesizer-skill`](https://github.com/Alpha-Park/genpark-autonomous-lead-scoring-and-outreach-synthesizer-skill) | Scores outbound lead profiles, evaluates purchase intent, and synthesizes personalized multi-channel outreach messages | `lead-scoring`, `outreach-automation`, `sales-agent`, `b2b-growth` |
| [`genpark-multimodal-video-demo-script-and-narration-generator-skill`](https://github.com/Alpha-Park/genpark-multimodal-video-demo-script-and-narration-generator-skill) | Transforms UI workflow action sequences into structured video demo chapters, narration voiceover scripts, and timing metadata | `video-scripting`, `product-demo`, `narration-generator`, `ui-walkthrough` |
| [`genpark-agentic-team-collaboration-messaging-bridge-skill`](https://github.com/Alpha-Park/genpark-agentic-team-collaboration-messaging-bridge-skill) | Normalizes, routes, and thread-correlates multi-agent notifications and interactive prompts across team collaboration channels | `collaboration-bridge`, `slack-integration`, `team-messaging`, `agent-orchestration` |
| [`genpark-interactive-product-tour-qualification-dialogue-engine-skill`](https://github.com/Alpha-Park/genpark-interactive-product-tour-qualification-dialogue-engine-skill) | Conducts conversational qualification, dynamically tailoring step-by-step product walkthrough paths based on prospect pain points | `product-tour`, `qualification-dialogue`, `interactive-demo`, `buyer-journey` |
| [`genpark-agentic-git-diff-pr-review-and-patch-synthesizer-skill`](https://github.com/Alpha-Park/genpark-agentic-git-diff-pr-review-and-patch-synthesizer-skill) | Parses unified git diffs, detects security and performance anomalies, generates inline code reviews, and synthesizes unified patches | `code-review`, `git-diff-analyzer`, `patch-synthesizer`, `agentic-engineering` |

### Phase 317 — Tool Calling Resilience & Schema Repair (2026 Frontier)
| Skill / Repository | Description | Topics |
| :--- | :--- | :--- |
| [`genpark-malformed-json-escape-character-sanitizer-skill`](https://github.com/Alpha-Park/genpark-malformed-json-escape-character-sanitizer-skill) | Sanitizes unescaped newlines, control characters, single-quoted keys, and trailing commas in model tool call JSON | `json-sanitizer`, `tool-call-repair`, `malformed-json`, `syntax-repair` |
| [`genpark-fuzzy-tool-parameter-name-resolver-skill`](https://github.com/Alpha-Park/genpark-fuzzy-tool-parameter-name-resolver-skill) | Resolves misspelled or hallucinated tool argument names against declared JSON schemas via difflib distance | `fuzzy-resolver`, `parameter-matching`, `schema-repair`, `tool-resilience` |
| [`genpark-type-coercion-and-casting-engine-skill`](https://github.com/Alpha-Park/genpark-type-coercion-and-casting-engine-skill) | Intelligently coerces stringified integers, booleans, and JSON array strings into strictly schema-compliant types | `type-coercion`, `schema-validator`, `argument-casting`, `defensive-parsing` |
| [`genpark-missing-required-parameter-fallback-injector-skill`](https://github.com/Alpha-Park/genpark-missing-required-parameter-fallback-injector-skill) | Automatically injects safe defaults, user profile contextual values, and fallbacks for omitted required schema parameters | `fallback-injector`, `default-parameters`, `schema-completion`, `robust-execution` |
| [`genpark-argument-boundary-clamping-filter-skill`](https://github.com/Alpha-Park/genpark-argument-boundary-clamping-filter-skill) | Clamps numeric parameters and truncates unbounded string payloads to schema minimums, maximums, and string length bounds | `boundary-clamper`, `argument-clamping`, `payload-sanitizer`, `safety-guardrail` |
