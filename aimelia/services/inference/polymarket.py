import json
import os
from configs import config
from services.inference.base import BaseInferenceService
from services.data.polymarket import PolymarketDataService
from typing import List, Any, Optional


class PolymarketInferenceService(BaseInferenceService):
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_news_by_id(event_id: str, question: str, force: Optional[bool] = False):
        service = PolymarketDataService()
        news = service.get_news_by_event_id(event_id, question, force=force)
        return news

    @staticmethod
    def post_process_verdict(verdict, question, news):
        try:
            x = verdict.dict()
            x["question"] = question
            x["news"] = news
        except Exception:
            return verdict
        else:
            return x

    def get_inference(
        self,
        event_id: str,
        question: str,
        force: Optional[bool] = False,
    ) -> None:
        try:
            from utils import llm
        except Exception:
            return {"message": "Inference engine not found!"}

        local_path = f"./db/verdict-{event_id}.json"
        news = self.get_news_by_id(event_id, question)
        print("News from inference node", news)

        if force:
            verdict = llm.get_verdict(question, news)
            verdict = self.post_process_verdict(verdict, question, news)
            try:
                with open(local_path, "w") as fp:
                    json.dump(verdict.dict(), fp)
            except Exception:
                pass
        else:
            if os.path.exists(local_path):
                with open(local_path, "r") as fp:
                    verdict = json.load(fp)
            else:
                verdict = llm.get_verdict(question, news)
                verdict = self.post_process_verdict(verdict, question, news)
                try:
                    with open(local_path, "w") as fp:
                        json.dump(verdict.dict(), fp)
                except Exception:
                    pass

        return verdict
