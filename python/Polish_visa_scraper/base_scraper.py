from abc import abstractmethod
from selenium import webdriver


class BaseScraper:

    def __init__(self, url):
        self.url = url
        self.driver = None

    @staticmethod
    def get_driver(url):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        driver.get(url)

        return driver

    @staticmethod
    def create_driver(parse_method):
        def create(self):
            self.driver = self.get_driver(self.url)
            info = parse_method(self)
            self.driver.quit()
            return info

        return create

    @abstractmethod
    def parse_html(self):
        pass
