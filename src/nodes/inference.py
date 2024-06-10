"""
Inference Node
~~~~~~~~~~~~~~~

Players employ inference nodes to make decisions. They can deposit
the money to the inference nodes and delegate the work entirely
to inference nodes to make decisions.

Function:

AI or humans draw conclusions from gathered knowledge
( which can be auditable on-chain) and learn from each other's
decision-making processes. Inference nodes are for
players to make better decisions.
"""

from src.config import configs
from src.nodes.base import Node
from src.nodes.data import DataNode
from src.utils import utility

import os
import json
from typing import Optional, List, Literal

from dotenv import load_dotenv
from py_clob_client.clob_types import OrderArgs, OrderType
from py_clob_client.order_builder.constants import BUY, SELL
from py_clob_client.client import ClobClient, ApiCreds
from py_clob_client.constants import AMOY
from fastapi import HTTPException, status
from transformers import pipeline
from pydantic import BaseModel

load_dotenv()


class Verdict(BaseModel):
    decision: Literal["BUY-YES", "BUY-NO", "HOLD", "SELL-YES", "SELL-NO"]
    avg_positive_score: Optional[float]
    avg_negative_score: Optional[float]
    condition_id: str
    question: str
    news_and_sentiment: List[dict]
    tags: List[str]


class InferenceNode(Node):
    """
    Compiles all the document together
    to allow users / bots to make informed decisions
    """

    @staticmethod
    def form_verdict(
        decision: str,
        condition_id: str,
        question: List[str],
        news_and_sentiment: List[dict],
        tags: List[str],
        avg_positive_score: Optional[float] = None,
        avg_negative_score: Optional[float] = None,
    ) -> Verdict:
        return Verdict(
            decision=decision,
            avg_positive_score=avg_positive_score,
            avg_negative_score=avg_negative_score,
            condition_id=condition_id,
            question=question,
            news_and_sentiment=news_and_sentiment,
            tags=tags,
        )

    def __init__(self) -> None:
        self.client = ClobClient(configs.AUTH_BASE, key=os.getenv("PK"), chain_id=AMOY)
        self.pipeline = pipeline("sentiment-analysis")

    def get_info(self, condition_id: str) -> dict:
        event = DataNode().get_event_by_condition_id(condition_id)
        if not event:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Event not found"
            )

        news = DataNode().get_relevant_news(condition_id)

        # Compute the sentiment of the news
        sentiments = self.pipeline(news)

        news_with_sentiments = []
        for n, sent in zip(news, sentiments):
            news_with_sentiments.append({"news": n, "sentiment": sent})

        # Save the computed sentiment value locally
        with open(f"./data/{condition_id}/sentiments.json", "w") as f:
            utility.log(f"Writing sentiments to ./data/{condition_id}/sentiments.json")
            json.dump(news_with_sentiments, f)

        return {"news": news_with_sentiments, "event": event}

    def infer_and_participate(self, condition_id: str) -> dict:
        """
        Helps draw inference from the gathered knowledge.
        """
        event = DataNode().get_event_by_condition_id(condition_id)
        if not event:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Event not found"
            )

        # Try and fetch the sentiments for this event
        if os.path.exists(f"./data/{condition_id}/sentiments.json"):
            with open(f"./data/{condition_id}/sentiments.json", "r") as f:
                sentiments = json.load(f)
        else:
            # This process will sure compute the sentiments
            r = self.get_info(condition_id)
            sentiments = r["news"]

        # Perform the inference
        positive_count = 0
        positive_score = []

        negative_count = 0
        negative_score = []

        for sentiment in sentiments:
            if sentiment["sentiment"]["label"] == "POSITIVE":
                positive_count += 1
                positive_score.append(sentiment["sentiment"]["score"])
            elif sentiment["sentiment"]["label"] == "NEGATIVE":
                negative_count += 1
                negative_score.append(sentiment["sentiment"]["score"])
            else:
                pass

        utility.log(f"Positive count: {positive_count}")
        avg_positive_score = (
            sum(positive_score) / positive_count if positive_count > 0 else 0
        )
        utility.log(f"Avg. Positive score: {avg_positive_score}")

        utility.log(f"Negative count: {negative_count}")
        avg_negative_score = (
            sum(negative_score) / negative_count if negative_count > 0 else 0
        )
        utility.log(f"Avg. Negative score: {avg_negative_score}")

        if configs.AUTO_BUY:
            try:
                token_id = event["tokens"][0]["token_id"]
            except Exception as err:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err)
                )
            else:
                l2 = self.client.derive_api_key()
                self.client = ClobClient(
                    configs.AUTH_BASE, key=os.getenv("PK"), chain_id=AMOY, creds=l2
                )

                # Perform the buy or sell
                order_args = OrderArgs(
                    price=0.50,
                    size=1,
                    side=BUY,
                    token_id=token_id,
                )
                signed_order = self.client.create_order(order_args)
                resp = self.client.post_order(signed_order, OrderType.GTC)
                print(resp)
                return resp

        if positive_count > negative_count:
            return self.form_verdict(
                decision="BUY-YES",
                avg_positive_score=avg_positive_score,
                avg_negative_score=avg_negative_score,
                condition_id=condition_id,
                question=event["question"],
                news_and_sentiment=sentiments,
                tags=event["tags"],
            )
        elif positive_count < negative_count:
            return self.form_verdict(
                decision="BUY-NO",
                avg_positive_score=avg_positive_score,
                avg_negative_score=avg_negative_score,
                condition_id=condition_id,
                question=event["question"],
                news_and_sentiment=sentiments,
                tags=event["tags"],
            )
        else:
            return self.form_verdict(
                decision="BUY-NO",
                avg_positive_score=avg_positive_score,
                avg_negative_score=avg_negative_score,
                condition_id=condition_id,
                question=event["question"],
                news_and_sentiment=sentiments,
                tags=event["tags"],
            )
