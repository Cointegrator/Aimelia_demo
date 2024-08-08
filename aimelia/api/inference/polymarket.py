from fastapi import APIRouter
from typing import List, Any, Optional
from services.inference.polymarket import PolymarketInferenceService

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.page_load_strategy = "eager"

chrome_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
print("Driver instantiated (Data node) ::", driver)

router = APIRouter(prefix="/polymarket", tags=["Polymarket"])

from pydantic import BaseModel


class InferenceRequest(BaseModel):
    event_id: str
    question: str
    force: Optional[bool] = False


@router.post("/infer")
def infer_polymarket_event_by_id(body: InferenceRequest):
    service = PolymarketInferenceService()
    result = service.get_inference(
        body.event_id, body.question, force=body.force, driver=driver
    )
    return result
