import pytest
from playwright.sync_api import sync_playwright
from Utils.config import BASE_URL

@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            channel="chrome"
            #channel="msedge"
        )

        # Fresh context = clean cookies, localStorage, sessionStorage
        context = browser.new_context()

        page = context.new_page()

        page.goto(BASE_URL)

        yield page

        context.close()
        browser.close()