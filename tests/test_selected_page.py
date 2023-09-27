from modsen_demo_project.components.header_menu import header_menu
from modsen_demo_project.pages.main_page import main_page


def test_selected_page_opens():
    main_page.open()

    header_menu.open_selected_page('Portfolio')

    header_menu.selected_page_title_should_have_correct_text('SUCCESS STORIES')
