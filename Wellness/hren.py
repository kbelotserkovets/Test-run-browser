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

    def forgot_password(self, email):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://staging.onestopwellness.ai/')
        driver.find_element(*LoginPage.FORGOT_PASSWORD).click()
        email_field = driver.find_element(*LoginPage.EMAIL)
        email_field.send_keys(email)
        driver.find_element(*ForgotPassPage.NEXT).click()

    def open_user_settings(self):
        driver = self.driver
        user_avatar = driver.find_element(*DashboardPage.USER_AVATAR)
        self.hover_element(user_avatar)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((DashboardPage.PROFILE_MENU)))
        driver.find_element(*DashboardPage.SETTINGS).click()

    def page_has_loaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        print(page_state)
        return page_state == 'complete'

    def test_login_with_valid_data(self):
        self.user_sign_in("support@onestopwellness.ai", "5SdaG12pY2t0")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class*="__nav_bar_header"]')))
        self.assertEqual(self.driver.current_url, 'https://staging.onestopwellness.ai/dashboard', 'URL should contain "../dashboard"')

    def test_error_message_in_login_with_invalid_data(self):
        self.user_sign_in("support@onestopwellness.ai", "qwerty")
        error_message = self.driver.find_element_by_css_selector('[class*="error__"]').text
        self.assertIn(error_message, 'Invalid email or password, please try again')

    def test_user_login_with_empty_field(self):
        self.user_sign_in("", "")
        custom_login_error = self.driver.find_element(*LoginPage.ERROR_EMPTY_EMAIL_FIELD)
        custom_password_error = self.driver.find_element(*LoginPage.ERROR_EMPTY_PASSWORD_FIELD)
        self.assertTrue(custom_login_error.is_displayed())
        self.assertTrue(custom_password_error.is_displayed())

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

        self.assertEqual(first_name.get_attribute("value"), "Support")
        self.assertEqual(last_name.get_attribute("value"), "Noreply")
        self.assertEqual(age.get_attribute("value"), "30")


    def test_forgot_password(self):
        driver = self.driver
        self.forgot_password('leoproject@bk.ru')
        email_title = driver.find_element(*ForgotPassPage.EMAIL_TITLE).text
        small_email_title = driver.find_element(*ForgotPassPage.SMALL_EMAIL_TITLE).text
        self.assertEqual(email_title, 'CHECK YOUR EMAIL', 'Title should contain text: "CHECK YOUR EMAIL"')
        self.assertEqual(small_email_title, 'Please check your inbox, an email is on the way', 'Under "CHECK YOUR EMAIL" title, user should observe text: "Please check your inbox, an email is on the way"')
        driver.find_element(*ForgotPassPage.NEXT).click()
        self.assertEqual(driver.current_url, 'https://staging.onestopwellness.ai/signin', 'After send request for reset password, user should observe "Sign In" page')

    def test_forgot_password_for_not_existing_email(self):
        self.forgot_password('test@test.com')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class*="error_message"]')))
        error_message = self.driver.find_element(*ForgotPassPage.ERROR_MESSAGE).text
        self.assertEqual(error_message, 'User not found')

    def test_forgot_password_empty_field(self):
        self.forgot_password("")
        custom_error = self.driver.find_element(*ForgotPassPage.ERROR_EMPTY_EMAIL)
        self.assertTrue(custom_error.is_displayed())


    def test_sign_in_button_on_forgot_password_form(self):
        self.forgot_password("")
        self.driver.find_element(*ForgotPassPage.SIGN_IN).click()
        self.assertEqual(self.driver.current_url, 'https://staging.onestopwellness.ai/signin', 'After send request for reset password, user should observe "Sign In" page')



if __name__ == '__main__':
    unittest.main()