import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Page_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")

    def hover_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def test_login_with_valid_data(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://staging.onestopwellness.ai/')

        username = driver.find_element_by_id("email--1")
        password = driver.find_element_by_id("password--2")

        username.send_keys("support@onestopwellness.ai")
        password.send_keys("5SdaG12pY2t0")

        driver.find_element_by_css_selector('[class*="sign_in_button"]').click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[class*="__nav_bar_header"]')))

        self.assertEqual(driver.current_url, 'https://staging.onestopwellness.ai/dashboard', 'URL should contain "../dashboard"')


    def test_error_message_in_login_with_invalid_data(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://staging.onestopwellness.ai/')

        username = driver.find_element_by_id("email--1")
        password = driver.find_element_by_id("password--2")

        username.send_keys("support@onestopwellness.ai")
        password.send_keys("password")

        driver.find_element_by_css_selector('[class*="sign_in_button"]').click()

        error_message = driver.find_element_by_css_selector('[class*="error__"]').text

        self.assertIn(error_message, 'Invalid email or password, please try again')


    # def test_login_with_empty_field(self):
    #     driver = self.driver
    #     driver.maximize_window()
    #     driver.implicitly_wait(5)
    #     driver.get('https://staging.onestopwellness.ai/')
    #
    #     username = driver.find_element_by_id("email--1")
    #     password = driver.find_element_by_id("password--2")
    #     #
    #     # username.send_keys("support@onestopwellness.ai")
    #     # password.send_keys("password")
    #
    #     driver.find_element_by_css_selector('[class*="sign_in_button"]').click()
    #
    #     error_class = driver.find_elements_by_css_selector('[class*="custom_error"]')
    #     #
    #     # WebDriverWait(driver, 10).until(
    #     #     EC.visibility_of_all_elements_located(error_class))
    #
    #     for error in error_class:
    #         self.assertIn(error, username)
    #         self.assertIn(error, password)


    def test_change_user_name(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://staging.onestopwellness.ai/')

        username = driver.find_element_by_id("email--1")
        password = driver.find_element_by_id("password--2")

        username.send_keys("support@onestopwellness.ai")
        password.send_keys("5SdaG12pY2t0")

        driver.find_element_by_css_selector('[class*="sign_in_button"]').click()

        user_photo = driver.find_element_by_css_selector('')
        header > div > div[

        class *="right_column_menu"] > div[class *= "user_information"] > div[class *= "user_profile] > div[class*="user_photo"]
        self.hover_element()


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
