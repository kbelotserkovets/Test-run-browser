import unittest

from selenium import webdriver

class BaseTest(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path="./chromedriver")

  def testSeasonOva(self):
    driver = self.driver
    driver.get('http://www.ts.kg/show/fairy_tail')

    firstSeasonHeader = driver.find_elements_by_css_selector("body > div.container.main-container > section > h3")[
        0].text
    secondSeasonHeader = driver.find_elements_by_css_selector("body > div.container.main-container > section > h3")[
        1].text
    thirdSeasonHeader = driver.find_elements_by_css_selector("body > div.container.main-container > section > h3")[
        2].text
    fourthSeasonHeader = driver.find_elements_by_css_selector("body > div.container.main-container > section > h3")[
        3].text
    fifthSeasonHeader = driver.find_elements_by_css_selector("body > div.container.main-container > section > h3")[
        4].text


    amountOfSeriesInSeasonOva = len(driver.find_elements_by_css_selector(
      "body > div.container.main-container > section:nth-child(7) > div > ul > li"))
    amountOfSeriesInSeasonOne = len(driver.find_elements_by_css_selector(
        "body > div.container.main-container > section:nth-child(8) > div > ul > li"))
    amountOfSeriesInSeasonTwo = len(driver.find_elements_by_css_selector(
        "body > div.container.main-container > section:nth-child(9) > div > ul > li"))
    amountOfSeriesInSeasonThree = len(driver.find_elements_by_css_selector(
        "body > div.container.main-container > section:nth-child(10) > div > ul > li"))
    amountOfSeriesInSeasonThree_Jam = len(driver.find_elements_by_css_selector(
        "body > div.container.main-container > section:nth-child(11) > div > ul > li"))

    self.assertEqual("Сезон: OVA", firstSeasonHeader)
    self.assertEqual("Сезон: 1", secondSeasonHeader)
    self.assertEqual("Сезон: 2", thirdSeasonHeader)
    self.assertEqual("Сезон: 3", fourthSeasonHeader)
    self.assertEqual("Сезон: 3_JAM", fifthSeasonHeader)

    self.assertGreaterEqual(7, amountOfSeriesInSeasonOva)
    self.assertGreaterEqual(179, amountOfSeriesInSeasonOne)
    self.assertGreaterEqual(102, amountOfSeriesInSeasonTwo)
    self.assertGreaterEqual(24, amountOfSeriesInSeasonThree)
    self.assertGreaterEqual(24, amountOfSeriesInSeasonThree_Jam)

  def tearDown(self):
    self.driver.close()



class SeriesLinksTest(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path="./chromedriver")

  def testEpisodeContainsUrl(self):
    driver = self.driver
    driver.get('http://www.ts.kg/show/fairy_tail')

    episodes = driver.find_elements_by_css_selector("section div a")
    count_episodes = len(episodes)
    print(count_episodes, "episodes at all")

    for episode in episodes:
        self.assertIn("http://www.ts.kg/show/fairy_tail", episode.get_attribute("href"))

  def tearDown(self):
    self.driver.close()



if __name__ == '__main__':
  unittest.main()