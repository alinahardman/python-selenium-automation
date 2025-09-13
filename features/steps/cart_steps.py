from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

EMPTY_CART_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="content-wrapper"] h4')
ADD_TO_CART_SIDE_NAV = (By.CSS_SELECTOR, 'shippingButton')


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()  # always clicks on 1st Add to cart btn
#     context.driver.wait.until(
#         EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
#         message='Side navigation product did not appear'
#     )


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored: ', context.product_name)


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_SIDE_NAV).click()
    sleep(5)


@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div[data-test="@web/CartIcon"]').click()
    sleep(3)


@then('Verify cart has correct product')
def verify_cart_product(context):
    cart_product_name = context.driver.find_element(By.CSS_SELECTOR, '[data-test="cartItem"] h4').text
    assert context.product_name in cart_product_name, f'Expected {context.product_name}, but got {cart_product_name}'


@then('Your cart is empty message is shown')
def empty_cart_message(context):
    actual_message = context.driver.find_element(*EMPTY_CART_MSG).text
    expected_message = 'Your cart is empty'
    assert expected_message in actual_message, f'Error. Expected "{expected_message}"'






