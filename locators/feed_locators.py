from selenium.webdriver.common.by import By

class FeedLocators:
    BUTTON_ORDER_FEED = (By.XPATH, "//p[text()='Лента заказов']/parent::a")
    ORDER_CARD_IN_FEED = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]//a[contains(@class, 'OrderHistory_link')]")
    COUNTER_ALL_TIME = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")
    COUNTER_TODAY = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")
    ORDER_IN_WORK_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")
    TITLE_FEED = (By.XPATH, "//h1[text()='Лента заказов']")
    BUTTON_CLOSE_MODAL = (By.XPATH, "//button[contains(@class, 'modal__close')] | //button[contains(@class, 'close')]")
    ORDER_MODAL_DETAILS = (By.XPATH, "//p[text()='Состав']")