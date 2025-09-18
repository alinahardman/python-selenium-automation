from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

CART_ICON = (By.CSS_SELECTOR, 'div[data-test="@web/CartIcon"]')
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="content-wrapper"] h4')
ADD_TO_CART_SIDE_NAV = (By.CSS_SELECTOR, '[class="styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButtonPrimary__tqtKH"]')
CLOSE_SIDE_BAR_NAV = CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'styles_ndsBaseIconButton__fvBCi') and contains(@class, 'styles_ndsIconButtonClose__CIRkR')]")# OVERLAY = (By.CLASS_NAME, 'ReactModal__Overlay')
VIEW_CART_CHECK_OUT_BUTTON = (By.CSS_SELECTOR, '[href="/cart"]')
PRODUCT_CART_TEXT = (By.CSS_SELECTOR, '[class="styles_ndsTruncate__GRSDE h-text-bs"]')


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    # Wait until the button is present
    button = context.driver.wait.until(
        EC.presence_of_element_located(ADD_TO_CART_BUTTON)
    )

    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    button.click()


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored: ', context.product_name)


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    button = context.driver.wait.until(
        EC.presence_of_element_located(ADD_TO_CART_SIDE_NAV)
    )
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    button.click()


@when('Click View Cart & Check Out')
def click_view_and_checkout(context):
    context.driver.find_element(*VIEW_CART_CHECK_OUT_BUTTON).click()


@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(*CART_ICON).click()


@then('Verify cart has correct product')
def verify_product_name(context):
    wait = WebDriverWait(context.driver, 10)
    # Wait till the product name in cart is visible or located
    product_elem = wait.until(
        EC.visibility_of_element_located(PRODUCT_CART_TEXT)
    )
    product_name_in_cart = product_elem.text
    print('Name in cart: ', product_name_in_cart)

    # Assuming context.product_name was set when you "Store product name"
    assert context.product_name[:20] == product_name_in_cart[:20], \
        f'Expected {context.product_name[:20]} did not match {product_name_in_cart[:20]}'


@then('Your cart is empty message is shown')
def empty_cart_message(context):
    context.app.cart_page.empty_cart_message()





