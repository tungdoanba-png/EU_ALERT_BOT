"""
=========================================================
EU ALERT BOT V1.0
Author : ChatGPT
Version: 1.0.0
=========================================================
"""

from datetime import datetime
import time

from core.logger import logger
from core.datafeed import DataFeed


class EUAlertBot:

    def __init__(self):

        self.datafeed = DataFeed()

        logger.info("=" * 60)
        logger.info("EU Alert Bot V1.0 Started")
        logger.info("=" * 60)

    def run(self):

        while True:

            try:

                df = self.datafeed.get_data()

                if df is not None:

                    last = df.iloc[-1]

                    logger.info(
                        f"{last['time']} | "
                        f"O:{last['open']} "
                        f"H:{last['high']} "
                        f"L:{last['low']} "
                        f"C:{last['close']}"
                    )

                else:

                    logger.warning("Không lấy được dữ liệu.")

            except Exception as e:

                logger.exception(e)

            time.sleep(10)


if __name__ == "__main__":

    bot = EUAlertBot()

    bot.run()