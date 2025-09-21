from behave import when, then


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.app.search_results_page.click_add_to_cart()


@when('Store product name')
def store_product_name(context):
    context.product_name = context.app.search_results_page.store_product_name()


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
   context.app.search_results_page.side_nav_click_add_to_cart()


@when('Click View Cart & Check Out')
def click_view_and_checkout(context):
    context.app.search_results_page.click_view_and_checkout()


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.search_results_page.verify_product_name(context.product_name)


@then('Your cart is empty message is shown')
def empty_cart_message(context):
    context.app.cart_page.empty_cart_message()





