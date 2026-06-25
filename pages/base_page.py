from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        
    def open_url(self,url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))
        return element

    def click_element(self,locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def input_text(self,text,locator):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def check_element_is_invisible(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))