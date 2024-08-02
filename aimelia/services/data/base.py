from abc import abstractmethod, ABCMeta
from typing import Any, Optional
import requests
import os


class BaseDataService(metaclass=ABCMeta):
    def __init__(self) -> None:
        # If no db directory create
        if not os.path.exists("./db"):
            print("Creating db directory")
            os.makedirs("./db")

    def get(self, url, headers: Optional[dict] = None) -> None:
        return requests.get(url, headers=headers)

    @abstractmethod
    def get_all_events(self) -> Any:
        pass

    @abstractmethod
    def get_event_by_id(self, event_id: str) -> Any:
        pass
