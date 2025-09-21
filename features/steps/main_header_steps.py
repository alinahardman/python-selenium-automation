from behave import when, then


@when('Click Account')
def click_account(context):
    context.app.header_page.click_account()


@when('Search for {product_name}')
def search_product(context, product_name):
    print(product_name)
    context.app.header_page.search_product(product_name)


@when('Click on Cart icon')
def click_cart(context):
    context.app.header_page.click_cart()


@then('Verify user is logged in')
def verify_user_logged_in(context):
    username = 'Future'
    context.app.header_page.verify_user_logged_in(username)

