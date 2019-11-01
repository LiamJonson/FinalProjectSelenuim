from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REG), "Registration  form is not found"

    def register_new_user(self, email, password):
        email_enter = self.browser.find_element(*LoginPageLocators.EMAIL_ENTER).send_keys(email)
        pas1_enter = self.browser.find_element(*LoginPageLocators.PAS1_ENTER).send_keys(password)
        pas2_enter = self.browser.find_element(*LoginPageLocators.PAS2_ENTER).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BTN).click()
        assert self.is_element_present(*LoginPageLocators.REG_COMPL) , "No registration complete"



