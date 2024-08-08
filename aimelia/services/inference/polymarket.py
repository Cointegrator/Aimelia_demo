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
    def get_news_by_id(
        event_id: str, question: str, driver, force: Optional[bool] = False
    ):
        service = PolymarketDataService()
        news = service.get_news_by_event_id(event_id, question, driver, force=force)
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

    def generate(
        self, event_id: str, question: str, news, llm, save: Optional[bool] = True
    ):
        local_path = f"./db/verdict-{event_id}.json"

        verdict = llm.get_verdict(question, news)
        verdict = self.post_process_verdict(verdict, question, news)
        if save:
            try:
                with open(local_path, "w") as fp:
                    json.dump(verdict.dict(), fp)
            except Exception:
                pass
        return verdict

    def get_inference(
        self,
        event_id: str,
        question: str,
        driver,
        force: Optional[bool] = False,
    ) -> None:
        try:
            from utils import llm
        except Exception as err:
            print("Exception:", err)
            return {"message": "Inference engine not found!"}

        local_path = f"./db/verdict-{event_id}.json"
        news = self.get_news_by_id(event_id, question, driver)
        print("News from inference node", news)

        if force:
            verdict = self.generate(event_id, question, news, llm)
            # verdict = llm.get_verdict(question, news)
            # verdict = self.post_process_verdict(verdict, question, news)
            # try:
            #     with open(local_path, "w") as fp:
            #         json.dump(verdict.dict(), fp)
            # except Exception:
            #     pass
        else:
            if os.path.exists(local_path):
                try:
                    with open(local_path, "r") as fp:
                        verdict = json.load(fp)
                except Exception:
                    # If problem loading file then generate
                    verdict = self.generate(event_id, question, news, llm)
            else:
                verdict = self.generate(event_id, question, news, llm)
                # verdict = llm.get_verdict(question, news)
                # verdict = self.post_process_verdict(verdict, question, news)
                # try:
                #     with open(local_path, "w") as fp:
                #         json.dump(verdict.dict(), fp)
                # except Exception:
                #     pass

        return verdict
