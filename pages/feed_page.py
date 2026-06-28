from pages.base_page import BasePage
from locators.feed_locators import FeedLocators
import allure

class FeedPage(BasePage):
    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed_button(self):
        self.click_element(FeedLocators.BUTTON_ORDER_FEED)

    @allure.step("Клик по карточке заказа в ленте")
    def click_order_card_in_feed(self):
        element = self.find_element_with_wait(FeedLocators.ORDER_CARD_IN_FEED)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получение значения счётчика 'Выполнено за всё время'")
    def get_all_time_counter_value(self):
        element = self.find_element_with_wait(FeedLocators.COUNTER_ALL_TIME)
        return element.text

    @allure.step("Получение значения счётчика 'Выполнено за сегодня'")
    def get_today_counter_value(self):
        element = self.find_element_with_wait(FeedLocators.COUNTER_TODAY)
        return element.text

    @allure.step("Получение номеров заказов из раздела 'В работе'")
    def get_orders_in_work_text(self):
        element = self.find_element_with_wait(FeedLocators.ORDER_IN_WORK_SECTION)
        return element.text