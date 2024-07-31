import os
import json
from configs import config
from services.data.base import BaseDataService
from utils import gnews
from typing import Optional


class PolymarketDataService(BaseDataService):
    def __init__(self) -> None:
        pass

    def get_all_events(self):
        url = f"{config.POLYMARKET_BASE_URL}/markets"
        r = self.get(url)
        return json.loads(r.content)

    def get_event_by_id(self, event_id: str):
        url = f"{config.POLYMARKET_BASE_URL}/markets/{event_id}"
        r = self.get(url)
        return json.loads(r.content)

    def get_news_by_event_id(
        self,
        event_id: str,
        question: str,
        fetch_content: Optional[bool] = True,
        n: Optional[int] = 5,
        force: Optional[bool] = False,
    ):
        # Check locally first
        local_path = f"./db/news-{event_id}.json"

        if force:
            news = gnews.get_news(question, fetch_content=fetch_content, n=n)
            with open(local_path, "w") as fp:
                json.dump(news, fp)

        else:
            if os.path.exists(local_path):
                with open(local_path, "r") as fp:
                    news = json.load(fp)
            else:
                news = gnews.get_news(question, fetch_content=fetch_content, n=n)

                with open(local_path, "w") as fp:
                    json.dump(news, fp)

        return news
