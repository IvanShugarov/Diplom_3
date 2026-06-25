from pages.base_page import BasePage
from locators.auth_locators import AuthLocators


class AuthPage(BasePage):
    def click_forgot_password_link(self):
        element = self.find_element_with_wait(AuthLocators.LINK_FORGOT_PASSWORD)
        self.driver.execute_script("arguments[0].click();", element)

    def input_email_for_restore(self, email):
        self.input_text(email, AuthLocators.INPUT_EMAIL_FORGOT)

    def click_restore_button(self):
        self.click_element(AuthLocators.BUTTON_RESTORE)

    def click_show_hide_password_icon(self):
        element = self.find_element_with_wait(AuthLocators.BUTTON_SHOW_HIDE_PASSWORD)
        self.driver.execute_script("arguments[0].click();", element)

    def is_password_field_active(self):
        element = self.find_element_with_wait(AuthLocators.INPUT_PASSWORD_CONTAINER_ACTIVE)
        return element.is_displayed()

    def login_user(self, email, password):
        self.input_text(email, AuthLocators.INPUT_EMAIL_LOGIN)
        self.input_text(password, AuthLocators.INPUT_PASSWORD_LOGIN)
        self.click_element(AuthLocators.BUTTON_LOGIN)