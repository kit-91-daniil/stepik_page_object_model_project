from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_TO_BASKET_ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) div p strong")
    ADD_TO_BASKET_ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alertinner:nth-child(2) strong")
