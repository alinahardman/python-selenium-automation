from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]').click()
    sleep(3)

@then('Sign In form opened')
def sign_in_form(context):
    username_field = context.driver.find_element(By.ID, 'username')
    # Verify that the field is visible on the page
    assert username_field.is_displayed(), "Error: Username field is not visible!"
    sleep(3)
    print("Username field is present and visible.")

    context.driver.quit()
