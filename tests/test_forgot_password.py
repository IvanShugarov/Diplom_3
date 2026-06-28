import allure
from urls import Urls
from pages.auth_page import AuthPage
from locators.auth_locators import AuthLocators

class TestForgotPassword:
    @allure.title("Проверка перехода на страницу восстановления пароля")
    def test_navigate_to_forgot_password(self,driver):
        auth_page = AuthPage(driver)
        auth_page.open_url(Urls.LOGIN_URL)
        auth_page.click_forgot_password_link()
        element = auth_page.find_element_with_wait(AuthLocators.BUTTON_RESTORE)
        assert "/forgot-password" in auth_page.get_current_url()
        assert element.is_displayed()

    @allure.title("Проверка перехода на страница создания нового пароля")    
    def test_input_email_and_click_restore(self,driver):
        auth_page = AuthPage(driver)
        auth_page.open_url(Urls.FORGOT_PASSWORD_URL)
        auth_page.input_email_for_restore("test_user@yandex.ru")
        auth_page.click_element(AuthLocators.BUTTON_RESTORE)
        element = auth_page.find_element_with_wait(AuthLocators.BUTTON_SHOW_HIDE_PASSWORD)
        assert "/reset-password" in auth_page.get_current_url()
        assert element.is_displayed()

    @allure.title("Проверка, что по клику на иконку глаза пароль становится видимым")
    def test_click_eye_icon_activates_field(self,driver):
        auth_page = AuthPage(driver)
        auth_page.open_url(Urls.FORGOT_PASSWORD_URL)
        auth_page.input_email_for_restore("test_user@yandex.ru")
        auth_page.click_element(AuthLocators.BUTTON_RESTORE)
        auth_page.click_show_hide_password_icon()
        assert auth_page.is_password_field_active() is True
