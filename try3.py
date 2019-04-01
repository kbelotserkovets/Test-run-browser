import unittest

from selenium import webdriver

class BaseTest(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path="./chromedriver")

  def testEpisodeContainsUrl(self):
    driver = self.driver
    driver.get('https://oc.kg/#/catalog/genre/37/order/1/page/1')

    films = self.driver.find_elements_by_css_selector('#catalog div div.title a')
    for film in films:
     print(film.text)
     print(film.get_attribute("href"))


    # for film in films:
    #   self.assertIn("https://oc.kg/movie", film.get_attribute("href"))


    # a = [film for film in films.range[0, 45] if "https://oc.kg/#/movie" in film.get_atribute("href")]
    # print(a).text

  def tearDown(self):
    self.driver.close()


if __name__ == '__main__':
  unittest.main()