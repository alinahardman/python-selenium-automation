from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ACCOUNT_ICON = (By.ID, 'account-sign-in')
CART_ICON = (By.CSS_SELECTOR, 'div[data-test="@web/CartIcon"]')


@when('Click Account')
def click_account(context):
    context.driver.find_element(*ACCOUNT_ICON).click()


@when('Search for {product_name}')
def search_product(context, product_name):
    print(product_name)
    context.app.header.search_product(product_name)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()

