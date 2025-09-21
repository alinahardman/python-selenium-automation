from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from features.steps.main_header_steps import search_product
from pages.base_page import BasePage


class Header(BasePage):

    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, '//button[@data-test="@web/Search/SearchButton"]')
    CART_ICON = (By.CSS_SELECTOR, 'div[data-test="@web/CartIcon"]')
    ACCOUNT_ICON = (By.ID, 'account-sign-in')

    def search_product(self, product_name):
        self.input_text(product_name, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
        sleep(9)


    def click_cart(self):
        self.click(*self.CART_ICON)


    def click_account(self):
        self.click(*self.ACCOUNT_ICON)


    def verify_user_logged_in(self, username):
        wait = WebDriverWait(self.driver, 10)
        account_icon_element = wait.until(
            EC.presence_of_element_located(self.ACCOUNT_ICON)
        )

        actual_text = account_icon_element.text
        assert username in actual_text, \
            f'Error. Expected text "{username}" but got "{actual_text}"'

