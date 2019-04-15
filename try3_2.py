import re
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")

    def testFilm(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('http://kinogo.eu')

        WebDriverWait(driver, 10)  # Time in seconds

        # Sort by genre
        driver.find_element_by_css_selector('a:nth-child(42)').click()

        films = driver.find_elements_by_css_selector('.shortstory')

        expected_names = ['Штамм химеры (2018) http://kinogo.eu/9570-shtamm-himery-2018.html',
                          'Миа и белый лев (2019) http://kinogo.eu/9537-mia-i-belyy-lev-2019.html',
                          'Высшее общество (2019) http://kinogo.eu/9504-vysshee-obschestvo-2019.html',
                          'Домовой (2019) http://kinogo.eu/9488-domovoy-2019.html',
                          'Среди теней (2019) http://kinogo.eu/9565-sredi-teney-2019.html',
                          'Работа без авторства (2019) http://kinogo.eu/9564-rabota-bez-avtorstva-2019.html',
                          'Призраки Шэрон Тейт (2019) http://kinogo.eu/9563-prizraki-sheron-teyt-2019.html',
                          'Гости (2019) http://kinogo.eu/9376-gosti-2019.html',
                          'Любовницы (2019) http://kinogo.eu/9258-lyubovnicy-2019.html',
                          'Магазин единорогов (2017) http://kinogo.eu/9558-magazin-edinorogov-2017.html'
                          ]

        actual_names = [
            '{name} {link}'.format(
                name=film.find_element_by_css_selector('div.zagolovki > strong > a').text,
                link=film.find_element_by_css_selector('div.zagolovki > strong > a').get_attribute('href'))
            for film in films
        ]
        for film in actual_names:
            print(film)
        self.assertEqual(expected_names, actual_names,
                         "Compare the film's name on the website with 'expected_names' list")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
