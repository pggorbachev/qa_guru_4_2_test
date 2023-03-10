import math

from selene.support.shared import browser
from selene import be, have


def test_google_should_find_selene():
    browser.config.hold_browser_open = True
    browser.config.timeout = 6.0

    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_homework_for_course_qa_guru_1():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.hold_browser_open = True
    browser.config.driver.maximize_window()
    browser.config.timeout = 5.0

    browser.element('[id="firstName"]').type('Pavel')
    browser.element('[id="lastName"]').type('Gorbachev')
    browser.element('[id="userEmail"]').type('test@test.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').type('1234567890')
    browser.element('[id="dateOfBirthInput"]').type('06 Dec 1995').press_enter()
    browser.element('[id="subjectsInput"]').type('e').press_enter()
    browser.element('[id="subjectsInput"]').type('e').send_keys(Keys.ARROW_DOWN).press_enter()
    browser.element('[id="hobbies-checkbox-3"]').submit()
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))



def test_login_on_qaguru():
    browser.open('https://qa.guru/cms/system/login')
    browser.config.hold_browser_open = True
    browser.config.timeout = 6.0

    browser.element('.login-form [name=email]').type('qagurubot@gmail.com')
    browser.element('.login-form [name="password"]').type('qagurupassword').press_enter()
    browser.element('.has-arrow').click()

    browser.element('.page-full-block').should(have.text('Здравствуйте, QA_GURU_BOT'))
