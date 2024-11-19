@qupos
Feature:payPerItem Feature

  @InitialSetup
  Scenario: Initial setup and Till Operations
    Given the user launches the "Qu POS" desktop application
    Then the user should be able to see the "Log In" and "Clock In" buttons
    When the user enter an employee "ID" on a counter login screen and select "Log In" button
    Then the user should be able to see the "Drive-Thru" dropdown in "orderWindow"

  @payPerItem
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
    | {"auto_id": "47587-47958"}  |  {"title": "#22 SAUSAGE CROISSANT"}  |   47587-47958-48058      |
    | {"auto_id": "47587-47958"}  |  {"title": "#23 LOADED BFST"}        |   47587-47958-48016      |
    | {"auto_id": "47587-56634"}  |  {"title": "2 TACOS"}                |   47587-56634-47708      |
    | {"auto_id": "47587-56634"}  |  {"title": "#1 SOURDOUGH JACK"}      |   47587-56634-47660      |
    Then each item should display in the cart view on the left side of the screen
    | itemsInCart                            |
    | {"title": "SAUSAGE CROISSANT"}         |
    | {"title": "LOADED BREAKFAST SANDWICH"} |
#    | {"title": "2 TACOS"}                   |
#    | {"title": "SOURDOUGH JACK"}            |
    And the subtotal, tax, and total should update as each item is added
    When the user selects the entrée "SAUSAGE CROISSANT" in the cart in "orderWindow"
    Then user should see "#22 SAUSAGE CROISSANT" entree is selected in "orderWindow"
    When the user removes a default modifier "SHELL EGG" by clicking "-" button in "orderWindow"
    Then the text "No SHELL EGG" should be displayed in the cart in "orderWindow"
    When the user adds a free modifier "MAYO" by clicking "+" button in "orderWindow"
    Then the text "ADD MAYO" should be displayed in the cart in "orderWindow"
    When the user adds a priced modifier "JALAPENOS" by clicking on it in "orderWindow"
    Then the text "Add JALAPENOS" should be displayed and the total should reflect the additional price of the modifier
    When the user clicks on the "Payment" button in "orderWindow"
    Then the user should be able to see the "ROUND UP DONATION" popup in "orderWindow"
    When the user clicks on the "NO THANKS" button in "orderWindow"
    Then the user should be able to see the "Cash" payment method in "paymentWindow"
    And the "Total" amount should match the total amount displayed in the cart
    When the user clicks on the "Cash" button in "paymentWindow"
    Then the "Due" amount should match the "Total" amount of the items in the cart
    When the user clicks on the "Pay per Item" button in "paymentWindow"
    Then the amount of each item in the "Select Check Items to Pay" pop-up should match the amount of the items displayed in the cart
    | itemsInPayPerItemPopup                                 |
    | {"auto_id": "PayPerItemItemPrice_47587-47958-48058"}    |
    | {"auto_id": "PayPerItemItemPrice_47587-47958-48016"}    |
    | {"auto_id": "PayPerItemItemPrice_47587-56634-47708"}   |
    | {"auto_id": "PayPerItemItemPrice_47587-56634-47660"}   |
    When the user selects the following items in the pop-up, click "OK" button and the total Amount for the selected item should match the due Amount
    |itemsInPayPerItemPopup                                               |
    | {"auto_id": "PayPerItemItemPrice_47587-47958-48058"}    |
    | {"auto_id": "PayPerItemItemPrice_47587-47958-48016"}    |
    And the user clicks on the "Apply Payment for Cash Payment" button in "paymentWindow"
    Then the sum of the "Tendered" amount and the "Due" amount should be equal to the "Total" amount
    When the user clicks on the "Cash" button in "paymentWindow"
    And the user clicks on the "Pay per Item" button in "paymentWindow"
    And the user selects the following items in the pop-up, click "OK" button
    |itemsInPayPerItemPopup                                               |
    | {"auto_id": "PayPerItemItemPrice_47587-56634-47708"}    |
    And the user clicks on the "Apply Payment for Cash Payment" button in "paymentWindow"
    Then the sum of the "Tendered" amount and the "Due" amount should be equal to the "Total" amount
    When the user clicks on the "Cash" button in "paymentWindow"
    And the user clicks on the "Apply Payment for Cash Payment" button in "paymentWindow"
    Then the "Total" amount should be zero and the "No Checks" text should be displayed
    When the user selects the "hamburgerMenu" in the bottom right corner in "orderWindow"
    Then the user should be able to see the "Claim/Close Till" button on the top navigation menu of the screen in "orderWindow"
    When the user clicks on the "Logout" button in "orderWindow"
    Then the user should be able to see the "Log In" and "Clock In" buttons
