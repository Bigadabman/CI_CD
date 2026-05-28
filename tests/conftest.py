from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,900")

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture()
def page_url():
    root = Path(__file__).resolve().parents[1]
    return (root / "index.html").as_uri()
