from selene.support.shared import browser
from selene import be, have


def test_google_should_find_selene():
    browser.config.hold_browser_open = True
    browser.config.timeout = 6.0

    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))