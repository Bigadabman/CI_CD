from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("-headless")

    windows_firefox = Path("C:/Program Files/Mozilla Firefox/firefox.exe")
    if windows_firefox.exists():
        options.binary_location = str(windows_firefox)

    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()


@pytest.fixture()
def page_url():
    root = Path(__file__).resolve().parents[1]
    return (root / "index.html").as_uri()
