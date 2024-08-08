from datetime import datetime

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
import base64
import requests
from urllib import parse
from bs4 import BeautifulSoup
from selenium import webdriver


from typing import Optional


def fetch_news_content(url: str) -> None:
    markup = requests.get(url, timeout=(3, 8)).text
    soup = BeautifulSoup(markup, "html.parser")
    content = []
    paragraphs = soup.find_all("p")

    for paragraph in paragraphs:
        content.append(paragraph.text)

    if not content:
        return None
    else:
        return " ".join([str(elem).strip() for elem in content])


def fetch_news_content_v2(driver, url: str) -> None:
    markup = None
    try:
        driver.get(url)
        # Wait till html is loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "html"))
        )
        time.sleep(2)
        driver_uri = driver.current_url
        if not driver_uri.startswith("https://news.google.com"):
            print("Driver URI", driver_uri)
            markup = driver.page_source
    except Exception as err:
        print("Exception while fetching content v2", err)
    else:
        if not markup:
            print("[INFO] No markup found!")
            return None
        else:
            print("Markup found!")
            soup = BeautifulSoup(markup, "html.parser")
            paragraphs = soup.find_all("p")
            content = []
            for paragraph in paragraphs:
                content.append(paragraph.text)
            text = " ".join([str(elem).strip() for elem in content])
            print(f"Text extracted: {text[:200]}...")
            return text


def get_decoded_source_url(url: str) -> str:
    encoded_string = url.split("read/")[-1].split("?")[0]
    encoded_string = encoded_string + "=="
    # encoded_string = encoded_string[4:] + "=="

    decoded_string = base64.b64decode(encoded_string)
    string = decoded_string.decode(json.detect_encoding(decoded_string), "ignore")
    decoded_url = "http" + string.split("http")[-1]
    decoded_url = str(decoded_url)[:-2]
    return decoded_url.strip()


def get_decoded_image_url(url: str) -> str:
    try:
        r = requests.get(url)
    except Exception:
        return "https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png"
    else:
        return r.url


def get_google_url(endpoint: str) -> str:
    return "https://news.google.com" + endpoint


def parse_datetime(dt_str: str) -> str:
    return datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%SZ")


def get_google_news_url(keyword: str) -> str:
    """
    Creates google news url from text using url encoding
    """
    params = {"q": keyword, "hl": "en-US"}
    query_params = parse.urlencode(params)
    return "https://news.google.com/search?" + query_params


def fetch_markup(url: str):
    r = requests.get(url)
    markup = r.text
    return markup


def parse_markup(
    markup: str,
    driver: webdriver.Chrome,
    verbose: Optional[bool] = False,
    n: Optional[int] = None,
    fetch_content: Optional[bool] = False,
):
    print("Fetch content:", fetch_content)
    if not n:
        n = 10

    soup = BeautifulSoup(markup, "html.parser")
    anchors = soup.find_all("a")

    data = []
    count = 0

    for anchor in anchors:
        try:
            href = anchor["href"]
        except Exception as err:
            print("Exception while fetching href", err)
            continue

        if not href.startswith("./read"):
            continue

        if not anchor.text:
            continue

        main = anchor.parent.parent.parent
        try:
            thumb = main.find("figure").find("img")["src"]
            thumb = get_google_url(thumb)
        except Exception as err:
            thumb = None
            print("Exception while fetching thumb", err)

        # Publisher
        # main = anchor.parent.parent.parent
        second_div = main.find_all("div")[1]
        try:
            publisher = second_div.find("div").find("div").find("div").find("div").text
        except Exception as err:
            publisher = None
            print("Exception while fetching publisher", err)

        # Published at
        try:
            x = main.parent
            published_at = x.find("time")["datetime"]
        except Exception as err:
            published_at = None
            print("Exception while fetching published_at", err)
        else:
            if published_at:
                # If published_at is greater than today then only keep
                cur_time = datetime.now()
                today = datetime(cur_time.year, cur_time.month, cur_time.day)
                _published_at = parse_datetime(published_at)

        # URL
        try:
            url = f"https://news.google.com{href[1:]}"
        except Exception as err:
            print("Exception while fetching url", err)

        # Decoded url
        try:
            decoded_url = get_decoded_source_url(href)
        except Exception as err:
            print("Exception while fetching decoded_url", err)
            continue

        if verbose:
            print(f"Headline: {anchor.text[:50]}...")
            print(f"Publisher: {publisher}")

        # Content
        content = None
        if fetch_content:
            try:
                if verbose:
                    print("\tAttempting to fetch content...")
                # content = fetch_news_content(decoded_url)
                content = fetch_news_content_v2(driver, url)
            except Exception as err:
                print("Exception while reading content", err)
                if verbose:
                    print("\tFailed to fetch content...")
            else:
                if content:
                    print(f"Content fetched: {content[:200]}...")

        data.append(
            {
                "headline": anchor.text,
                "url": url,
                "decoded_url": decoded_url,
                "publisher": publisher,
                "thumb": thumb,
                "decoded_image_url": get_decoded_image_url(thumb),
                "content": content,
                "published_at": published_at,
            }
        )

        if n:
            count += 1
            if count == n:
                break

    return data


def get_news(
    keyword: str,
    driver: webdriver.Chrome,
    verbose: Optional[bool] = True,
    n: Optional[int] = None,
    fetch_content: Optional[bool] = False,
):
    print("Keyword:", keyword)
    url = get_google_news_url(keyword=keyword)
    if verbose:
        print("URL:", url)
    markup = requests.get(url).text
    data = parse_markup(
        markup, driver=driver, verbose=verbose, n=n, fetch_content=fetch_content
    )
    return data
