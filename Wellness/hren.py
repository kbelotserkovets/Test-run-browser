import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import *
import time


class Login_Page_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./Wellness/chromedriver")
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()

    def hover_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def user_sign_in(self, login, passwrd):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://staging.onestopwellness.ai/')
        username = driver.find_element(*LoginPage.EMAIL)
        password = driver.find_element(*LoginPage.PASSWORD)
        username.send_keys(login)
        password.send_keys(passwrd)

        driver.find_element(*LoginPage.SIGN_IN).click()

    def open_user_settings(self):
        driver = self.driver
        user_avatar = driver.find_element(*DashboardPage.USER_AVATAR)
        self.hover_element(user_avatar)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((DashboardPage.PROFILE_MENU)))
        driver.find_element(*DashboardPage.SETTINGS).click()


    def test_login_with_valid_data(self):
        self.user_sign_in("support@onestopwellness.ai", "5SdaG12pY2t0")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class*="__nav_bar_header"]')))
        self.assertEqual(self.driver.current_url, 'https://staging.onestopwellness.ai/dashboard', 'URL should contain "../dashboard"')


    def test_error_message_in_login_with_invalid_data(self):
        self.user_sign_in("support@onestopwellness.ai", "qwerty")
        error_message = self.driver.find_element_by_css_selector('[class*="error__"]').text

        self.assertIn(error_message, 'Invalid email or password, please try again')

    def page_has_loaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        print(page_state)
        return page_state == 'complete'


    def test_change_user_name(self):
        driver = self.driver
        self.user_sign_in("support@onestopwellness.ai", "5SdaG12pY2t0")

        self.open_user_settings()

        first_name = driver.find_element(*SettingsPage.FIRST_NAME)
        last_name = driver.find_element(*SettingsPage.LAST_NAME)
        age = driver.find_element(*SettingsPage.AGE)
        gender_female = driver.find_element(*SettingsPage.GENDER_FEMALE)

        first_name.clear()
        first_name.send_keys("Support")

        last_name.clear()
        last_name.send_keys("Noreply")

        age.clear()
        age.send_keys("30")

        gender_female.click()

        driver.find_element(*SettingsPage.SAVE_CHANGES).click()

        WebDriverWait(self.driver, 10).until(EC.url_contains("dashboard"))

        self.open_user_settings()

        first_name = driver.find_element(*SettingsPage.FIRST_NAME)
        last_name = driver.find_element(*SettingsPage.LAST_NAME)
        age = driver.find_element(*SettingsPage.AGE)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME,"firstName")))
        self.page_has_loaded() == True
        print(first_name.get_attribute("value"))
        print(last_name.get_attribute("value"))
        print(age.get_attribute("value"))

        self.assertEqual(first_name.get_attribute("value"), "Support")
        self.assertEqual(last_name.get_attribute("value"), "Noreply")
        self.assertEqual(age.get_attribute("value"), "30")


if __name__ == '__main__':
    unittest.main()