import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")

    def test_films_list(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('https://www.ivi.ru/movies')

        wait = WebDriverWait(driver, 6000000000)  # Time in seconds

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
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".year-filter div.sub-menu.single-column")))
        driver.find_element_by_css_selector('li > a[data-value="2018"]').click()

        # html = driver.find_element_by_tag_name('html')
        # html.send_keys(Keys.END)
        # WebDriverWait(driver, 10)

        # driver.implicitly_wait(10)

        time.sleep(5)

        films = driver.find_elements_by_css_selector(".js-catalog-list .poster-badge")

        expected_names = ["[4K] Разлом 2018 https://www.ivi.ru/watch/305813",
                          'Ограбление в ураган 2018 https://www.ivi.ru/watch/177085',
                          "Разлом 2018 https://www.ivi.ru/watch/263738",
                          "Спитак 2018 https://www.ivi.ru/watch/185617"
                          ]

        actual_names = []

        print(len(films))
        self.assertTrue(len(films) == 4)

        for film in films:
            # target = driver.find_element_by_css_selector('a > span.title > span.name')
            # actions = ActionChains(driver)
            # actions.move_to_element(target)
            # actions.perform()

            name = driver.find_element_by_css_selector('.title .name').text

            hover = ActionChains(driver).move_to_element(film)
            hover.perform()
            wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".popup-wrapper-container")))

            year = driver.find_element_by_css_selector('span[itemprop="datePublished"]').text,

            link = film.find_element_by_css_selector('a').get_attribute('href')

            print('{name} {year} {link}'.format(name=name, year=year, link=link))

            actual_names.append(film)

        self.assertEqual(expected_names, actual_names,
                         "Compare the film's name on the website with 'expected_names' list")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
