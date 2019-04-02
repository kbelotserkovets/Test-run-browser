import re
import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path="./chromedriver")

  def testEpisodeContainsUrl(self):
    driver = self.driver
    driver.implicitly_wait(5)
    driver.get('https://oc.kg/#/catalog/genre/37/order/1/page/1')

    films = self.driver.find_elements_by_css_selector('#catalog div.item')

    for film in films:
      name = film.find_element_by_css_selector('div.title a').text
      year = re.search('\(.*\)', film.find_element_by_css_selector('div.subtitle').text).group()
      link = film.find_element_by_css_selector('div a').get_attribute('href')
      print(name, year, link)




  def tearDown(self):
    self.driver.close()


if __name__ == '__main__':
  unittest.main()