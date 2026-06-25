from pages.base_page import BasePage
from locators.feed_locators import FeedLocators

class FeedPage(BasePage):
    def click_order_feed_button(self):
        self.click_element(FeedLocators.BUTTON_ORDER_FEED)

    def click_order_card_in_feed(self):
        element = self.find_element_with_wait(FeedLocators.ORDER_CARD_IN_FEED)
        self.driver.execute_script("arguments[0].click();", element)

    def get_all_time_counter_value(self):
        element = self.find_element_with_wait(FeedLocators.COUNTER_ALL_TIME)
        return element.text

    def get_today_counter_value(self):
        element = self.find_element_with_wait(FeedLocators.COUNTER_TODAY)
        return element.text

    def get_orders_in_work_text(self):
        element = self.find_element_with_wait(FeedLocators.ORDER_IN_WORK_SECTION)
        return element.text