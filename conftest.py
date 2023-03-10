import pytest
from selene import browser
from selene import be, have


@pytest.fixture
def open_browser():
    browser.open('https://google.com')


@pytest.fixture
def maximize_window():
    browser.config.driver.maximize_window()
