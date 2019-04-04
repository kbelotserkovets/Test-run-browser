import re
import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path="./chromedriver")

  def testFilm(self):
    driver = self.driver
    driver.implicitly_wait(5)
    driver.get('https://oc.kg/#/catalog/genre/37/order/1/page/1')

    films = self.driver.find_elements_by_css_selector('#catalog div.item')

    for film in films:
      name = film.find_element_by_css_selector('div.title a').text
      year = re.search('([\d]+)', film.find_element_by_css_selector('div.subtitle').text).group()
      link = film.find_element_by_css_selector('div a').get_attribute('href')

      print('Russian name: {name}, Year: {year}, Link: {link}'.format(name=name, year=year, link=link))

      self.assertNotEqual(0, len(name), "Expectation: The film's name in Russian should contain string ")

      self.assertTrue(year.isdigit(), "Check the year contains only digits! :)")
      self.assertEqual(4, len(year), "Expectation: The length of digits in year should be '4'")

      self.assertIn("https://oc.kg/movie.php?id", link, "The link should contains: 'https://oc.kg/movie.php?id'")


  def tearDown(self):
    self.driver.close()


if __name__ == '__main__':
  unittest.main()