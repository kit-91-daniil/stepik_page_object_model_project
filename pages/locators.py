from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
