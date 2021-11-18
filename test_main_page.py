from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    main_page_url = MainPageLocators.MAIN_PAGE_URL
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    main_page_url = MainPageLocators.MAIN_PAGE_URL
    page = MainPage(browser, main_page_url)
    page.open()
    page.should_be_login_link()
