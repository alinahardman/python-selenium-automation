from behave import given, when


@when('Store original window')
def store_window(context):
    context.original_window = context.app.sign_in_page.get_original_window()
    print('Original window: ', context.original_window)


@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions(context):
    context.app.sign_in_page.click_target_terms_and_conditions()


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


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.page.switch_to_newly_opened_window([context.original_window])



