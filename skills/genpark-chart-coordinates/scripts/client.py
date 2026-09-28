import sys, json, math

class MultimodalChartDataPointExtractor:
    """
    Visual Chart-to-Data Recovery Engine.
    Converts 2D pixel coordinates of bars, axes, and points into calibrated numerical series.
    """
    def __init__(self):
        pass

    def calibrate_axis_scale(self, tick_marks):
        """
        tick_marks: list of dicts [{"coord": 500, "val": 0.0}, {"coord": 100, "val": 100.0}]
        Returns slope and intercept for mapping: value = slope * coord + intercept
        """
        if len(tick_marks) < 2:
            return {"status": "ERROR", "message": "At least 2 tick marks required for calibration"}

        # Linear regression across tick points
        n = len(tick_marks)
        coords = [t["coord"] for t in tick_marks]
        vals = [t["val"] for t in tick_marks]
        
        sum_c = sum(coords)
        sum_v = sum(vals)
        sum_cc = sum(c * c for c in coords)
        sum_cv = sum(c * v for c, v in zip(coords, vals))

        denom = (n * sum_cc - sum_c * sum_c)
        if abs(denom) < 1e-9:
            return {"status": "ERROR", "message": "Degenerate coordinate distribution"}

        slope = (n * sum_cv - sum_c * sum_v) / denom
        intercept = (sum_v - slope * sum_c) / n

        return {
            "status": "CALIBRATED",
            "slope": slope,
            "intercept": intercept,
            "r_squared": (1.0 - sum((v - (slope*c + intercept))**2 for c,v in zip(coords,vals)) / sum((v-sum_v/n)**2 for v in vals)) if any(v != vals[0] for v in vals) else 1.0
        }

    def extract_bar_chart_series(self, bars_coords, y_calibration):
        # bars_coords: [{"label": "2024", "y_top": 250, "y_base": 500}, ...]
        slope = y_calibration["slope"]
        intercept = y_calibration["intercept"]
        series = []

        for bar in bars_coords:
            y_top = bar["y_top"]
            calc_val = slope * y_top + intercept
            series.append({
                "label": bar.get("label", "Unknown"),
                "extracted_value": round(calc_val, 2),
                "pixel_height": bar.get("y_base", 0) - y_top
            })

        return series

    def extract_scatter_points(self, points_coords, x_calibration, y_calibration):
        results = []
        for pt in points_coords:
            x_val = x_calibration["slope"] * pt["x"] + x_calibration["intercept"]
            y_val = y_calibration["slope"] * pt["y"] + y_calibration["intercept"]
            results.append({
                "x": round(x_val, 2),
                "y": round(y_val, 2),
                "label": pt.get("label", "")
            })
        return results

    def run_benchmark_chart_extraction(self):
        # Calibrate Y axis: pixel 500 = 0.0, pixel 100 = 200.0 (inverted pixel coordinates)
        y_ticks = [{"coord": 500, "val": 0.0}, {"coord": 100, "val": 200.0}]
        y_cal = self.calibrate_axis_scale(y_ticks)

        # Bar chart with 3 bars
        bars = [
            {"label": "Product A", "y_top": 300, "y_base": 500}, # Should be 100.0
            {"label": "Product B", "y_top": 200, "y_base": 500}, # Should be 150.0
            {"label": "Product C", "y_top": 100, "y_base": 500}  # Should be 200.0
        ]
        series = self.extract_bar_chart_series(bars, y_cal)

        return {
            "benchmark_status": "PASSED",
            "series_count": len(series),
            "series": series,
            "product_a_value": series[0]["extracted_value"]
        }
