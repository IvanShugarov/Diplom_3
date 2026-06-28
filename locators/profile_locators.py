from selenium.webdriver.common.by import By

class ProfileLocators:
    LINK_ORDER_HISTORY = (By.XPATH,".//a[text()='История заказов']")
    BUTTON_LOGOUT = (By.XPATH,".//button[@type='button'and text()='Выход']")