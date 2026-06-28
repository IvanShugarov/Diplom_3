from pages.base_page import BasePage
from locators.auth_locators import AuthLocators
import allure


class AuthPage(BasePage):
    @allure.step("Клик по ссылке 'Восстановить пароль'")
    def click_forgot_password_link(self):
        element = self.find_element_with_wait(AuthLocators.LINK_FORGOT_PASSWORD)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввод email для восстановления пароля: {email}")
    def input_email_for_restore(self, email):
        self.input_text(email, AuthLocators.INPUT_EMAIL_FORGOT)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_restore_button(self):
        self.click_element(AuthLocators.BUTTON_RESTORE)

    @allure.step("Клик по иконке показать/скрыть пароль")
    def click_show_hide_password_icon(self):
        element = self.find_element_with_wait(AuthLocators.BUTTON_SHOW_HIDE_PASSWORD)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Проверка активности поля ввода пароля")
    def is_password_field_active(self):
        element = self.find_element_with_wait(AuthLocators.INPUT_PASSWORD_CONTAINER_ACTIVE)
        return element.is_displayed()

    @allure.step("Авторизаця пользователя с email: {email}")
    def login_user(self, email, password):
        self.input_text(email, AuthLocators.INPUT_EMAIL_LOGIN)
        self.input_text(password, AuthLocators.INPUT_PASSWORD_LOGIN)
        self.click_element(AuthLocators.BUTTON_LOGIN)