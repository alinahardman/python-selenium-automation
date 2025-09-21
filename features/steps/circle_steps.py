from behave import given, then


@given('Open circle page')
def open_circle(context):
    context.app.circle_page.open_circle()


@then('At least 10 Benefit cells are shown')
def benefit_cells_count(context):
    context.app.circle_page.benefit_cells_count()

