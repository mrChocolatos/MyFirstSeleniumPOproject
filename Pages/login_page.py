from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.get_curren_url(), 'Url dont have "login" path'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGIST_FORM), "REGIST_FORM is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.RESIST_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.RESIST_PASS1_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.RESIST_PASS2_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.RESIST_SUBMIT).click()
