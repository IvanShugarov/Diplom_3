from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(BasePage):
    def click_personal_account_button(self):
        element = self.find_element_with_wait(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)
        self.driver.execute_script("arguments[0].click();", element)

    def click_counstructor_button(self):
        element = self.find_element_with_wait(MainPageLocators.BUTTON_CONSTRUCTOR)
        self.driver.execute_script("arguments[0].click();", element)

    def click_ingredient_card(self): 
        element = self.find_element_with_wait(MainPageLocators.INGREDIENT_CARD)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_close_modal_button(self):
        self.click_element(MainPageLocators.BUTTON_CLOSE_MODAL)

    def click_create_order_button(self):
        element = self.find_element_with_wait(MainPageLocators.BUTTON_CREATE_ORDER)
        self.driver.execute_script("arguments[0].click();", element)

    def get_ingredient_counter_value(self):
        element = self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER)
        return element.text

    def wait_for_counter_to_increase(self, old_value):
        WebDriverWait(self.driver, 5).until(lambda d: d.find_element(*MainPageLocators.INGREDIENT_COUNTER).text.strip().isdigit() and int(d.find_element(*MainPageLocators.INGREDIENT_COUNTER).text.strip()) > old_value)
    
    def drag_and_drop_ingredient_to_order(self):
        element = self.find_element_with_wait(MainPageLocators.INGREDIENT_CARD)
        target = self.find_element_with_wait(MainPageLocators.BASKET_TOP_BUN)
        # Скроллим до булки, чтобы браузеры её железно увидели в DOM
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element, target)

    def get_order_id_value(self):
        element = self.find_element_with_wait(MainPageLocators.ORDER_ID_TEXT)
        return element.text
        
    def click_order_feed_header_button(self):
        element = self.find_element_with_wait(MainPageLocators.BUTTON_ORDER_FEED_HEADER)
        self.driver.execute_script("arguments[0].click();", element)