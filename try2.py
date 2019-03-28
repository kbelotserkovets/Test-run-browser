import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path="./chromedriver")

  def testSearch(self):
    driver = self.driver
    driver.get('http://www.ts.kg/show/fairy_tail')

    element = driver.find_element_by_name('q')
    element.send_keys('Selenide' + Keys.RETURN)

    firstResultHeader = driver.find_elements_by_css_selector("body > div.container.main-container > section > div")[
        0].text
    self.assertEqual("Selenide: concise UI tests in Java", firstResultHeader)

  def tearDown(self):
    self.driver.close()


if __name__ == '__main__':
  unittest.main()

  # body > div.container.main-container > section > div > ul > li