import allure
from allure_commons.types import Severity

from modsen_demo_project.components.header_menu import header_menu
from modsen_demo_project.pages.main_page import main_page


@allure.title('Scroll to Top button works correctly')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_scroll_button_returns_focus_to_the_top():
    main_page.open()

    main_page.scroll_to_lets_work_with_us_section().click_on_scroll_button()

    header_menu.logo_should_be_present()
