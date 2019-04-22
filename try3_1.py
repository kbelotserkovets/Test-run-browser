import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")

    def hover_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def test_films_list(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://www.ivi.ru/movies')

        # Sort by genre
        genre_to_hover_over = driver.find_element_by_css_selector('.genre-filter.js-expandable')
        self.hover_element(genre_to_hover_over)

        driver.find_element_by_css_selector('a[data-hru="disaster"]').click()

        # Sort by year
        year_to_hover_over = driver.find_element_by_css_selector('li.year-filter.js-expandable.js-catalog-filter-year')
        self.hover_element(year_to_hover_over)

        driver.find_element_by_css_selector('li > a[data-value="2016"]').click()

        time.sleep(1) # Sleep for waiting all films are loaded

        films = driver.find_elements_by_css_selector(".js-catalog-list .poster-badge")

        expected_names = [
                          "День независимости: Возрождение 2016 https://www.ivi.ru/watch/131236",
                          "Ледокол 2016 https://www.ivi.ru/watch/133299",
                          "Постапокалипсис 2016 https://www.ivi.ru/watch/192845",
                          "И грянул шторм 2016 https://www.ivi.ru/watch/136467",
                          "Землетрясение 2016 https://www.ivi.ru/watch/146639",
                          "Глубоководный горизонт 2016 https://www.ivi.ru/watch/144751",
                          "Экипаж 2016 https://www.ivi.ru/watch/126896"
                          ]


        print(len(films))

        actual_names = []

        for film in reversed(films):

            name = film.find_element_by_css_selector(".title .name").text

            self.hover_element(film)
            year = film.find_element_by_css_selector("span[itemprop='datePublished']").text

            link = film.find_element_by_css_selector("a").get_attribute("href")

            print("{name} {year} {link}".format(name=name, year=year, link=link))

            actual_names.append("{name} {year} {link}".format(name=name, year=year, link=link))

        self.assertEqual(expected_names, actual_names,
                         "Compare the film's name on the website with 'expected_names' list")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()