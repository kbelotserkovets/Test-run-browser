import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import *


class Login_Page_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        self.driver.implicitly_wait(5)

    def hover_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def user_sign_in(self, login, passwrd):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://staging.onestopwellness.ai/')
        username = driver.find_element(*LoginPageLocators.EMAIL)
        password = driver.find_element(*LoginPageLocators.PASSWORD)
        username.send_keys(login)
        password.send_keys(passwrd)

        driver.find_element(*LoginPageLocators.SIGN_IN).click()

    def open_user_settings(self):
        driver = self.driver
        user_avatar = driver.find_element(*DashboardPageLocators.USER_AVATAR)
        self.hover_element(user_avatar)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((DashboardPageLocators.PROFILE_MENU)))

        driver.find_element(*DashboardPageLocators.SETTINGS).click()


    def test_login_with_valid_data(self):
        self.user_sign_in("support@onestopwellness.ai", "5SdaG12pY2t0")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class*="__nav_bar_header"]')))
        self.assertEqual(self.driver.current_url, 'https://staging.onestopwellness.ai/dashboard', 'URL should contain "../dashboard"')


    def test_error_message_in_login_with_invalid_data(self):
        self.user_sign_in("support@onestopwellness.ai", "qwerty")
        error_message = self.driver.find_element_by_css_selector('[class*="error__"]').text

        self.assertIn(error_message, 'Invalid email or password, please try again')

    # def test_login_with_empty_field(self):
    #     self.user_sign_in("", "")
    #     error_class = self.driver.find_elements_by_css_selector('[class*="custom_error"]')
    #
    #     # WebDriverWait(driver, 10).until(
    #     #     EC.visibility_of_all_elements_located(error_class))
    #
    #     for error in error_class:
    #         self.assertIn(error, username)
    #         self.assertIn(error, password)

    def test_change_user_name(self):
        self.user_sign_in("support@onestopwellness.ai", "5SdaG12pY2t0")
        driver = self.driver

        self.open_user_settings()

        first_name = driver.find_element(*SettingsPageLocators.FIRST_NAME)
        last_name = driver.find_element(*SettingsPageLocators.LAST_NAME)
        age = driver.find_element(*SettingsPageLocators.AGE)
        gender_female = driver.find_element(*SettingsPageLocators.GENDER_FEMALE)

        first_name.clear()
        first_name.send_keys("John")

        last_name.clear()
        last_name.send_keys("Doe")

        age.clear()
        age.send_keys("30")

        gender_female.click()

        driver.find_element(*SettingsPageLocators.SAVE_CHANGES).click()

        self.open_user_settings()

        self.assertIn(first_name, "John")





    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
