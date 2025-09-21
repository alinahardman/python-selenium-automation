from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SignInSideBar(BasePage):

    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')

    def click_sign_in(self):
        self.click(*self.SIGN_IN_BUTTON)