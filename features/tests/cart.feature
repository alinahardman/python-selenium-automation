Feature: Tests for Cart feature
  # clicks on the cart icon and verifies that “Your cart is empty” message is shown.

  Scenario: Verify that 'Your cart is empty' message is shown.
    Given Open target main page
    When Click on Cart icon
    Then Your cart is empty message is shown


