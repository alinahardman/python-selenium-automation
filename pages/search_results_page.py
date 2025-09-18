from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import BasePage

class SearchResults(BasePage):

    SEARCH_RESULTS = (By.XPATH, '//div[@data-test="lp-resultsCount"]')

    def verify_search_results(self, product):
        wait = WebDriverWait(self.driver, 10)
        search_results_element = wait.until(
            EC.presence_of_element_located(self.SEARCH_RESULTS)
        )
        actual_text = search_results_element.text
        assert product in actual_text, f'Error. Expected text "{product}" but got "{actual_text}"'