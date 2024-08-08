from fastapi import APIRouter
from services.data.polymarket import PolymarketDataService
from typing import Optional

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


class NewsRequest(BaseModel):
    event_id: str
    question: str
    fetch_content: Optional[bool] = True
    num: Optional[int] = 5
    force: Optional[bool] = False


@router.get("/events")
def get_all_polymarket_events():
    service = PolymarketDataService()
    return service.get_all_events()


@router.get("/events/{event_id}")
def get_polymarket_event_by_id(event_id: str):
    service = PolymarketDataService()
    return service.get_event_by_id(event_id)


@router.post("/news")
def get_news_by_polymarket_event_id(body: NewsRequest):
    service = PolymarketDataService()
    return service.get_news_by_event_id(
        body.event_id,
        body.question,
        driver=driver,
        fetch_content=body.fetch_content,
        n=body.num,
        force=body.force,
    )
