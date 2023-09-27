import allure
from selene import browser, have


class LetsWorkPage:
    def __init__(self):
        self.page_title = browser.element('[class^="StyledHeading"]')

    @allure.step('Lets Work Page should have title {text}')
    def page_title_should_have_correct_text(self, text):
        self.page_title.should(have.exact_text(text))


lets_work_page = LetsWorkPage()
