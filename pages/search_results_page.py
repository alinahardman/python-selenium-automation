from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import BasePage

class SearchResults(BasePage):

    SEARCH_RESULTS = (By.XPATH, '//div[@data-test="lp-resultsCount"]')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="content-wrapper"] h4')
    ADD_TO_CART_SIDE_NAV = (By.CSS_SELECTOR, '[class="styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButtonPrimary__tqtKH"]')
    PRODUCT_CART_TEXT = (By.CSS_SELECTOR, '[class="styles_ndsTruncate__GRSDE h-text-bs"]')
    VIEW_CART_CHECK_OUT_BUTTON = (By.CSS_SELECTOR, '[href="/cart"]')

    def verify_search_results(self, product):
        wait = WebDriverWait(self.driver, 10)
        search_results_element = wait.until(
            EC.presence_of_element_located(self.SEARCH_RESULTS)
        )
        actual_text = search_results_element.text
        assert product in actual_text, f'Error. Expected text "{product}" but got "{actual_text}"'


    def click_add_to_cart(self):
        button = self.driver.wait.until(
            EC.presence_of_element_located(self.ADD_TO_CART_BUTTON)
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        button.click()


    def store_product_name(self):
        product_name = self.driver.find_element(*self.SIDE_NAV_PRODUCT_NAME).text
        print('Product name stored: ', product_name)
        return product_name


    def side_nav_click_add_to_cart(self):
        button = self.driver.wait.until(
            EC.presence_of_element_located(self.ADD_TO_CART_SIDE_NAV)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        button.click()


    def verify_product_name(self, expected_product_name):
        wait = WebDriverWait(self.driver, 10)
        # Wait till the product name in cart is visible or located
        product_elem = self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_CART_TEXT)
        )
        product_name_in_cart = product_elem.text
        print('Name in cart: ', product_name_in_cart)

        # Assuming context.product_name was set when you "Store product name"
        assert expected_product_name[:20] == product_name_in_cart[:20], \
            f'Expected {expected_product_name[:20]} did not match {product_name_in_cart[:20]}'


    def click_view_and_checkout(self):
        self.driver.find_element(*self.VIEW_CART_CHECK_OUT_BUTTON).click()


