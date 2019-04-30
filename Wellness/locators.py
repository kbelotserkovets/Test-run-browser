from selenium.webdriver.common.by import By


class LoginPage(object):

    EMAIL              = (By.ID, 'email--1')
    PASSWORD           = (By.ID, 'password--2')
    SIGN_IN            = (By.CSS_SELECTOR, '[class*="sign_in_button"]')
    ERROR_MESSAGE      = (By.CSS_SELECTOR, '[class*="error__"]')

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