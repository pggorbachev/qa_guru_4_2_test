import pytest
from selene import browser
from selene import be, have


@pytest.fixture
def open_browser():
    browser.open('https://google.com')


@pytest.fixture
def maximize_window():
    browser.config.driver.maximize_window()


@pytest.fixture
def find_text():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()