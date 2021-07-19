Feature: it returns buzz for multiples of five

Scenario: it returns buzz for five
When the user enters 5
Then they should get the word "buzz"

Scenario: it returns buzz for twenty-five
When the user enters 25
Then they should get the word "buzz"
