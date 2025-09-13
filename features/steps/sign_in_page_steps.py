from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN_BUTTON).click()


@then('Sign In form opened')
def sign_in_form(context):
    username_field = context.driver.find_element(By.ID, 'username')
    # Verify that the field is visible on the page
    assert username_field.is_displayed(), "Error: Username field is not visible!"
    print("Username field is present and visible.")


