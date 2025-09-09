from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Your cart is empty message is shown')
def empty_cart_message(context):
    actual_message = context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]').text
    expected_message = 'Your cart is empty'
    assert expected_message in actual_message, f'Error. Expected "{expected_message}"'
    sleep(3)

    context.driver.quit()


