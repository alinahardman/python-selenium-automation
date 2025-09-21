
Feature: Terms and Conditions Link

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target main page
    When Click Account
      #    from side bar
    When Click Sign In
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    When Close current page
    Then Switch back to original

