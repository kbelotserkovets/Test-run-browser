from selenium.webdriver.common.by import By

class LoginPageLocators(object):

    EMAIL         = (By.ID, 'email--1')
    PASSWORD      = (By.ID, 'password--2')
    SIGN_IN       = (By.CSS_SELECTOR, '[class*="sign_in_button"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[class*="error__"]')

class SettingsPageLocators(object):

    FIRST_NAME    = (By.ID, 'firstName--3')
    LAST_NAME     = (By.ID, 'lastName--4')
    AGE           = (By.ID, 'age--5')
    GENDER_MALE   = (By.CSS_SELECTOR, 'value="Male"')
    GENDER_FEMALE = (By.CSS_SELECTOR, 'value="Female"')
    SAVE_CHANGES  = (By.CSS_SELECTOR, '[class*="button_save_changes"]')