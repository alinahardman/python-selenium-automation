Feature: Tests for Sign In feature

  Scenario: Verify that user can navigate to Sign In
    Given Open target main page
    When Click Account
    When Click Sign In
    Then Sign In form opened

  Scenario: Verify that user can Sign In
    Given Open target main page
    When Click Account
    When Click Sign In
    Then Sign In form opened
    When Input email
    And Click Continue
    And Click use password
    And Input password
    And Click Sign In With Password
#   And Click Skip Phone Number
   Then Verify user is logged in

