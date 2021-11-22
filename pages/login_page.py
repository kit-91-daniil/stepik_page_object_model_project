import time
from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = "87rWiEtX8RdBqBu"
        email_input = self.find_element_expl_waiting(*LoginPageLocators.REGISTER_FORM_EMAIL_INPUT)
        password_input = self.find_element_expl_waiting(*LoginPageLocators.REGISTER_FORM_PASSWORD_INPUT)
        password_input_repeat = self.find_element_expl_waiting(
            *LoginPageLocators.REGISTER_FORM_PASSWORD_INPUT_REPEAT
        )
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_input_repeat.send_keys(password)
        self.do_click(*LoginPageLocators.REGISTER_FORM_SUBMIT_BUTTON)
        self.is_element_present_and_has_the_text(*MainPageLocators.MAIN_PAGE_REGISTRATION_SUCCESS_MESSAGE)
        self.should_be_authorized_user()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_with_lang = self.browser.current_url
        splitted_url = url_with_lang.split(".com")
        url_without_lang = splitted_url[0] + \
                           ".com/" + "/".join(splitted_url[1].split("/")[2:])

        assert url_without_lang == LoginPageLocators.LOGIN_PAGE_URL, "Current url is not match login page url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "The login form " \
                                                                       "is not present on the login page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "The register form " \
                                                                          "is not present on the register page"
