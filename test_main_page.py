import pytest

from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_from_main
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        main_page_url = MainPageLocators.MAIN_PAGE_URL
        main_page = MainPage(browser, main_page_url)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        main_page_url = MainPageLocators.MAIN_PAGE_URL
        page = MainPage(browser, main_page_url)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page_url = MainPageLocators.MAIN_PAGE_URL
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_text_about_empty_basket()


@pytest.mark.xfail(reason="message does not disappeared")
def test_guest_can_see_products_in_basket_opened_from_the_main_page(browser):
    main_page_url = MainPageLocators.MAIN_PAGE_URL
    page = MainPage(browser, main_page_url)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_products_in_basket()
