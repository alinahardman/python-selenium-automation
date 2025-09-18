from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify search results are shown for {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)



