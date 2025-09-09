from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click Account')
def click_account(context):
    context.driver.find_element(By.ID, 'account-sign-in').click()
    sleep(3)

@when('Click on Cart icon')
def click_cart(context):
        context.driver.find_element(By.CSS_SELECTOR, 'div[data-test="@web/CartIcon"]').click()
        sleep(3)

