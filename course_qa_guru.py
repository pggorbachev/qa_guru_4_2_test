from selene import browser, be, have
from selene.support.shared import browser


def test_google_should_find_selene(open_browser, maximize_window):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_negative_find_google_selene(open_browser, maximize_window):
    browser.element('[name="q"]').should(be.blank).type('qqqqqqqqqqqqqqqqqweewqweqweqweqweqw').press_enter()
    browser.element('.card-section').should(
        have.text('По запросу qqqqqqqqqqqqqqqqqweewqweqweqweqweqw ничего не найдено.'))
