from base_scraper import BaseScraper
from selenium.webdriver.common.by import By


class NewsScraper(BaseScraper):

    def __init__(self):
        super().__init__('https://visa.vfsglobal.com/blr/en/pol/')

    @BaseScraper.create_driver
    def parse_html(self):
        all_news = self.driver.find_element(by=By.CLASS_NAME, value='page-component').\
            find_elements(By.CLASS_NAME, value='news-li')

        list_news = []
        for news in all_news:
            list_news.append(
                {
                    'date': news.find_element(By.CLASS_NAME, value='news-date').text,
                    'news': news.find_element(By.CLASS_NAME, value='renderer-content').text,
                    'link': news.find_element(By.TAG_NAME, value='a').get_attribute('href')
                }
            )

        return list_news
