import unittest

from selenium import webdriver

class BaseTest(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path="./chromedriver")

  def testSeasons(self):
    driver = self.driver
    driver.get('http://www.ts.kg/show/fairy_tail')

    seasonHeader = driver.find_elements_by_css_selector("body > div.container.main-container > section > h3")

    firstSeasonHeader = seasonHeader[0].text
    secondSeasonHeader = seasonHeader[1].text
    thirdSeasonHeader = seasonHeader[2].text
    fourthSeasonHeader = seasonHeader[3].text
    fifthSeasonHeader = seasonHeader[4].text


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

  def testEpisodeContainsUrl(self):
    driver = self.driver
    driver.get('http://www.ts.kg/show/fairy_tail')

    episodes = driver.find_elements_by_css_selector("section div a")
    count_episodes = len(episodes)
    print(count_episodes, "episodes at all")

    # for episode in episodes:
    #     self.assertIn("http://www.ts.kg/show/fairy_tail", episode.get_attribute("href"))

    actual = [episode for episode in episodes if "http://www.ts.kg/show/fairy_tail/OVA" in episode.get_attribute("href")]
    not_valid_episodes = count_episodes - len(actual)

    print(len(actual), "of %d episodes is valid" % count_episodes)
    print(not_valid_episodes, "of %d episodes is not valid" % count_episodes)
    self.assertEqual(0, not_valid_episodes, "Expectation: not valid episodes should be equal to zero, but have {0}".format(not_valid_episodes))

  def tearDown(self):
    self.driver.close()


if __name__ == '__main__':
  unittest.main()