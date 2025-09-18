from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from features.steps.main_header_steps import search_product
from pages.base_page import BasePage


# circle, categories, deals, new & featured, pickup & delivery, search field, account icon, cart
class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, '//button[@data-test="@web/Search/SearchButton"]')
    CART_ICON = (By.CSS_SELECTOR, 'div[data-test="@web/CartIcon"]')

    def search_product(self, product_name):
        self.input_text(product_name, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
        sleep(9)

    def click_cart(self):
        self.click(*self.CART_ICON)