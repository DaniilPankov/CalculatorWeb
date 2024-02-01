Feature: Calculator

  Scenario: Addition
    Given I have a calculator on http://127.0.0.1:5000/calculator
    And I have entered 10 in dec in first entry
    And I have entered 5 in dec in second entry
    And I have chosen sum operation
    And I have chosen dec as type of result
    When I press button
    Then The result should be 15 on the screen

  Scenario: Subtraction
    Given I have a calculator on http://127.0.0.1:5000/calculator
    And I have entered 14 in dec in first entry
    And I have entered 7 in dec in second entry
    And I have chosen sub operation
    And I have chosen bin as type of result
    When I press button
    Then The result should be 111 on the screen

  Scenario: Multiplication
    Given I have a calculator on http://127.0.0.1:5000/calculator
    And I have entered 2 in dec in first entry
    And I have entered A in hex in second entry
    And I have chosen mul operation
    And I have chosen dec as type of result
    When I press button
    Then The result should be 20 on the screen

  Scenario: Division
    Given I have a calculator on http://127.0.0.1:5000/calculator
    And I have entered 10 in dec in first entry
    And I have entered 5 in dec in second entry
    And I have chosen div operation
    And I have chosen dec as type of result
    When I press button
    Then The result should be 2 on the screen

  Scenario: Division with remainder
    Given I have a calculator on http://127.0.0.1:5000/calculator
    And I have entered 2 in dec in first entry
    And I have entered B in hex in second entry
    And I have chosen mod operation
    And I have chosen bin as type of result
    When I press button
    Then The result should be 10 on the screen

  Scenario: Exponentiation
    Given I have a calculator on http://127.0.0.1:5000/calculator
    And I have entered 2 in dec in first entry
    And I have entered 111 in bin in second entry
    And I have chosen pow operation
    And I have chosen oct as type of result
    When I press button
    Then The result should be 200 on the screen

  Scenario: Division by zero in div
    Given I have a calculator on http://127.0.0.1:5000/calculator
    And I have entered 2 in dec in first entry
    And I have entered 0 in oct in second entry
    And I have chosen div operation
    And I have chosen hex as type of result
    When I press button
    Then An ZeroDivisionError should be raised

  Scenario: Division by zero in mod
    Given I have a calculator on http://127.0.0.1:5000/calculator
    And I have entered 2 in dec in first entry
    And I have entered 0 in hex in second entry
    And I have chosen mod operation
    And I have chosen bin as type of result
    When I press button
    Then An ZeroDivisionError should be raised

  Scenario: Input Error
    Given I have a calculator on http://127.0.0.1:5000/calculator
    And I have entered 10 in dec in first entry
    And I have entered hffghdd in hex in second entry
    And I have chosen mod operation
    And I have chosen bin as type of result
    When I press button
    Then An ValueError should be raised
