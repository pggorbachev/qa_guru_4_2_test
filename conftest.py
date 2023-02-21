import pytest
from selene import browser


@pytest.fixture
def open_browser():
    browser.open('https://google.com')


@pytest.fixture
def maximize_window():
    browser.config.driver.maximize_window()
