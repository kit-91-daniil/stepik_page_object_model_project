import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    product_page_url = ProductPageLocators.PRODUCT_PAGE_URL
    product_page = ProductPage(browser, product_page_url)
    product_page.open()
    product_page.should_be_product_page()


@pytest.mark.xfail(reason="message are present")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page_url = ProductPageLocators.PRODUCT_PAGE_URL
    product_page = ProductPage(browser, product_page_url)
    product_page.open()
    product_page.should_be_not_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    product_page_url = ProductPageLocators.PRODUCT_PAGE_URL
    product_page = ProductPage(browser, product_page_url)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="message does not disappeared")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page_url = ProductPageLocators.PRODUCT_PAGE_URL
    product_page = ProductPage(browser, product_page_url)
    product_page.open()
    product_page.should_success_message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page_url = ProductPageLocators.PRODUCT_PAGE_URL
    product_page = ProductPage(browser, product_page_url)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_text_about_empty_basket()


@pytest.mark.xfail(reason="message does not disappeared")
def test_guest_can_see_products_in_basket_opened_from_the_main_page(browser):
    product_page_url = ProductPageLocators.PRODUCT_PAGE_URL
    product_page = ProductPage(browser, product_page_url)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_products_in_basket()
