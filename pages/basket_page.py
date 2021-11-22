from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "There are products in basket, but they shouldn't be"

    def should_be_products_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "There are no products in basket"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present_and_has_the_text(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Text about basket emptiness does not present"
