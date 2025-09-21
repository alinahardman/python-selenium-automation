from behave import given, when, then


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_opened(context):
    context.app.terms_and_conditions_page.verify_terms_and_conditions_opened()


@when('Close current page')
def close_current_page(context):
    context.app.terms_and_conditions_page.close_current_page()


@then('Switch back to original')
def switch_back_to_previous(context):
    context.app.terms_and_conditions_page.switch_back_to_previous(context.original_window)