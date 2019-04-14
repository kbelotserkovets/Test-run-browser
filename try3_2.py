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
        driver.maximize_window()
        driver.get('http://kinogo.eu')

        wait = WebDriverWait(driver, 10) # Time in seconds

        # Sort by genre
        driver.find_element_by_css_selector('a:nth-child(42)').click()

        # # Sort by year
        # driver.find_element_by_css_selector("#sort_menu_item > li > a").click()
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[id=sort_wrapper]")))
        # driver.find_element_by_css_selector('#sort_wrapper > li > a[data-short-text="Новинки"]').click()

        films = driver.find_elements_by_css_selector('.shortstory')

        expected_names = ['Среди теней (2019) http://kinogo.eu/9565-sredi-teney-2019.html',
                          'Работа без авторства (2019) http://kinogo.eu/9564-rabota-bez-avtorstva-2019.html',
                          'Призраки Шэрон Тейт (2019) http://kinogo.eu/9563-prizraki-sheron-teyt-2019.html',
                          'Гости (2019) http://kinogo.eu/9376-gosti-2019.html',
                          'Любовницы (2019) http://kinogo.eu/9258-lyubovnicy-2019.html',
                          'Магазин единорогов (2017) http://kinogo.eu/9558-magazin-edinorogov-2017.html',
                          'Время монстров (2019) http://kinogo.eu/9557-vremya-monstrov-2019.html',
                          'Сирано. Успеть до премьеры (2019) http://kinogo.eu/9556-sirano-uspet-do-premery-2019.html',
                          'Потерянный остров (2019) http://kinogo.eu/9555-poteryannyy-ostrov-2019.html',
                          'Отпетые мошенницы (2019) http://kinogo.eu/9554-otpetye-moshennicy-2019.html'
                          ]

        actual_names = [
            '{name} {link}'.format(
                name=film.find_element_by_css_selector('div.zagolovki > strong > a').text,
                link=film.find_element_by_css_selector('div.zagolovki > strong > a').get_attribute('href'))
            for film in films
        ]
        for film in actual_names:
            print(film)
        self.assertEqual(expected_names, actual_names, "Compare the film's name on the website with list 'expected_names'")



    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
