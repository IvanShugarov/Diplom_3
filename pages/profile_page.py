from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators
import allure

class ProfilePage(BasePage):
    @allure.step("Клик по кнопке 'История заказов' в личном кабинете")
    def click_order_history_link(self):
        self.click_element(ProfileLocators.LINK_ORDER_HISTORY)

    @allure.step("Клик по кнопке 'Выход' в личном кабинете")
    def click_logout_button(self):
        self.click_element(ProfileLocators.BUTTON_LOGOUT)