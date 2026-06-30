from abc import ABC, abstractmethod
import pandas as pd


class DataProvider(ABC):
    """
    Interface cho tất cả nguồn dữ liệu.
    Mọi module phân tích chỉ làm việc với DataProvider.
    """

    @abstractmethod
    def get_data(self) -> pd.DataFrame:
        """
        Trả về DataFrame chuẩn gồm:

        time
        open
        high
        low
        close
        volume
        """
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        """
        Kiểm tra kết nối tới nguồn dữ liệu.
        """
        pass

    @abstractmethod
    def reconnect(self):
        """
        Thử kết nối lại khi mất kết nối.
        """
        pass