import json
import time

from selenium.webdriver.common.by import By

from core_layer.driver_manager.selenium_driver import SeleniumDriver, waits_config
from core_layer.utility.selenium_utilities import SafeActions
from test_project.features.steps.childPricingForDrinks import driver


class commonAction:

    SignIn = (By.XPATH, '//span[text()="Sign In"]')
    jackInTheBoxLogo = (By.CLASS_NAME, '[class="c-navbar__nav__logo"]')
    orderNowButton = (By.CLASS_NAME, '[class="c-navbar__order-now btn--primary--sm"]')
    exploreOurMenuText = (By.XPATH, '//h2[text()="Explore Our Menu"]')
    burgerCombosButton = (By.XPATH, '//h5[text()="Burger Combos"]')
    burgerCombosMenu = (By.XPATH, '//h2[text()="Burger Combos"]')
    tripleBonusJackCombo = (By.XPATH, '//p[text()="Triple Bonus Jack® Combo"]')
    tripleBonusJackComboText = (By.XPATH, '//h1[text()="Triple Bonus Jack® Combo"]')
    bagIcon = (By.XPATH, '//*[@id="navbar"]/div[2]/button[2]/svg/use')
    checkoutButton = (By.CLASS_NAME, '[class="btn--primary"]')
    defaultTestCard = (By.CLASS_NAME, '[class="payment__saved__content ng-star-inserted"]')
    continueButton = (By.XPATH, '//button[contains(text(), "Continue")]')
    driveThru = (By.XPATH, '//span[contains(text(), "Drive-Thru")]')
    carryout = (By.XPATH, '//span[contains(text(), "Carry-Out")]')

    def __init__(self):
        self.driver = SeleniumDriver()
        self.safeActions = SafeActions()

    def isVisible(self, locator, friendlyElement):
        self.safeActions.wait_until_visible(locator, friendlyElement, waits_config['shortWait'])

    def clickButton(self, locator, friendlyElement):
        self.safeActions.safe_click(locator, friendlyElement, waits_config['shortWait'])

