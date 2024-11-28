@qpos
Feature:creditCardPayment Feature

  @InitialSetup
  Scenario: Initial setup and Till Operations
    Given the user launches the "Qu POS" desktop application
    Then the user should be able to see the "Log In" button in "loginWindow"
    And the user should be able to see the "Clock In" button in "loginWindow"
    When the user enter an employee "ID" on a counter login screen and select "Log In" button
    Then the user should be able to see the "Drive-Thru" dropdown in "orderWindow"

  @creditCardPayment
  Scenario:
    When the user selects the "hamburgerMenu" in the bottom right corner in "orderWindow"
    Then the user should be able to see the "Claim/Close Till" button on the top navigation menu of the screen in "orderWindow"
    And the user should be able to see the "Show Open Checks" button on the top navigation menu of the screen in "orderWindow"
    When the user clicks on the "Claim/Close Till" button in "orderWindow"
    Then the user should be able to see the "Till Device Selection" popup in "orderWindow"
    When the user select "Claim" on an available till and verify the "Till, Successfully Claimed!" text and "current cash"
    And the user clicks on the "close" button on the till pop-up in "orderWindow"
    Then the user should be able to see the "Drive-Thru" dropdown in "orderWindow"

   When the user adds multiple entree items to the order
    | menuOption                  |    itemName                          |        autoIdOfItem      |
    | {"auto_id": "47587-56634"}  |  {"title": "HAMBURGER"}              |   47587-56634-48003      |
    Then each item should display in the cart view on the left side of the screen
    | itemsInCart                                                                                |
    | {"title": "HAMBURGER", "auto_id":"CheckItemText_Item-0-47587-56634-48003"}                  |
    And the subtotal, tax, and total should update as each item is added


    When the user clicks on the "Payment" button in "orderWindow"
    Then the user should be able to see the "ROUND UP DONATION" popup in "orderWindow"
    When the user clicks on the "NO THANKS" button in "orderWindow"
    Then the user should be able to see the "Offline Credit" payment method in "paymentWindow"
    And the "Total" amount should match the total amount displayed in the cart
    When the user clicks on the "Offline Credit" button in "paymentWindow"
    Then the "Due" amount for Offline Credit Card Payment should match the "Total" amount of the items in the cart
    When the user clicks on the "Apply Payment for Offline Credit Payment" button in "paymentWindow"
    Then the "Apply Payment" confirmation pop-up and the text "Apply & <Due amount> payment + $0.00 tip, and close check?" should be displayed
    When the user clicks on the "OK" button in "orderWindow"
    Then the user should be able to see the "Check Closed!" popup in "orderWindow"
    When the user clicks on the "OK" button in "orderWindow"
    Then the "Total" amount should be zero and the "No Checks" text should be displayed
    When the user selects the "hamburgerMenu" in the bottom right corner in "orderWindow"
    Then the user should be able to see the "Claim/Close Till" button on the top navigation menu of the screen in "orderWindow"
    When the user clicks on the "Logout" button in "orderWindow"
    Then the user should be able to see the "Log In" button in "loginWindow"
    And the user should be able to see the "Clock In" button in "loginWindow"