from abc import abstractmethod, ABCMeta
from typing import Any, Optional
import requests


class BaseInferenceService(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    def get(self, url, headers: Optional[dict] = None) -> None:
        return requests.get(url, headers=headers)

    @abstractmethod
    def get_inference(self) -> None:
        pass
