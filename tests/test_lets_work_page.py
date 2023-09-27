from modsen_demo_project.pages.lets_work_page import lets_work_page
from modsen_demo_project.pages.main_page import main_page


def test_lets_work_page_successfully_opens():
    main_page.open()

    main_page.open_lets_work_page_via_get_started_button()

    lets_work_page.page_title_should_have_correct_text(
        'SOLVING YOUR BUSINESS CHALLENGES WITH MODSEN'
    )
