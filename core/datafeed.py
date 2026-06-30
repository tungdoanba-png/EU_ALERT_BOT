"""
=========================================================
DATA FEED
Twelve Data
=========================================================
"""

import requests
import pandas as pd

from config import (
    API_KEY,
    SYMBOL,
    INTERVAL,
    OUTPUTSIZE
)


class DataFeed:

    BASE_URL = "https://api.twelvedata.com/time_series"

    def __init__(self):

        self.symbol = SYMBOL
        self.interval = INTERVAL
        self.outputsize = OUTPUTSIZE
        self.api_key = API_KEY

    def get_data(self):

        params = {

            "symbol": self.symbol,

            "interval": self.interval,

            "outputsize": self.outputsize,

            "apikey": self.api_key,

            "format": "JSON"

        }

        try:

            response = requests.get(
                self.BASE_URL,
                params=params,
                timeout=15
            )

            data = response.json()

            if "values" not in data:

                print(data)

                return None

            df = pd.DataFrame(data["values"])

            df.rename(
                columns={
                    "datetime": "time"
                },
                inplace=True
            )

            df["time"] = pd.to_datetime(df["time"])

            numeric = [
                "open",
                "high",
                "low",
                "close"
            ]

            for col in numeric:

                df[col] = df[col].astype(float)

            df.sort_values(
                "time",
                inplace=True
            )

            df.reset_index(
                drop=True,
                inplace=True
            )

            return df

        except Exception as ex:

            print(ex)

            return None