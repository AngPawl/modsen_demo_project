import allure
from allure_commons.types import Severity

from modsen_demo_project.pages.lets_work_page import lets_work_page
from modsen_demo_project.pages.main_page import main_page


@allure.title('Let\'s Work page successfully opens via Get Started button')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_lets_work_page_successfully_opens():
    main_page.open()

    main_page.open_lets_work_page_via_get_started_button()

    lets_work_page.page_title_should_have_correct_text(
        'SOLVING YOUR BUSINESS CHALLENGES WITH MODSEN'
    )
