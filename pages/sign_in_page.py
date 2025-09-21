from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SignInPage(BasePage):

    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    USERNAME_FIELD = (By.NAME, 'username')
    PASSWORD_FIELD = (By.NAME, 'password')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button#login')
    ENTER_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'div#password')
    SIGN_IN_WITH_PASSWORD_BUTTON = (By.XPATH, '//button[text()="Sign in with password"]')
    SKIP_LINK = (By.XPATH, '//a[text()="Skip" and @href="/"]')
    TERMS_CONDITIONS_LINK = (By.XPATH, '//a[contains(@aria-label, "terms & conditions")]')


    def store_window(self):
        original_window = self.get_original_window()
        print('Original window: ', original_window)


    def click_target_terms_and_conditions(self):
        self.driver.find_element(*self.TERMS_CONDITIONS_LINK).click()


    def verify_sign_in_form_opened(self):
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


