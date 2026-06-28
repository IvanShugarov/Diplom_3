from selenium.webdriver.common.by import By

class AuthLocators:
    LINK_FORGOT_PASSWORD = (By.XPATH,".//a[@href='/forgot-password']")
    INPUT_EMAIL_FORGOT = (By.XPATH,".//input[@name='name']")
    BUTTON_RESTORE = (By.XPATH,".//button[text()='Восстановить']")
    BUTTON_SHOW_HIDE_PASSWORD = (By.XPATH, "//*[contains(@class, 'icon')] | //svg")
    INPUT_PASSWORD_CONTAINER_ACTIVE = (By.XPATH, "//*[contains(@class, 'active')]")
    INPUT_EMAIL_LOGIN = (By.XPATH, ".//input[@name='name']")
    INPUT_PASSWORD_LOGIN = (By.XPATH,".//input[@type='password']")
    BUTTON_LOGIN = BUTTON_LOGIN = (By.XPATH, ".//button[contains(@class, 'button_button_type_primary')]")