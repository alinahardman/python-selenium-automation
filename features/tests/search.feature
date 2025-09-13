Feature: Tests for Target search functionality

  Scenario: User can search for tea on Target
    Given Open target main page
    When Search for tea
    Then Verify search results are shown for tea


  Scenario: User can search for bottle on Target
    Given Open target main page
    When Search for bottle
    Then Verify search results are shown for bottle


  Scenario: User can search for mug on Target
    Given Open target main page
    When Search for mug
    Then Verify search results are shown for mug



