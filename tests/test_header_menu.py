from modsen_demo_project.components.header_menu import header_menu
from modsen_demo_project.pages.main_page import main_page


def test_header_menu_has_correct_titles():
    main_page.open()

    header_menu.header_menu_should_have_correct_titles(
        ['Services', 'Possibilities', 'Approach', 'Portfolio', 'Blog', 'Our Team']
    )


def test_header_menu_has_logo():
    main_page.open()

    header_menu.logo_should_be_present()
