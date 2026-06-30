"""
=========================================================
KEY LEVEL ENGINE
=========================================================
"""

import pandas as pd


class KeyLevel:

    def __init__(self, df: pd.DataFrame):

        self.df = df.copy()

        self.df["time"] = pd.to_datetime(self.df["time"])

        self.df.set_index("time", inplace=True)

    # ==========================================
    # Previous Day High / Low
    # ==========================================

    def previous_day(self):

        daily = self.df.resample("D").agg({

            "high": "max",

            "low": "min"

        })

        if len(daily) < 2:

            return None

        return {

            "PDH": float(daily.iloc[-2]["high"]),

            "PDL": float(daily.iloc[-2]["low"])

        }

    # ==========================================
    # Previous Week High / Low
    # ==========================================

    def previous_week(self):

        weekly = self.df.resample("W-MON").agg({

            "high": "max",

            "low": "min"

        })

        if len(weekly) < 2:

            return None

        return {

            "PWH": float(weekly.iloc[-2]["high"]),

            "PWL": float(weekly.iloc[-2]["low"])

        }

    # ==========================================
    # Equal High
    # ==========================================

    def equal_high(self, tolerance=0.00010):

        highs = self.df["high"].values

        result = []

        for i in range(1, len(highs)):

            if abs(highs[i] - highs[i-1]) <= tolerance:

                result.append(highs[i])

        return result

    # ==========================================
    # Equal Low
    # ==========================================

    def equal_low(self, tolerance=0.00010):

        lows = self.df["low"].values

        result = []

        for i in range(1, len(lows)):

            if abs(lows[i] - lows[i-1]) <= tolerance:

                result.append(lows[i])

        return result

    # ==========================================
    # Old High
    # ==========================================

    def old_high(self):

        return float(self.df["high"].max())

    # ==========================================
    # Old Low
    # ==========================================

    def old_low(self):

        return float(self.df["low"].min())

    # ==========================================
    # All Levels
    # ==========================================

    def get_all(self):

        return {

            **self.previous_day(),

            **self.previous_week(),

            "EQH": self.equal_high(),

            "EQL": self.equal_low(),

            "OLD_HIGH": self.old_high(),

            "OLD_LOW": self.old_low()

        }