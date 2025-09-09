Feature: Tests for Sign In feature

  Scenario: Verify that user can navigate to Sign In.
    Given Open target main page
    When Click Account
    When Click Sign In
    Then Sign In form opened

