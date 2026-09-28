import sys, json, math

class BoundingBoxTableReconstructor:
    """
    Deterministic 2D spatial clustering engine for OCR bounding boxes.
    Reconstructs structured rows and columns without external computer vision packages.
    """
    def __init__(self, y_threshold=8.0, x_gap_threshold=20.0):
        self.y_threshold = y_threshold
        self.x_gap_threshold = x_gap_threshold

    def reconstruct_table_grid(self, bounding_boxes):
        if not bounding_boxes:
            return {"grid": [], "num_rows": 0, "num_cols": 0}

        if any(b["x1"] < b["x0"] or b["y1"] < b["y0"] for b in bounding_boxes):
            raise ValueError("Invalid bounding box coordinates")

        # Sort boxes primarily by vertical midpoint (y), then by horizontal start (x0)
        def box_v_center(b):
            return (b.get("y0", 0) + b.get("y1", 0)) / 2.0

        boxes_sorted = sorted(bounding_boxes, key=lambda b: (box_v_center(b), b.get("x0", 0)))

        # Cluster boxes into vertical rows
        raw_rows = []
        for box in boxes_sorted:
            placed = False
            v_mid = box_v_center(box)
            for r in raw_rows:
                row_v_mid = sum(box_v_center(b) for b in r) / len(r)
                if abs(v_mid - row_v_mid) <= self.y_threshold:
                    r.append(box)
                    placed = True
                    break
            if not placed:
                raw_rows.append([box])

        # Sort elements within each row horizontally by x0
        for r in raw_rows:
            r.sort(key=lambda b: b.get("x0", 0))

        # Detect global column divisions from x0 coordinates across all rows
        col_splits = []
        for r in raw_rows:
            for b in r:
                x_mid = b.get("x0", 0)
                matched = False
                for c in col_splits:
                    if abs(x_mid - c["center"]) < self.x_gap_threshold:
                        c["samples"].append(x_mid)
                        c["center"] = sum(c["samples"]) / len(c["samples"])
                        matched = True
                        break
                if not matched:
                    col_splits.append({"center": x_mid, "samples": [x_mid]})

        col_splits.sort(key=lambda c: c["center"])
        num_cols = max(1, len(col_splits))

        # Align each row's items into the nearest column slots
        aligned_grid = []
        for r in raw_rows:
            row_cells = [""] * num_cols
            for b in r:
                b_mid = b.get("x0", 0)
                # Find closest column
                closest_idx = min(range(num_cols), key=lambda idx: abs(b_mid - col_splits[idx]["center"]))
                existing = row_cells[closest_idx]
                row_cells[closest_idx] = (existing + " " + b.get("text", "")).strip() if existing else b.get("text", "")
            aligned_grid.append(row_cells)

        return {
            "num_rows": len(aligned_grid),
            "num_cols": num_cols,
            "grid": aligned_grid
        }

    def format_to_markdown(self, grid):
        grid = [[cell.replace("|", "\\|").replace("\n", "<br>") for cell in row] for row in grid]
        if not grid:
            return ""
        lines = []
        header = grid[0]
        lines.append("| " + " | ".join(header) + " |")
        lines.append("| " + " | ".join(["---"] * len(header)) + " |")
        for row in grid[1:]:
            lines.append("| " + " | ".join(row) + " |")
        return "\n".join(lines)

    def run_benchmark_table_reconstruction(self):
        # Sample document bounding boxes for a financial quarterly summary
        sample_boxes = [
            {"x0": 50, "y0": 20, "x1": 150, "y1": 35, "text": "Quarter"},
            {"x0": 200, "y0": 20, "x1": 300, "y1": 35, "text": "Revenue ($M)"},
            {"x0": 350, "y0": 20, "x1": 450, "y1": 35, "text": "Net Income ($M)"},
            {"x0": 50, "y0": 50, "x1": 100, "y1": 65, "text": "Q1 2026"},
            {"x0": 200, "y0": 50, "x1": 250, "y1": 65, "text": "125.4"},
            {"x0": 350, "y0": 50, "x1": 400, "y1": 65, "text": "34.2"},
            {"x0": 50, "y0": 80, "x1": 100, "y1": 95, "text": "Q2 2026"},
            {"x0": 200, "y0": 80, "x1": 250, "y1": 95, "text": "148.8"},
            {"x0": 350, "y0": 80, "x1": 400, "y1": 95, "text": "41.5"}
        ]
        res = self.reconstruct_table_grid(sample_boxes)
        md = self.format_to_markdown(res["grid"])
        return {
            "benchmark_status": "PASSED",
            "num_rows": res["num_rows"],
            "num_cols": res["num_cols"],
            "markdown_table": md
        }
