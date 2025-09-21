from behave import then


@then('Sign In form opened')
def sign_in_form(context):
    context.app.sign_in_page.sign_in_form()