Feature: We can search for items on Amazon.com

Scenario: Toys for sale include LEGO
    Given that we have gone to www.amazon.com
     When we search for "toys"
     Then we find items from "LEGO"
     
Scenario Outline: search for any product
    Given that we have gone to www.amazon.com
     When we search for "<product>"
     Then we find items from "<vendor>"
     
Examples: Various things
  | product  | vendor |
  | t-shirts | Hanes  |
  | Apple TV | Apple  |
  | toys     | LEGO   |
