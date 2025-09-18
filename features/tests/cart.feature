Feature: Tests for Cart feature

  Scenario: Verify that 'Your cart is empty' message is shown.
    Given Open target main page
    When Click on Cart icon
    Then Your cart is empty message is shown

   Scenario: Verify product is added to cart.
     Given Open target main page
     When Search for mug
     And Click on Add to Cart button
     And Store product name
     And Confirm Add to Cart button from side navigation
     And Click View Cart & Check Out
     Then Verify cart has correct product




