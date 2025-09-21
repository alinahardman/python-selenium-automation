from behave import when


@when('Click Sign In')
def click_sign_in(context):
    context.app.sign_in_side_bar.click_sign_in()


@when('Input email')
def input_email(context):
    test_email = "future3pete@getmail1.com"  # Your test email
    context.app.sign_in_page.input_email(test_email)


@when('Click Continue')
def click_continue(context):
    context.app.sign_in_page.click_continue()


@when('Click use password')
def click_use_password(context):
    context.app.sign_in_page.click_use_password()


@when('Input password')
def input_password(context):
    test_password = "******"
    context.app.sign_in_page.input_password(test_password)


@when('Click Sign In With Password')
def click_sign_in_with_password(context):
    context.app.sign_in_page.click_sign_in_with_password()


@when('Click Skip Phone Number')
def skip_link(context):
    context.app.sign_in_page.skip_link()