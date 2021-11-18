from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
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
