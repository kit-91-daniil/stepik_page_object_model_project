from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini span a.btn-default.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators(BasePageLocators):
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner>p")


class MainPageLocators(BasePageLocators):
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com"
    MAIN_PAGE_REGISTRATION_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success div.alertinner.wicon")


class LoginPageLocators:
    LOGIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD_INPUT_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    PRODUCT_PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_TO_BASKET_ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) div p strong")
    ADD_TO_BASKET_ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alertinner:nth-child(2) strong")
