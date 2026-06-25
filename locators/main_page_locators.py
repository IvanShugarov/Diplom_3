from selenium.webdriver.common.by import By

class MainPageLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//a[contains(@href, 'account')]")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    INGREDIENT_CARD = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    BUTTON_CLOSE_MODAL = (By.XPATH, "//button[contains(@class, 'modal__close')]")
    INGREDIENT_COUNTER = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a//*[contains(@class, 'counter_counter')]")
    BUTTON_CREATE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    BASKET_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    BASKET_TOP_BUN = (By.XPATH, "//*[contains(@class, 'constructor-element_pos_top')]")
    TITLE_CONSTRUCTOR = (By.XPATH, "//h1[text()='Соберите бургер']")
    TITLE_INGREDIENT_MODAL = (By.XPATH, "//h2[text()='Детали ингредиента']")
    ORDER_ID_TEXT = (By.XPATH, "//*[contains(@class, 'Modal_modal_container')]//h2 | //*[contains(text(), 'идентификатор')] | //*[contains(text(), 'Идентификатор')]")
    BUTTON_ORDER_FEED_HEADER = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    