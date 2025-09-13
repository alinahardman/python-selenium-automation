from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_CELLS = (By.CSS_SELECTOR, '.sc-acea07d2-5.lbeNLX')

@given('Open circle page')
def open_circle(context):
    context.driver.get('https://www.target.com/circle')

@then('At least 10 Benefit cells are shown')
def benefit_cells_count(context):
    benefit_cells = context.driver.find_elements(*BENEFIT_CELLS)
    assert len(benefit_cells) >= 10

