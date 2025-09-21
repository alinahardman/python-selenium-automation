from behave import given, then


@given('Open target product A-91269718 page')
def open_target(context):
    context.app.product_details_page.open_target()


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    context.app.product_details_page.click_and_verify_colors()
