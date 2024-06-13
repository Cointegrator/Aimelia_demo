"""
Data node
~~~~~~~~~~

Creators, players, and validators can all select data nodes
to provide real-time information to support decisions. Data nodes
can directly work as information source to support each party
make decisions as well.

Function:

AI or institutions that actively collect and reuse 
information to provide evidence for inference node
to make decisions
"""

import os
import json
from typing import Optional, List, Any

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


# from src.nodes.base import Node
import configs
import utility

# from src.config import configs
# from src.utils import utility

load_dotenv()


class Node:
    """
    Base node for the project.
    Every other node in the architecture will inherit from this class.
    """

    def __init__(self) -> None:
        pass

    def get(self, url, headers: Optional[dict] = None) -> None:
        return requests.get(url, headers=headers)

    def post(
        self, url: str, headers: Optional[dict] = None, data: Optional[Any] = None
    ) -> None:
        return requests.post(url, headers=headers, data=data)


class DataNode(Node):
    """
    Service class for the data node operations
    """

    def __init__(self) -> None:
        pass

    def get_all_events_data(self):
        url = f"{configs.BASE}/markets"
        r = self.get(url)
        return json.loads(r.content)

    def get_event_by_condition_id(
        self, condition_id: str, cache: Optional[bool] = configs.CACHE
    ):
        if os.path.exists(f"./data/{condition_id}/event.json"):
            with open(f"./data/{condition_id}/event.json", "r") as f:
                utility.log(f"Using locally saved event data for {condition_id}")
                return json.load(f)

        url = f"{configs.BASE}/markets/{condition_id}"
        r = self.get(url)

        if cache:
            if not os.path.exists(f"./data/{condition_id}"):
                utility.log(
                    f"Creating a new directory for the condition_id: {condition_id}"
                )
                os.makedirs(f"./data/{condition_id}")

            if r.status_code == 200:
                with open(f"./data/{condition_id}/event.json", "w") as f:
                    utility.log(
                        f"Saving event data for the condition_id: {condition_id}"
                    )
                    json.dump(json.loads(r.content), f)

        return json.loads(r.content)

    @staticmethod
    def scrape_news(event):
        search_url = f"https://news.google.com/search?q={event}"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all("article")
        ws = [article.text for article in articles]
        return ws

    def get_relevant_news(self, condition_id: str) -> List[str]:
        """
        Get relevant news from the inference node
        """
        # If data is there then use the prefetched data
        if os.path.exists(f"./data/{condition_id}/news.json"):
            utility.log(
                f"Using locally saved news data for the condition_id: {condition_id}"
            )
            with open(f"./data/{condition_id}/news.json", "r") as f:
                news = json.load(f)
            return news

        else:
            if not os.path.exists(f"./data/{condition_id}/event.json"):
                utility.log(
                    f"Found no event data for the condition_id: {condition_id}. Fetching from the server"
                )
                event = self.get_event_by_condition_id(condition_id)
            else:
                # Use locally saved event data
                utility.log(
                    f"Using locally saved event data for the condition_id: {condition_id}"
                )
                with open(f"./data/{condition_id}/event.json", "r") as f:
                    event = json.load(f)

            news = []
            news.extend(self.scrape_news(event["question"]))

            if news:
                utility.log(f"Saving news data for the condition_id: {condition_id}")
                with open(f"./data/{condition_id}/news.json", "w") as f:
                    json.dump(news, f)

            return news
