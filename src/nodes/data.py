"""
Data node

Creators, players, and validators can all select data nodes
to provide real-time information to support decisions. Data nodes
can directly work as information source to support each party
make decisions as well.

Function:

AI or institutions that actively collect and reuse 
information to provide evidence for inference node
to make decisions
"""
import json

import requests
from bs4 import BeautifulSoup

from src.nodes.base import Node
from src.config import configs


class DataNode(Node):
    """
    Service class for the data node operations
    """

    def __init__(self) -> None:
        pass

    def get_all_events_data(self):
        url = f'{configs.BASE}/markets'
        r = self.get(url)
        return json.loads(r.content)

    def get_event_by_condition_id(self, condition_id: str):
        url = f'{configs.BASE}/markets/{condition_id}'
        r = self.get(url)
        return json.loads(r.content)
    

    @staticmethod
    def scrape_news(event):
        search_url = f"https://news.google.com/search?q={event}"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        ws = [article.text for article in articles]
        return ws

    def get_relevant_news(self, question: str, tags: Optional[List[str]] = None) -> List[str]:
        """
        Get relevant news from the inference node
        """
        news = []
        news.extend(self.scrape_news(question))
        if isinstance(tags, list):
            for tag in tags:
                news.extend(self.   scrape_news(tag))
        return list(set(news))
    
