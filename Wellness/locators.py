from selenium.webdriver.common.by import By

class LoginPageLocatars(object):
  EMAIL         = (By.ID, 'email--1')
  PASSWORD      = (By.ID, 'password--2')
  SIGN_IN       = (By.CSS_SELECTOR, '[class*="sign_in_button"]')
  ERROR_MESSAGE = (By.CSS_SELECTOR, '[class*="error__"]')