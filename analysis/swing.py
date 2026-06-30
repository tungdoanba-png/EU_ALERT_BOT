import pandas as pd


class SwingEngine:

    def __init__(self, df, left=3, right=3):

        self.df = df.copy()

        self.left = left

        self.right = right

    def find_swings(self):

        swing_high = []

        swing_low = []

        highs = self.df["high"].values

        lows = self.df["low"].values

        for i in range(self.left, len(self.df)-self.right):

            high = highs[i]

            low = lows[i]

            if high == max(highs[i-self.left:i+self.right+1]):

                swing_high.append(i)

            if low == min(lows[i-self.left:i+self.right+1]):

                swing_low.append(i)

        return swing_high, swing_low

    def get_swing_dataframe(self):

        sh, sl = self.find_swings()

        data = []

        for i in sh:

            data.append({

                "index": i,

                "time": self.df.iloc[i]["time"],

                "price": self.df.iloc[i]["high"],

                "type": "SH"

            })

        for i in sl:

            data.append({

                "index": i,

                "time": self.df.iloc[i]["time"],

                "price": self.df.iloc[i]["low"],

                "type": "SL"

            })

        result = pd.DataFrame(data)

        result.sort_values("index", inplace=True)

        result.reset_index(drop=True, inplace=True)

        return result