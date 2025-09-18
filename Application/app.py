from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResults



class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResults(driver)
