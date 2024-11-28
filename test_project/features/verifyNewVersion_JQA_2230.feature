@qpos
Feature:verifyNewVersion Feature

  @verifyNewVersion
  Scenario:
    Given the user launches the "Qu POS" desktop application
    Then the user should be able to see the version of the application
    When the user enter an employee "ID" on a counter login screen and select "Log In" button
    Then the user should be able to see the "Drive-Thru" dropdown in "orderWindow"
    When the user selects the "hamburgerMenu" in the bottom right corner in "orderWindow"
    Then the user should be able to see the "Claim/Close Till" button on the top navigation menu of the screen in "orderWindow"
    When the user clicks on the "Search Closed Checks" button in "orderWindow"
    Then the application version displayed in the "Search Closed Checks" window should match the version retrieved from the "LogIn" window
    When the user clicks on the "Back arrow" button in "closedChecksWindow"
    Then the user should be able to see the "Drive-Thru" dropdown in "orderWindow"
    When the user selects the "hamburgerMenu" in the bottom right corner in "orderWindow"
    Then the user should be able to see the "Claim/Close Till" button on the top navigation menu of the screen in "orderWindow"
    When the user clicks on the "More" button in "orderWindow"
    Then the application version displayed in the "Information and Tools" window should match the version retrieved from the "LogIn" window
    When the user clicks on the "Terminal Configuration" button in "informationAndToolsWindow"
    Then the user should be able to see the "Configuration" button in "informationAndToolsWindow"
    And the user should be able to see the "Menus" button in "informationAndToolsWindow"
    When the user clicks on the "Configuration" button in "informationAndToolsWindow"
    Then the software version displayed in the "Terminal Configuration" should match the version retrieved from the "LogIn" window
    When the user clicks on the "Return to Dashboard" button in "informationAndToolsWindow"
    Then the user should be able to see the "Configuration" button in "informationAndToolsWindow"
    And the user should be able to see the "Menus" button in "informationAndToolsWindow"
    When the user clicks on the "close" button in "informationAndToolsWindow"
    Then the user should be able to see the "Terminal Configuration" button in "informationAndToolsWindow"
    When the user clicks on the "Back arrow" button in "closedChecksWindow"
    Then the user should be able to see the "Drive-Thru" dropdown in "orderWindow"
    When the user selects the "hamburgerMenu" in the bottom right corner in "orderWindow"
    Then the user should be able to see the "Claim/Close Till" button on the top navigation menu of the screen in "orderWindow"
    When the user clicks on the "Logout" button in "orderWindow"
    Then the user should be able to see the "Log In" button in "loginWindow"
    And the user should be able to see the "Clock In" button in "loginWindow"