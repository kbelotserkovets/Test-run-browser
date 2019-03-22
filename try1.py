import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

current_dir = os.path.dirname(__file__)

browser = webdriver.Chrome(executable_path=os.path.join(current_dir, 'chromedriver')) # "/home/kbelotserkovets/Documents/Test/chromedriver") # Path to Chrome webdriber
browser.get('http://www.google.com') #
assert 'Google' in browser.title

elem = browser.find_element_by_name('q')  # Find the search box
elem.send_keys('Selenide' + Keys.RETURN)  # Input word "Selenide" and tarting search

# browser.quit() # This is optional for closing browser