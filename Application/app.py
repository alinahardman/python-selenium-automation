from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.header_page import Header
from pages.search_results_page import SearchResults
from pages.sign_in_page import SignInPage
from pages.sign_in_side_bar import SignInSideBar
from pages.circle_page import CirclePage
from pages.product_details_page import ProductDetailsPage
from pages.terms_and_conditions_page import TermsAndConditions

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.header_page = Header(driver)
        self.search_results_page = SearchResults(driver)
        self.cart_page = CartPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.sign_in_side_bar = SignInSideBar(driver)
        self.circle_page = CirclePage(driver)
        self.product_details_page = ProductDetailsPage(driver)
        self.terms_and_conditions_page = TermsAndConditions(driver)