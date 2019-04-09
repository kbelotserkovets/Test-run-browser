import re
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BaseTest(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path="./chromedriver")

  def testFilm(self):
      driver = self.driver
      driver.get('https://oc.kg/#/catalog/genre/37/order/1/page/1')

      wait = WebDriverWait(driver, 100)

      # Sort by genre
      driver.find_element_by_css_selector("#genres_menu_item > li").click()
      wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[id=genres]")))
      driver.find_element_by_css_selector('#genres > li[data-name="Фэнтези"]').click()

      # Sort by year
      driver.find_element_by_css_selector("#sort_menu_item > li > a").click()
      wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[id=sort_wrapper]")))
      driver.find_element_by_css_selector('#sort_wrapper > li > a[data-short-text="Новинки"]').click()

      films = self.driver.find_elements_by_css_selector('#catalog div.item')

      for film in films:
        name = film.find_element_by_css_selector('div.title a').text
        year = re.search('([\d]+)', film.find_element_by_css_selector('div.subtitle').text).group()
        link = film.find_element_by_css_selector('div a').get_attribute('href')

        expected_names = ["Ну разве не романтично? 2019 https://oc.kg/movie.php?id=15576",
                          "Тайная жизнь пингвинов 2018 https://oc.kg/movie.php?id=15774",
                          "Мэри Поппинс возвращается 2018 https://oc.kg/movie.php?id=15765",
                          "Во время грозы 2018 https://oc.kg/movie.php?id=15742",
                          "Гринч 2018 https://oc.kg/movie.php?id=15680",
                          "Аквамен 2018 https://oc.kg/movie.php?id=15401",
                          "Осевшие 2018 https://oc.kg/movie.php?id=15674",
                          "Остров 2018 https://oc.kg/movie.php?id=15590",
                          "Фантастические твари: Преступления Грин-де-Вальда 2018 https://oc.kg/movie.php?id=15500",
                          "Снежная Королева: Зазеркалье 2018 https://oc.kg/movie.php?id=15490",
                          "На границе миров 2018 https://oc.kg/movie.php?id=15450",
                          "Суспирия 2018 https://oc.kg/movie.php?id=15446",
                          "Щелкунчик и четыре королевства 2018 https://oc.kg/movie.php?id=15428",
                          "Хроники хищных городов 2018 https://oc.kg/movie.php?id=15425",
                          "Человек, который убил Дон Кихота 2018 https://oc.kg/movie.php?id=15381"
                          ]

        for names in range(expected_names):
            actual_names = name + " " + year + " " + link
            self.assertEqual(actual_names, names)
            print(actual_names[names])


        # self.assertNotEqual(0, len(name), "Expectation: The film's name in Russian should contain string")
        # self.assertRegex(name, '[а-яА-Я]+.*')
        #
        # self.assertTrue(year.isdigit(), "Check the year contains only digits! :)")
        # self.assertEqual(4, len(year), "Expectation: The length of digits in year should be '4'")
        #
        # self.assertIn("https://oc.kg/movie.php?id", link, "The link should contains: 'https://oc.kg/movie.php?id'")
        #
        # print('Russian name: {name}, Year: {year}, Link: {link}'.format(name=name, year=year, link=link))



  def tearDown(self):
    self.driver.close()


if __name__ == '__main__':
  unittest.main()



