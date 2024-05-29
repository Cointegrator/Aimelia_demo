import requests
from typing import Optional, Any

class Node:

    def __init__(self) -> None:
        pass

    def get(self, url, headers: Optional[dict] = None) -> None:
        return requests.get(url, headers=headers)

    def post(self, url: str, headers: Optional[dict] = None, data: Optional[Any] = None) -> None:
        return requests.post(url, headers=headers, data=data)
    