from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ACCOUNT_ICON = (By.ID, 'account-sign-in')
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH, '//button[@data-test="@web/Search/SearchButton"]')
CART_ICON = (By.CSS_SELECTOR, 'div[data-test="@web/CartIcon"]')


@when('Click Account')
def click_account(context):
    context.driver.find_element(*ACCOUNT_ICON).click()


@when('Search for {product_name}')
def search_product(context, product_name):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product_name)
    context.driver.find_element(*SEARCH_BUTTON).click()


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()

