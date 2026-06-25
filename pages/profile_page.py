from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators

class ProfilePage(BasePage):
    def click_order_history_link(self):
        self.click_element(ProfileLocators.LINK_ORDER_HISTORY)

    def click_logout_button(self):
        self.click_element(ProfileLocators.BUTTON_LOGOUT)