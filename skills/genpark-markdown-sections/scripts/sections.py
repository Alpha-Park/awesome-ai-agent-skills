"""ATX section boundaries with fenced-code awareness and line provenance. MIT."""
import json
import re
import sys


def sections(text):
    lines = text.splitlines(keepends=True)
    result, path = [], []
    start, fence = 0, None
    for index, line in enumerate(lines):
        if fence:
            if re.fullmatch(r" {0,3}" + re.escape(fence[0]) + "{" + str(fence[1]) + r",}[ \t]*", line.rstrip("\r\n")):
                fence = None
            continue
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if opening and not (opening[1][0] == "`" and "`" in opening[2]):
            fence = (opening[1][0], len(opening[1]))
            continue
        heading = re.match(r"^ {0,3}(#{1,6})(?:[ \t]+(.*)|[ \t]*)$", line.rstrip("\r\n"))
        if heading:
            if index > start:
                result.append({"heading_path": [p[1] for p in path], "start_line": start + 1, "end_line": index, "text": "".join(lines[start:index])})
            level = len(heading[1])
            title = re.sub(r"(?:^|[ \t]+)#+[ \t]*$", "", heading[2] or "").strip()
            path = [p for p in path if p[0] < level] + [(level, title)]
            start = index
    if lines:
        result.append({"heading_path": [p[1] for p in path], "start_line": start + 1, "end_line": len(lines), "text": "".join(lines[start:])})
    return result


if __name__ == "__main__":
    sys.stdin.reconfigure(encoding="utf-8", newline="")
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(sections(sys.stdin.read()), ensure_ascii=False))
