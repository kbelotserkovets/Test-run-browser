import re
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")

    def testFilm(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.ivi.ru/movies')


        wait = WebDriverWait(driver, 10) # Time in seconds

        # Sort by genre
        genre_to_hover_over = driver.find_element_by_css_selector('.genre-filter.js-expandable')
        hover = ActionChains(driver).move_to_element(genre_to_hover_over)
        hover.perform()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li.genre-filter.js-expandable > div.sub-menu")))
        driver.find_element_by_css_selector('a[data-hru="disaster"]').click()


        # Sort by year
        year_to_hover_over = driver.find_element_by_css_selector('li.year-filter.js-expandable.js-catalog-filter-year')
        hover = ActionChains(driver).move_to_element(year_to_hover_over)
        hover.perform()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li.year-filter.js-expandable.js-catalog-filter-year > div.sub-menu.single-column")))
        driver.find_element_by_css_selector('li > a[data-value="2018"]').click()

        films = driver.find_elements_by_css_selector("div.gallery-wrapper > ul > li[data-content-type='content']")

        expected_names = ["Ну разве не романтично? 2019 https://oc.kg/movie.php?id=15576",
                          'Удивительный мир Марвена 2018 https://oc.kg/movie.php?id=15790',
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
                          "Хроники хищных городов 2018 https://oc.kg/movie.php?id=15425"
                          ]

        actual_names = [
            '{name} {year} {link}'.format(
                name=film.find_element_by_css_selector('div.title a').text,
                year=re.search('([\d]+)', film.find_element_by_css_selector('div.subtitle').text).group(),
                link=film.find_element_by_css_selector('div a').get_attribute('href'))
            for film in films
        ]

        self.assertEqual(expected_names, actual_names)


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
