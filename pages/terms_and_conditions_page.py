from selenium.webdriver.common.by import By


from pages.base_page import BasePage

class TermsAndConditions(BasePage):

    def verify_terms_and_conditions_opened(self):
        self.wait_until_url_contains('terms-conditions')


    def close_current_page(self):
         self.close()


    def switch_back_to_previous(self, original_window):
        self.switch_to_window_by_id(original_window)

