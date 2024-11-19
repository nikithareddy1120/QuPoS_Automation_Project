@qupos
Feature:childPricingForSides Feature

  @InitialSetup
  Scenario: Initial setup and Till Operations
    Given the user launches the "Qu POS" desktop application
    Then the user should be able to see the "Log In" and "Clock In" buttons
    When the user enter an employee "ID" on a counter login screen and select "Log In" button
    Then the user should be able to see the "Drive-Thru" dropdown in "orderWindow"

  @childPricingForSides
  Scenario:
    When the user selects the "hamburgerMenu" in the bottom right corner in "orderWindow"
    Then the user should be able to see the "Claim/Close Till" button on the top navigation menu of the screen in "orderWindow"
    And the user should be able to see the "Show Open Checks" button on the top navigation menu of the screen in "orderWindow"
    When the user clicks on the "Claim/Close Till" button in "orderWindow"
    Then the user should be able to see the "Till Device Selection" popup in "orderWindow"
    When the user select "Claim" on an available till and verify the "Till, Successfully Claimed!" text and "current cash"
    And the user clicks on the "close" button on the till pop-up in "orderWindow"
    Then the user should be able to see the "Drive-Thru" dropdown in "orderWindow"
     When the user adds combo item to the order
       | menuOption                  |    itemName                           | comboSize        |        autoIdOfItem      |
       | {"auto_id": "47587-56634"}  | {"title":"#4 BACON ULTIMATE CHBURGER"}| {"title":"SMALL"}|   47587-56634-48037      |
     Then each item should display in the cart view on the left side of the screen
      | itemsInCart                                            |
      | {"title":"#4 BACON ULTIMATE CHEESEBURGER COMBO (S)" }    |
    When the user clicks on the "Sides" button in "orderWindow" and get small Amount of Sides
    Then the user should be able to see the "Fries" option in "orderWindow"
    When the user clicks on the "FRENCH FRIES" button in "orderWindow"
    Then the user should be able to see the "Medium" option in "orderWindow"
    And the user should be able to see the "Large" option in "orderWindow"
    When the user clicks on the "Large" button in "orderWindow"
    Then the upCharge for large french Fries should be added to the total amount, and the item should be displayed in the cart view
    When the user clicks on the "3 EGG ROLLS" button in "orderWindow"
    Then the upCharge for 3 EGG ROLLS should be added to the total amount, and the item should be displayed in the cart view
    When the user clicks on the "1 EGG ROLL" in sides button in "orderWindow"
    Then no upCharge for sides should be added to the total amount, and the item should be displayed in the cart view
    When the user clicks on the "Payment" button in "orderWindow"
    Then the user should be able to see the "ROUND UP DONATION" popup in "orderWindow"
    When the user clicks on the "NO THANKS" button in "orderWindow"
    Then the user should be able to see the "Cash" payment method in "paymentWindow"
    And the "Total" amount should match the total amount displayed in the cart
    When the user clicks on the "Cash" button in "paymentWindow"
    Then the "Due" amount should match the "Total" amount of the items in the cart
    When the user clicks on the "Apply Payment for Cash Payment" button in "paymentWindow"
    Then the "Total" amount should be zero and the "No Checks" text should be displayed
    When the user selects the "hamburgerMenu" in the bottom right corner in "orderWindow"
    Then the user should be able to see the "Claim/Close Till" button on the top navigation menu of the screen in "orderWindow"
    When the user clicks on the "Logout" button in "orderWindow"
    Then the user should be able to see the "Log In" and "Clock In" buttons
