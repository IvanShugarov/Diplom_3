import allure
from urls import Urls
from pages.feed_page import FeedPage
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from locators.feed_locators import FeedLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestFeed:
    @allure.title("Проверка успешного открытия окна с деталями заказа")
    def test_open_order_modal_in_feed_success(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_url(Urls.FEED_URL)
        feed_page.click_order_card_in_feed()
        WebDriverWait(driver,10).until(EC.url_changes(Urls.FEED_URL))
        assert driver.current_url != Urls.FEED_URL
        assert "/feed/" in driver.current_url

    @allure.title("Проверка успешного обновления счётчиков при создании заказа")
    def test_counters_update_success(self, driver, user_data):
        feed_page = FeedPage(driver)
        feed_page.open_url(Urls.FEED_URL)
        old_all = int(feed_page.get_all_time_counter_value())
        old_today = int(feed_page.get_today_counter_value())
        auth_page = AuthPage(driver)
        auth_page.open_url(Urls.LOGIN_URL)
        auth_page.login_user(user_data["email"], user_data["password"])
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_create_order_button()
        feed_page.open_url(Urls.FEED_URL)
        assert int(feed_page.get_all_time_counter_value()) >= old_all
        assert int(feed_page.get_today_counter_value()) >= old_today

    @allure.title("Отображение номера созданного заказа в разделе 'В работе'")
    def test_order_in_work_section_success(self, driver, user_data):
        auth_page = AuthPage(driver)
        auth_page.open_url(Urls.LOGIN_URL)
        auth_page.login_user(user_data["email"], user_data["password"])
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_create_order_button()
        feed_page = FeedPage(driver)
        feed_page.open_url(Urls.FEED_URL)
        assert feed_page.find_element_with_wait(FeedLocators.ORDER_IN_WORK_SECTION).is_displayed()