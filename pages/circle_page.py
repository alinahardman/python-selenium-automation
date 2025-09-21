from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CirclePage(BasePage):

    BENEFIT_CELLS = (By.CSS_SELECTOR, '.sc-acea07d2-5.lbeNLX')

    def open_circle(self):
        self.driver.get('https://www.target.com/circle')


    def benefit_cells_count(self):
        benefit_cells = self.driver.find_elements(*self.BENEFIT_CELLS)
        assert len(benefit_cells) >= 10, \
            f"Expected at least 10 benefit cells, but found {len(benefit_cells)}"

