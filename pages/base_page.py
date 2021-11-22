import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from .locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def do_click(self, how, what, timeout=4):
        WebDriverWait(self.browser, timeout=timeout).until(EC.visibility_of_element_located((how, what))).click()

    def find_element_expl_waiting(self, how, what, timeout=4):
        try:
            element = WebDriverWait(self.browser, timeout=timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return element

    def is_element_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present_and_has_the_text(self, how, what, timeout=4):
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        result = element.text if hasattr(element, "text") else True
        return result

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def go_to_basket_page(self):
        self.do_click(*BasePageLocators.BASKET_LINK)

    def go_to_login_page(self):
        self.do_click(*BasePageLocators.LOGIN_LINK)

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, " \
                                                                     "probably unauthorized user"

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Basket link is not present"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not present"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            print("TRY BLOCK")
            alert = self.browser.switch_to.alert
            print("Switching to alert")
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            return True
        except NoAlertPresentException:
            print("No second alert presented")
