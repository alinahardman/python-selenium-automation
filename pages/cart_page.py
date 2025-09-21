from selenium.webdriver.common.by import By


from pages.base_page import BasePage

class CartPage(BasePage):

    EMPTY_CART_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

    def empty_cart_message(self):
        actual_message = self.driver.find_element(*self.EMPTY_CART_MSG).text
        expected_message = 'Your cart is empty'
