import os
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

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

elem = browser.find_element_by_name('q')  # Find the search box
elem.send_keys('Selenide' + Keys.RETURN)  # Input word "Selenide" and start search

#  Проверка результатов поиска
search_result = browser.find_elements(
     by=By.CSS_SELECTOR,
     value='#rso .srg div.g'
    )
assert len(search_result) > 0
for result in search_result:
    title_text = result.find_element_by_tag_name('h3').text
    assert 'Selenide' in title_text


# RESULTS_LOCATOR = "//div/h3/a"
#
# WebDriverWait(browser, 10).until(
#     EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))
#
# page1_results = browser.find_elements(By.XPATH, RESULTS_LOCATOR)
#
# for item in page1_results:
#     print(item.text)

assert 'Google' in browser.title
# browser.quit() # This is optional, for closing browser