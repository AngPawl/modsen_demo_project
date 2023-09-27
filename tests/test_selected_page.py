import allure
from allure_commons.types import Severity

from modsen_demo_project.components.header_menu import header_menu
from modsen_demo_project.pages.main_page import main_page


@allure.title('User opens a new page via header menu')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_selected_page_opens():
    main_page.open()

    header_menu.open_selected_page('Portfolio')

    header_menu.selected_page_title_should_have_correct_text('SUCCESS STORIES')
