from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SignInPage(BasePage):

    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    USERNAME_FIELD = (By.NAME, 'username')
    PASSWORD_FIELD = (By.NAME, 'password')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button#login')
    # CONTINUE_BUTTON = (By.XPATH, '(//*[contains(@class, "styles_cellContent__tjccx")])[3]')
    ENTER_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'div#password')
    SIGN_IN_WITH_PASSWORD_BUTTON = (By.XPATH, '//button[text()="Sign in with password"]')
    SKIP_LINK = (By.XPATH, '//a[text()="Skip" and @href="/"]')

    def sign_in_form(self):
        username_field = self.driver.find_element(*self.USERNAME_FIELD)
        assert username_field.is_displayed(), "Error: Username field is not visible!"
        print("Username field is present and visible.")


    def input_email(self, email):
        self.input_text(email, *self.USERNAME_FIELD)


    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()


    def click_use_password(self):
        self.driver.find_element(*self.ENTER_PASSWORD_BUTTON).click()


    def input_password(self, password):
        # password_field = self.driver.find_element(*self.PASSWORD_FIELD).click()
        self.input_text(password, *self.PASSWORD_FIELD)


    def click_sign_in_with_password(self):
        self.driver.find_element(*self.SIGN_IN_WITH_PASSWORD_BUTTON).click()


    def skip_link(self):
        self.driver.find_element(*self.SKIP_LINK).click()