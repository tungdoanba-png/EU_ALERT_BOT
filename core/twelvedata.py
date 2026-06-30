# core/twelvedata.py

import requests
import pandas as pd

from config import (
    API_KEY,
    SYMBOL,
    INTERVAL,
    OUTPUTSIZE
)

from core.data_provider import DataProvider


class TwelveData(DataProvider):

    BASE_URL = "https://api.twelvedata.com/time_series"

    def __init__(self):

        self.connected = False

    def get_data(self):

        params = {

            "symbol": SYMBOL,

            "interval": INTERVAL,

            "outputsize": OUTPUTSIZE,

            "apikey": API_KEY,

            "format": "JSON"

        }

        try:

            r = requests.get(
                self.BASE_URL,
                params=params,
                timeout=20
            )

            r.raise_for_status()

            data = r.json()

            if "values" not in data:

                self.connected = False

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

            for c in numeric:

                df[c] = df[c].astype(float)

            if "volume" in df.columns:

                df["volume"] = df["volume"].astype(float)

            else:

                df["volume"] = 0

            df.sort_values(
                "time",
                inplace=True
            )

            df.reset_index(
                drop=True,
                inplace=True
            )

            self.connected = True

            return df

        except Exception:

            self.connected = False

            return None

    def is_connected(self):

        return self.connected

    def reconnect(self):

        return self.get_data() is not None