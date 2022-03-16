from abc import abstractmethod
from selenium import webdriver


class BaseScraper:

    def __init__(self, url):
        self.driver = self.__get_driver(url)

    @staticmethod
    def __get_driver(url):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        driver.get(url)

        return driver

    @abstractmethod
    def parse_html(self):
        pass
