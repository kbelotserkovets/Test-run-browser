import os
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

current_dir = os.path.dirname(__file__)

def getDriverByPlatform():
    if sys.platform == 'linux':
        return 'chromedriver'
    elif sys.platform == 'darwin':
        return 'chromedriver_mac'
    elif sys.platform == 'win32':
        return 'chromedriver.exe'


browser = webdriver.Chrome(executable_path=os.path.join(current_dir, getDriverByPlatform())) # Path to Chrome webdriber
browser.get('http://www.google.com')

element = browser.find_element_by_name('q')  # Find the search box
element.send_keys('Selenide' + Keys.RETURN)  # Input word "Selenide" and start search

# RESULTS_LOCATOR = "#ires .g"
#
# WebDriverWait(browser, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, RESULTS_LOCATOR)))

elements = browser.find_elements_by_css_selector("#ires .g")
print(elements[0].text)

assert 'Google' in browser.title
assert "Selenide" in elements[0].text

browser.quit() # This is optional