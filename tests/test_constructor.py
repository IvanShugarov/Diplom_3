import allure
from urls import Urls
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from pages.feed_page import FeedPage
from locators.feed_locators import FeedLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructor:
    @allure.title("Проверка перехода в Конструктор заказа")
    def test_navigate_to_constructor_success(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.LOGIN_URL)
        main_page.click_counstructor_button()
        element = main_page.find_element_with_wait(MainPageLocators.TITLE_CONSTRUCTOR)
        assert driver.current_url == Urls.BASE_URL
        assert element.is_displayed()

    @allure.title("Проверка перехода в Ленту заказов")
    def test_navigate_to_feed_success(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)
        main_page.click_order_feed_header_button()
        feed_page = FeedPage(driver)
        element = feed_page.find_element_with_wait(FeedLocators.TITLE_FEED)
        assert "/feed" in driver.current_url
        assert element.is_displayed()

    @allure.title("Проверка, что по клику на ингредиент всплывает окно с деталями")
    def test_open_ingredient_modal_success(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)
        main_page.click_ingredient_card()
        element = main_page.find_element_with_wait(MainPageLocators.BUTTON_CLOSE_MODAL)
        assert element.is_displayed()

    @allure.title("Проверка закрытие всплывающего окна с деталями ингредиента по клику на крестик")
    def test_close_ingredient_modal_success(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)
        main_page.click_ingredient_card()
        main_page.click_close_modal_button()
        assert main_page.check_element_is_invisible(MainPageLocators.TITLE_INGREDIENT_MODAL)

    @allure.title("Проверка увеличения каунтера ингредиента при его выборе")
    def test_ingredient_counter_increases_after_drag_and_drop(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)
        inital_counter_text = main_page.get_ingredient_counter_value()
        inital_counter = int(inital_counter_text or 0)
        main_page.drag_and_drop_ingredient_to_order()
        main_page.wait_for_counter_to_increase(inital_counter)
        new_counter = int(main_page.get_ingredient_counter_value())
        assert new_counter > inital_counter

    @allure.title("Проверка успешного оформления заказа залогиненным пользователем")
    def test_create_order_by_autorized_user_success(self, driver, user_data):
        auth_page = AuthPage(driver)
        auth_page.open_url(Urls.LOGIN_URL)
        auth_page.login_user(user_data["email"], user_data["password"])
        WebDriverWait(driver, 15).until(EC.url_to_be(Urls.BASE_URL))
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_create_order_button()
        element = main_page.find_element_with_wait(MainPageLocators.ORDER_ID_TEXT)
        assert element.is_displayed()