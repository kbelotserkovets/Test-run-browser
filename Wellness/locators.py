from selenium.webdriver.common.by import By


class LoginPage(object):

    EMAIL              = (By.NAME, 'email')
    PASSWORD           = (By.NAME, 'password')
    SIGN_IN            = (By.CSS_SELECTOR, '[class*="sign_in_button"]')
    ERROR_MESSAGE      = (By.CSS_SELECTOR, '[class*="error__"]')
    FORGOT_PASSWORD    = (By.CSS_SELECTOR, '[class*="forgot_pass"]')
    ERROR_EMPTY_EMAIL_FIELD  = (By.CSS_SELECTOR, '[class*="login_form"] > [class*="custom_error"]')
    ERROR_EMPTY_PASSWORD_FIELD  = (By.CSS_SELECTOR, '[class*="password_field"] > [class*="custom_error"]')


class ForgotPassPage(object):
    NEXT               = (By.CSS_SELECTOR, '[class*="btn_issue_details"]')
    SIGN_IN            = (By.CSS_SELECTOR, '[class*="sign_in"]')
    EMAIL_TITLE        = (By.CSS_SELECTOR, '[class*="email_title__"]')
    SMALL_EMAIL_TITLE  = (By.CSS_SELECTOR, '[class*="email_title_item"]')
    ERROR_MESSAGE      = (By.CSS_SELECTOR, '[class*="error_message"]')
    ERROR_EMPTY_EMAIL  = (By.CSS_SELECTOR, '[class*="custom_error"]')

class DashboardPage(object):

    USER_AVATAR        = (By.CSS_SELECTOR, 'div[class*="right_column_menu"] > div[class*="user_information"] > div[class*="user_profile"] > div[class*="user_photo"]')
    SETTINGS           = (By.CSS_SELECTOR, '[class*="right_column_menu"] [class*="profile_menu"] > [class*="menu_items_container"] > [class*="menu_items"] > li > [href="/settings"]')
    PROFILE_MENU       = (By.CSS_SELECTOR, 'div[class*="right_column_menu"] > div[class*="user_information"] > div[class*="user_profile"] > div[class*="profile_menu"] > div[class*="menu_items_container"]')
    HEADER             = (By.CSS_SELECTOR, '[class*="__nav_bar_header"]')
    NOTIFICATION_BELL  = (By.CSS_SELECTOR, 'div[class*="header"] div[class*="notification_icon"]')
    DAILY_PROGRESS     = (By.CSS_SELECTOR, '[class*="daily_progress_container"]')

class SettingsPage(object):

    FIRST_NAME         = (By.NAME, 'firstName')
    LAST_NAME          = (By.NAME, 'lastName')
    AGE                = (By.NAME, 'age')
    GENDER_MALE        = (By.CSS_SELECTOR, '[value="Male"]')
    GENDER_FEMALE      = (By.CSS_SELECTOR, '[value="Female"]')
    SAVE_CHANGES       = (By.CSS_SELECTOR, '[class*="button_save_changes"]')