import unittest
import urllib.request
from selenium import webdriver

class BaseTest(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path="./chromedriver")

  def testSeasonOva(self):
    driver = self.driver
    driver.get('http://www.ts.kg/show/fairy_tail')

    firstSeasonHeader = driver.find_elements_by_css_selector("body > div.container.main-container > section:nth-child(7) > h3")[
        0].text

    amountOfSeries = len(driver.find_elements_by_css_selector(
      "body > div.container.main-container > section:nth-child(7) > div > ul > li"))

    self.assertEqual("Сезон: OVA", firstSeasonHeader)
    self.assertEqual(7, amountOfSeries)

  def tearDown(self):
    self.driver.close()



class UrlIsUpTest(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path="./chromedriver")

  def testSeasonFirst(self):
    driver = self.driver
    driver.get('http://www.ts.kg/show/fairy_tail')

    series = driver.find_elements_by_css_selector('')


print(urllib.request.urlopen("http://www.stackoverflow.com").getcode())



if __name__ == '__main__':
  unittest.main()