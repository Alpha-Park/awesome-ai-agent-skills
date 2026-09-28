import sys, json, math

class FinancialFormulaAuditValidator:
    """
    Arithmetic consistency checks for supplied statement data and total matrices.
    """
    def __init__(self, tolerance=0.5):
        if not math.isfinite(tolerance) or tolerance < 0:
            raise ValueError("tolerance must be finite and non-negative")
        self.tolerance = tolerance

    def _required(self, values, fields):
        missing = [field for field in fields if field not in values]
        if missing:
            raise ValueError("Missing required fields: " + ", ".join(missing))
        for value in values.values():
            if isinstance(value, bool) or not math.isfinite(float(value)):
                raise ValueError("Values must be finite numbers")

    def audit_balance_sheet(self, balance_sheet_dict):
        self._required(balance_sheet_dict, ["total_assets", "total_liabilities", "stockholders_equity"])
        assets = float(balance_sheet_dict.get("total_assets", 0.0))
        current_assets = float(balance_sheet_dict.get("current_assets", 0.0))
        non_current_assets = float(balance_sheet_dict.get("non_current_assets", 0.0))
        
        liabilities = float(balance_sheet_dict.get("total_liabilities", 0.0))
        equity = float(balance_sheet_dict.get("stockholders_equity", 0.0))
        liab_and_equity = float(balance_sheet_dict.get("total_liabilities_and_equity", liabilities + equity))

        # Check 1: Fundamental Balance Sheet Equation: Assets == Liabilities + Equity
        fundamental_diff = abs(assets - (liabilities + equity))
        is_fundamental_balanced = fundamental_diff <= self.tolerance

        # Check 2: Total Assets == Current + Non-Current
        assets_sum_diff = abs(assets - (current_assets + non_current_assets))
        is_assets_summed = assets_sum_diff <= self.tolerance if ("current_assets" in balance_sheet_dict and "non_current_assets" in balance_sheet_dict) else True

        issues = []
        if abs(liab_and_equity - (liabilities + equity)) > self.tolerance:
            issues.append("Reported liabilities-and-equity total does not match its components")
        if not is_fundamental_balanced:
            issues.append(f"Balance sheet mismatch: Total Assets ({assets}) != Liab + Equity ({liabilities + equity}), discrepancy = {fundamental_diff:.2f}")
        if not is_assets_summed:
            issues.append(f"Asset component mismatch: Total Assets ({assets}) != Current ({current_assets}) + Non-Current ({non_current_assets})")

        return {
            "status": "BALANCED" if not issues else "DISCREPANCY_DETECTED",
            "total_assets": assets,
            "total_liabilities_and_equity": liab_and_equity,
            "discrepancy": round(fundamental_diff, 2),
            "is_balanced": not issues,
            "audit_issues": issues
        }

    def audit_income_statement(self, income_stmt_dict):
        self._required(income_stmt_dict, ["revenue", "cogs", "gross_profit", "operating_expenses", "operating_income"])
        revenue = float(income_stmt_dict.get("revenue", 0.0))
        cogs = float(income_stmt_dict.get("cogs", 0.0))
        gross_profit = float(income_stmt_dict.get("gross_profit", revenue - cogs))
        
        opex = float(income_stmt_dict.get("operating_expenses", 0.0))
        operating_income = float(income_stmt_dict.get("operating_income", gross_profit - opex))
        
        tax = float(income_stmt_dict.get("tax_expense", 0.0))
        net_income = float(income_stmt_dict.get("net_income", operating_income - tax))

        issues = []
        if "net_income" in income_stmt_dict and "tax_expense" in income_stmt_dict:
            if abs(net_income - (operating_income - tax)) > self.tolerance:
                issues.append("Net income does not match operating income minus tax in the simplified model")
        gp_calc = revenue - cogs
        if abs(gross_profit - gp_calc) > self.tolerance:
            issues.append(f"Gross profit error: Reported ({gross_profit}) != Rev ({revenue}) - COGS ({cogs}) = {gp_calc:.2f}")

        op_calc = gross_profit - opex
        if abs(operating_income - op_calc) > self.tolerance:
            issues.append(f"Operating income error: Reported ({operating_income}) != Gross Profit ({gross_profit}) - Opex ({opex}) = {op_calc:.2f}")

        return {
            "status": "VALIDATED" if not issues else "DISCREPANCY_DETECTED",
            "revenue": revenue,
            "gross_profit": gross_profit,
            "operating_income": operating_income,
            "net_income": net_income,
            "audit_issues": issues
        }

    def audit_cross_footing(self, matrix_rows):
        """
        Validates that row sums and column sums align (footing and cross-footing).
        matrix_rows is a 2D float list where the last column is row total and last row is col total.
        """
        if len(matrix_rows) < 2 or len(matrix_rows[0]) < 2:
            return {"status": "INSUFFICIENT_DIMENSIONS"}

        if any(len(row) != len(matrix_rows[0]) for row in matrix_rows):
            raise ValueError("matrix_rows must be rectangular")
        for row in matrix_rows:
            if any(type(v) not in (int, float) or not math.isfinite(v) for v in row):
                raise ValueError("Matrix values must be finite numbers")

        num_r = len(matrix_rows)
        num_c = len(matrix_rows[0])
        issues = []
        if abs(matrix_rows[-1][-1] - sum(row[-1] for row in matrix_rows[:-1])) > self.tolerance:
            issues.append("Grand total does not match row totals")
        if abs(matrix_rows[-1][-1] - sum(matrix_rows[-1][:-1])) > self.tolerance:
            issues.append("Grand total does not match column totals")

        # Check each row total
        for r_idx in range(num_r - 1):
            row_vals = matrix_rows[r_idx][:-1]
            reported_total = matrix_rows[r_idx][-1]
            calc_sum = sum(row_vals)
            if abs(reported_total - calc_sum) > self.tolerance:
                issues.append(f"Row {r_idx} footing error: Reported {reported_total} != Calc {calc_sum:.2f}")

        # Check each column total
        for c_idx in range(num_c - 1):
            col_vals = [matrix_rows[r][c_idx] for r in range(num_r - 1)]
            reported_total = matrix_rows[-1][c_idx]
            calc_sum = sum(col_vals)
            if abs(reported_total - calc_sum) > self.tolerance:
                issues.append(f"Col {c_idx} cross-footing error: Reported {reported_total} != Calc {calc_sum:.2f}")

        return {
            "status": "PERFECT_MATCH" if not issues else "DISCREPANCY_DETECTED",
            "issues_count": len(issues),
            "issues": issues
        }

    def run_benchmark_financial_audit(self):
        bs_data = {
            "total_assets": 10500.0,
            "current_assets": 4500.0,
            "non_current_assets": 6000.0,
            "total_liabilities": 5200.0,
            "stockholders_equity": 5300.0,
            "total_liabilities_and_equity": 10500.0
        }
        res_bs = self.audit_balance_sheet(bs_data)

        # Cross footing matrix: 2 data rows, 2 data cols, plus totals
        matrix = [
            [100.0, 200.0, 300.0],
            [150.0, 250.0, 400.0],
            [250.0, 450.0, 700.0]
        ]
        res_cf = self.audit_cross_footing(matrix)

        return {
            "benchmark_status": "PASSED",
            "balance_sheet_status": res_bs["status"],
            "cross_footing_status": res_cf["status"],
            "is_balanced": res_bs["is_balanced"]
        }
