from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_product_to_basket_button()

    def should_be_success_message_actual(self):
        self.should_add_product_to_basket_message_name_be_actual()
        self.should_add_product_to_basket_message_price_be_actual()

    def should_be_not_success_message_after_adding_product_to_basket(self):
        self.should_be_add_product_to_basket_button()
        self.should_not_be_success_message_name_after_adding_product_to_basket()
        self.should_not_be_success_message_price_after_adding_product_to_basket()

    def should_not_be_success_message(self):  # Implemented
        self.should_not_be_success_message_name()
        self.should_not_be_success_message_price()

    def should_success_message_disappeared_after_adding_product_to_basket(self):
        self.should_be_add_product_to_basket_button()
        self.should_success_message_with_name_disappeared_after_adding_product_to_basket()
        self.should_success_message_with_price_disappeared_after_adding_product_to_basket()

    def should_be_add_product_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET
        ), "The add_to_basket button is not present on the product page"

    def should_be_solving_quiz_and_getting_code(self):
        self.do_click(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        assert self.solve_quiz_and_get_code(), "Quiz wasn't solved"

    def should_add_product_to_basket_message_name_be_actual(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        add_to_basket_alert_product_name = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_ALERT_PRODUCT_NAME
        ).text
        assert product_name == add_to_basket_alert_product_name, \
            "When product is added to basket in the message product name is not actual"

    def should_add_product_to_basket_message_price_be_actual(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        add_to_basket_alert_product_price = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_ALERT_PRODUCT_PRICE
        ).text
        assert product_price == add_to_basket_alert_product_price, \
            "When product is added to basket in the message product price is not actual"

    def should_not_be_success_message_name(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_ALERT_PRODUCT_NAME), \
            "Success message about product adding to basket present"

    def should_not_be_success_message_price(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_ALERT_PRODUCT_PRICE), \
            "Success message about basket total price increasing present"

    def should_not_be_success_message_name_after_adding_product_to_basket(self):
        self.do_click(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_ALERT_PRODUCT_NAME), \
            "Success message about product adding to basket present"

    def should_not_be_success_message_price_after_adding_product_to_basket(self):
        self.do_click(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_ALERT_PRODUCT_PRICE), \
            "Success message about basket total price increasing present"

    def should_success_message_with_name_disappeared_after_adding_product_to_basket(self):
        self.do_click(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        assert self.is_element_disappeared(*ProductPageLocators.ADD_TO_BASKET_ALERT_PRODUCT_NAME), \
            "Success message with name after adding product to basket is disappeared"

    def should_success_message_with_price_disappeared_after_adding_product_to_basket(self):
        self.do_click(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        assert self.is_element_disappeared(*ProductPageLocators.ADD_TO_BASKET_ALERT_PRODUCT_PRICE), \
            "Success message with price after adding product to basket is not disappeared"
