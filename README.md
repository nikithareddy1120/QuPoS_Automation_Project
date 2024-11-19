# Qualiframe-lite Desktop #

## Introduction:

> Automation framework developed using Python + WinAppDriver + PyWinAuto + BDD with Page Object Model which can be used across various Windows desktop applications on Windows 10 or above.

## Dependencies
The versions for some of the below packages can be found in the requirements.txt file:
 - Selenium with WinAppDriver - Desktop automation
 - PyWinAuto - Desktop automation
 - Allure, Behave html - Reporting

## Prerequisites
 - __pycharm__ (preferred IDE)
    - Download and install [pycharm-community](https://www.jetbrains.com/pycharm/download/)
 - __Python__
    - Version: `python-3.xx`
	- Download and install [Website](https://www.python.org/downloads/)
    - After successfull completion of installation, add the below python paths to Environment Variables
      - C:\Users\<yourname>\AppData\Roaming\Python\Python3xx\Scripts
      - C:\Users\<yourname>\AppData\Roaming\Python\Python3xx\site-packages
 - __WinAppDriver__
   - Download and install [WinAppDriver](https://github.com/Microsoft/WinAppDriver/releases)
 - __WindowsSDK__
   - Download and install [Windows-SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/)

For assistance with WinAppDriver and PyWinAuto, please refer to the following resources:
- [WinAppDriver](https://github.com/microsoft/WinAppDriver)
- [PyWinAuto](https://pywinauto.readthedocs.io/en/latest/)

## How to use: 

   - **Clone the Repository**
    - Use the following command to clone the repository:
      ```
      git clone <repository-url>
      ```
   - Import the project in PyCharm IDE.

   - After importing the Framework, the Project Structure will look like below:

   ``` 
     |- qualiframelite-desktop-coe
     |   |- .circleci
     |   |   |- config.yml
     |   |- config
     |   |   |- config_reader.py                          # config file reader
     |   |- core_layer
     |   |   |- driver_manager
     |   |   |   |- application_driver.py                 
     |   |   |   |- driver_factory.py                     
     |   |   |   |- pywinauto_driver.py                   # PyWinAuto driver
     |   |   |   |- winappdriver_driver.py                # WinApp driver
     |   |   |- utility
     |   |   |   |- assertions.py                         # assertions
     |   |   |   |- pywinauto_utilities.py                # utilities related to PyWinAuto
     |   |   |   |- winappdriver_utilities.py             # utilities related to WinAppDriver
     |   |   |   |- yamlManager.py 
     |   |- Reports
     |   |   |- allureReport
     |   |   |- htmlReport
     |   |   |- Logs
     |   |   |   |- LatestLogs_CurrentTimeStamp           # logs
     |   |   |   |   |- Logs.log 
     |   |- test_project 
     |   |   |- business_layer
     |   |   |   |- windows                               # Windows                                                       
     |   |   |- features                                  # feature files
     |   |   |- steps                                     # step definition files
     |   |- .gitignore
     |   |- behave.ini                                    # behave configuration 
     |   |- config.cfg                                    # config file
     |   |- InstallRequirements.bat                       # Batch file for installing requirements
     |   |- log_file.py                                   # logging configuration
     |   |- README.md                                     # README file
     |   |- requirements.txt                              # requirements file
     |   |- RUnTests.bat                                  # Batch file to run tests
```

   - In Pycharm `Goto File > Settings > Python interpreter, add python 3.xx interpreter(Location of Python installed)` and Click Ok
   - If you see `install requirements` pop-up/alert in Pycharm , Please click on it to install libraries. (or) Follow the below step
   - Install required ` python libraries` by executing `InstallRequirements.bat`file
      * Open "..\qualiframelite-desktop-coe" from file explorer and double-click the "installRequirements.bat" to install the requirements.

## Configuration Settings

- **WinAppDriver configuration**:
    - Update the following parameter in the `qualiframelite-desktop-coe > config.cfg` file:
    ```
      [Framework]
      type = winappdriver
  
- **PyWinAuto configuration**:
    - Update the following parameter in the `qualiframelite-desktop-coe > config > config.py` file:
    ```
      [Framework]
      type = pywinauto
    ```

## Configure the Runner

* To execute the particular tests based on markers,
    * Add marker to scenario as below and execute them by using the command `behave --tags=testing`
```
   @testing
   Scenario:
```
* To execute all the test cases in the feature file based on markers,
    * Add marker to the feature as below and execute them by using the command `behave --tags=Calculator`
```
    @Calculator
    Feature: Calculation Feature
```

* Use the below commands to execute the tests and generate the reports
``` 
    behave --tags=testing -f html -o Reports/htmlReport/report.html -f allure_behave.formatter:AllureFormatter -o Reports\allureReport\allure_results
    allure generate --clean Reports\allureReport\allure_results -o Reports\allureReport\allure_report
    allure open Reports\allureReport\allure_report
```
   
- Change the tag name based on the markers given in the Feature file
- To view the Allure report, open the index.html file in any of the browser which is installed in your system
- To view the Behave html report, open the report.html file in any of the browser which is installed in your system

## Execution

- Use the above behave commands which are mentioned in the "Configure the runner"

                                        OR

- Navigate to "..\qualiframelite-desktop-coe" and double click "RunTests.bat" file.

## What happens when a batch file is triggered...
 - After the successful execution of the tests, the logs will be saved in the `Reports/Logs` folder with the file name `LatestLogs`, including the current timestamp
    - Project Structure for Logs:

              |- Reports 
              |   |- allureReport
              |   |- htmlReport
              |   |- Logs
              |   |   |- LatestLogs_10_07_2024_10_37_29  

 - Reports will be generated and saved under `Reports` folder.
   - Project Structure for Reports:

                |- Reports
                |   |- allureReport
                |   |   |- allure_report  
                |   |   |- index.html
                |   |- allure_results  
                |   |- htmlReport
                |   |   |- report.html

   - To view the Allure report, open the index.html file in any of the browser which is installed in your system 
   - To view the Behave html report, open the report.html file in any of the browser which is installed in your system
    
## Features:

 - _Batch File Execution_
   - Execute tests by simply executing batch files:
    - Windows: Execute the tests by double-click on a `RunTests.bat` file
      - example code: 
   ```
    behave --tags=testing -f html -o Reports/htmlReport/report.html -f allure_behave.formatter:AllureFormatter -o Reports\allureReport\allure_results
    allure generate --clean Reports\allureReport\allure_results -o Reports\allureReport\allure_report
    allure open Reports\allureReport\allure_report
   ```

 - _Logging_
    - Logging is used to include your own messages. Logs file is created in location "Reports/Logs/LatestLogs_currentTimestamp"

 - _Reporting_
   - After the batch file execution the results are saved in 'allure_results' folder in json format, based on the results allure report will be generated and stored in the "allureReport/allure_report" folder.
   - Behave html report is also generated and stored in the 'htmlReport' folder

## TODO : Add Circle CI integration
 - Install Remote Desktop Service from the Server Manager > Add Roles and Features.
 - Navigate to Circle CI url and Sign in Using Your GitHub Account 
 - Once you logged in, specify which GitHub repositories CircleCI should manage. 
 - You can select either All repositories for broad access, or limit CircleCI to specific repositories.
 - Set Up a New Project
   - Click on the Projects tab on your CircleCI dashboard.
   - Under Projects, find the GitHub repository where your code resides and click Set Up Project.
   - After clicking Set Up Project, CircleCI will search for a `.circleci/config.yml` file in your repository's root.
 - Create a resource class and install the CircleCI runner for a self-hosted agent using [CircleCI Runner installation](https://circleci.com/docs/machine-runner-3-manual-installation-on-windows/)
 - Open powershell as an admin mode and navigate to the folder where the CircleCI is installed and run the below command to run the self hosted agent.
   - "./circleci-runner.exe machine --config machine-runner-config.yaml"
 - After running the above command the runner will be detected in the CircleCI self-hosted agent tab.
 - Commit and push the code to the git, Once pushed, CircleCI will automatically detect the configuration and trigger the pipeline.

## Contribution guidelines
	* If you have any issues with framework, please contact Automation CoE Team
	* If you have a fix for any existing problem, please submit a pull request (https://gitlab.com/qualitest.group/general/development/cloudassuranceservices/qualiframe-desktop)
