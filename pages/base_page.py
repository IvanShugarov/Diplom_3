from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
class BasePage:
    def __init__(self,driver):
        self.driver = driver

    @allure.step("Открытие URL-адреса: {url}")    
    def open_url(self,url):
        self.driver.get(url)

    @allure.step("Поиск элемента с ожиданием: {locator}")
    def find_element_with_wait(self, locator):
        element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))
        return element

    @allure.step("Клик по элементу: {locator}")
    def click_element(self,locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step("Ввод текста в элемент: {locator}")
    def input_text(self,text,locator):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step("Проверка, что элемент не отображается: {locator}")
    def check_element_is_invisible(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))
    
    @allure.step("Получение текущего URL-адреса страницы браузера")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Ожидание изменения URL-адреса с базового {old_url}")
    def wait_for_url_to_change(self, old_url, timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.url_changes(old_url))
    
    @allure.step("Ожидание, пока URL-адрес строго станет равен {target_url}")
    def wait_for_url_to_be(self, target_url, timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.url_to_be(target_url))