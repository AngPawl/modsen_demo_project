import allure
from selene import browser, have, be
from selene.support.conditions.have import exact_text


class HeaderMenu:
    def __init__(self):
        self.logo = browser.element('[alt="Modsen Logo"]')
        self.header_nemu = browser.all(
            '#header [class^="StyledBox"] span [color="milkyWhite"]'
        )
        self.selected_page_title = browser.element('.image-section-title div')

    @allure.step('Open {page_name} page')
    def open_selected_page(self, page_name):
        self.header_nemu.element_by(exact_text(page_name)).click()

    @allure.step('Header menu titles should have correct titles: {titles}')
    def header_menu_should_have_correct_titles(self, titles):
        self.header_nemu.should(have.exact_texts(titles))

    @allure.step('Logo should be present on the page')
    def logo_should_be_present(self):
        self.logo.should(be.present)

    @allure.step('Portfolio Page should have title {text}')
    def selected_page_title_should_have_correct_text(self, text):
        self.selected_page_title.should(have.exact_text(text))


header_menu = HeaderMenu()
