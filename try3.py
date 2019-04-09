import re
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from langdetect import detect



class BaseTest(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path="./chromedriver")

  def testFilm(self):
      driver = self.driver
      driver.get('https://oc.kg/#/catalog/genre/37/order/1/page/1')

      wait = WebDriverWait(driver, 10)

      # Sort by genre
      driver.find_element_by_css_selector("#genres_menu_item > li > a").click()
      wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[id=genres]")))
      options = driver.find_elements_by_css_selector("#genres > li")
      options[15].click()

      # Sort by year
      driver.find_element_by_css_selector("#sort_menu_item > li > a").click()
      wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[id=sort_wrapper]")))
      options = driver.find_elements_by_css_selector("#sort_wrapper > li")
      options[1].click()

      films = self.driver.find_elements_by_css_selector('#catalog div.item')

      for film in films:
        name = film.find_element_by_css_selector('div.title a').text
        lang = detect(name)

        year = re.search('([\d]+)', film.find_element_by_css_selector('div.subtitle').text).group()
        link = film.find_element_by_css_selector('div a').get_attribute('href')

        self.assertNotEqual(0, len(name), "Expectation: The film's name in Russian should contain string")
        # self.assertEqual('ru', lang)
        self.assertRegex(name, '[а-яА-Я]+.*')

        self.assertTrue(year.isdigit(), "Check the year contains only digits! :)")
        self.assertEqual(4, len(year), "Expectation: The length of digits in year should be '4'")

        self.assertIn("https://oc.kg/movie.php?id", link, "The link should contains: 'https://oc.kg/movie.php?id'")

        print('Russian name: {name}, Year: {year}, Link: {link}'.format(name=name, year=year, link=link))
        print(lang)



  def tearDown(self):
    self.driver.close()


if __name__ == '__main__':
  unittest.main()



