import allure
from selene import browser, be
from selene.core.command import js


class MainPage:
    def __init__(self):
        self.get_started_button = browser.element('[id="get stared"]')
        self.scroll_button = browser.element('#scroll_button')
        self.lets_work_with_us_section = browser.element('h2.title')

    @staticmethod
    @allure.step('Open Main Page')
    def open():
        browser.open('/')

    @allure.step('Scroll to Lets Work With Us section')
    def scroll_to_lets_work_with_us_section(self):
        self.lets_work_with_us_section.perform(command=js.scroll_into_view)
        return self

    @allure.step('Click on scroll button')
    def click_on_scroll_button(self):
        self.scroll_button.click()

    @allure.step('Button Get Started should be visible')
    def get_started_button_should_be_visible(self):
        self.get_started_button.should(be.visible)

    @allure.step('Open Lets Work Page')
    def open_lets_work_page_via_get_started_button(self):
        self.get_started_button.click()


main_page = MainPage()
