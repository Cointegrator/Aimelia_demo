from fastapi import APIRouter

from src.nodes.inference import InferenceNode

router = APIRouter(prefix="/inference", tags=["Inference Node"])


@router.get("/{condition_id}")
async def get_market_inferential_data(condition_id: str):
    """
    Given the condition_id (Unique identifier of an event in **Polymarket**), this endpoint returns the inferential
    insights (if any exists) for the given `condition_id`, currently provides the following insights

    * News associated with the event question
    * Market information
    * Sentiment analysis result of the procured news
    """
    return InferenceNode().get_info(condition_id=condition_id)


@router.get("/{condition_id}/infer")
async def infer_and_participate(condition_id: str):
    """
    Helps draw inference from the gathered knowledge.
    Returns a verdict object of the following schema

    ```python
    class Verdict(BaseModel):
        decision: Literal["BUY-YES", "BUY-NO", "HOLD", "SELL-YES", "SELL-NO"]
        avg_positive_score: Optional[float]
        avg_negative_score: Optional[float]
        condition_id: str
        question: str
        news_and_sentiment: List[dict]
        tags: List[str]

    ```
    """
    return InferenceNode().infer_and_participate(condition_id=condition_id)
