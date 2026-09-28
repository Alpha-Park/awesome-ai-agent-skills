"""Line-delimited JSON-RPC stdio transport, tested with the official MCP client."""
import inspect
import json
import math
import sys
from .client import VoiceTurnTakingEndpointDetector

NAME = 'genpark-voice-vad'
VERSION = "1.0.1"
SCHEMAS = {'analyze_turn_status': {'frame_energies_db': {'type': 'array', 'items': {'type': 'number'}}, 'transcript_fragment': {'type': 'string'}, 'elapsed_silence_ms': {'type': 'number', 'minimum': 0}}, 'calibrate_acoustic_thresholds': {'ambient_frames_db': {'type': 'array', 'items': {'type': 'number'}}}, 'predict_semantic_closure': {'transcript_fragment': {'type': 'string'}}, 'run_benchmark_turn_detection': {}}

def validate(value, schema):
    kind = schema.get("type")
    valid = {"object": isinstance(value, dict), "array": isinstance(value, list),
             "string": isinstance(value, str),
             "number": type(value) in (int, float) and math.isfinite(value),
             "integer": type(value) is int}
    if kind and not valid[kind]:
        raise ValueError("Expected " + kind)
    if kind in ("number", "integer") and "minimum" in schema and value < schema["minimum"]:
        raise ValueError("Value below minimum")
    if kind == "array":
        for item in value:
            validate(item, schema["items"])
    if kind == "object":
        props = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                raise ValueError("Missing argument: " + key)
        for key, item in value.items():
            if key in props:
                validate(item, props[key])
            elif schema.get("additionalProperties") is False:
                raise ValueError("Unknown argument: " + key)
            elif isinstance(schema.get("additionalProperties"), dict):
                validate(item, schema["additionalProperties"])

def main():
    client = VoiceTurnTakingEndpointDetector()
    if "--test" in sys.argv:
        print(json.dumps(getattr(client, 'run_benchmark_turn_detection')(), allow_nan=False))
        return
    for line in sys.stdin:
        if not line.strip():
            continue
        rid = None
        try:
            req = json.loads(line)
        except (ValueError, TypeError):
            print(json.dumps({"jsonrpc":"2.0","id":None,"error":{"code":-32700,"message":"Parse error"}}), flush=True)
            continue
        if not isinstance(req, dict) or req.get("jsonrpc") != "2.0" or not isinstance(req.get("method"), str):
            print(json.dumps({"jsonrpc":"2.0","id":None,"error":{"code":-32600,"message":"Invalid Request"}}), flush=True)
            continue
        if "id" not in req:
            continue  # Notifications never receive a response.
        rid = req["id"]
        response = {"jsonrpc":"2.0", "id":rid}
        method = req["method"]
        params = req.get("params", {})
        try:
            if not isinstance(params, dict):
                raise ValueError("params must be an object")
            if method == "initialize":
                requested = params.get("protocolVersion")
                version = requested if requested in ("2024-11-05", "2025-03-26", "2025-06-18", "2025-11-25") else "2025-11-25"
                result = {"protocolVersion":version,"capabilities":{"tools":{"listChanged":False}},"serverInfo":{"name":NAME,"version":VERSION}}
            elif method == "ping":
                result = {}
            elif method == "tools/list":
                result = {"tools":[{"name":n,"description":inspect.getdoc(getattr(client,n)) or n.replace("_", " "),"inputSchema":{"type":"object","properties":p,"required":list(p),"additionalProperties":False}} for n,p in SCHEMAS.items()]}
            elif method == "tools/call":
                name = params.get("name")
                if not isinstance(name, str) or name not in SCHEMAS:
                    raise ValueError("Unknown tool")
                args = params.get("arguments", {})
                validate(args, {"type":"object","properties":SCHEMAS[name],"required":list(SCHEMAS[name]),"additionalProperties":False})
                try:
                    # Benchmarks use isolated state; they cannot reset a live session.
                    instance = VoiceTurnTakingEndpointDetector() if name.startswith("run_benchmark_") else client
                    value = getattr(instance,name)(**args)
                    result = {"content":[{"type":"text","text":json.dumps(value, allow_nan=False)}],"isError":False}
                except (ValueError, TypeError, KeyError, IndexError, OverflowError) as exc:
                    result = {"content":[{"type":"text","text":str(exc)}],"isError":True}
            else:
                response["error"] = {"code":-32601,"message":"Method not found"}
                print(json.dumps(response), flush=True)
                continue
            response["result"] = result
        except (ValueError, TypeError, OverflowError) as exc:
            response["error"] = {"code":-32602,"message":str(exc)}
        print(json.dumps(response, allow_nan=False), flush=True)

if __name__ == "__main__":
    main()
