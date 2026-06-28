import allure
from locators.auth_locators import AuthLocators
from urls import Urls
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from locators.profile_locators import ProfileLocators


class TestProfile:
    @allure.title("Проверка успешного перехода в 'Личный кабинет'")
    def test_navigate_to_profile_page_success(self,driver,user_data):
        auth_page = AuthPage(driver)
        auth_page.open_url(Urls.LOGIN_URL)
        auth_page.login_user(user_data["email"],user_data["password"])
        auth_page.wait_for_url_to_change(Urls.LOGIN_URL)
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver)
        element = profile_page.find_element_with_wait(ProfileLocators.BUTTON_LOGOUT)
        assert "/account/profile" in profile_page.get_current_url()
        assert element.is_displayed()

    @allure.title("Проверка успешного перехода на страницу 'История Заказов'")
    def test_navigate_to_order_history_success(self,driver,user_data):
        auth_page = AuthPage(driver)
        auth_page.open_url(Urls.LOGIN_URL)
        auth_page.login_user(user_data["email"],user_data["password"])
        auth_page.wait_for_url_to_change(Urls.LOGIN_URL)
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver)
        profile_page.click_order_history_link()
        element = profile_page.find_element_with_wait(ProfileLocators.LINK_ORDER_HISTORY)
        assert "/account/order-history" in profile_page.get_current_url()
        assert element.is_displayed()
         
    @allure.title("Проверка успешного выхода из аккаунта")
    def test_logout_from_profile_success(self,driver,user_data):
        auth_page = AuthPage(driver)
        auth_page.open_url(Urls.LOGIN_URL)
        auth_page.login_user(user_data["email"],user_data["password"])
        auth_page.wait_for_url_to_change(Urls.LOGIN_URL)
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver)
        profile_page.click_logout_button()
        profile_page.wait_for_url_to_be(Urls.LOGIN_URL)
        element = auth_page.find_element_with_wait(AuthLocators.BUTTON_LOGIN)
        assert "/login" in auth_page.get_current_url()
        assert element.is_displayed()
