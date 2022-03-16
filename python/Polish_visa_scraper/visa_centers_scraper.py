from base_scraper import BaseScraper
from selenium.webdriver.common.by import By


class VisaCentersScraper(BaseScraper):

    def __init__(self):
        super().__init__('https://visa.vfsglobal.com/blr/ru/pol/attend-centre/')

    def parse_html(self):
        info = self.driver.find_element(by=By.CLASS_NAME, value='v-data-table__wrapper') \
            .find_elements(by=By.TAG_NAME, value='td')

        cities = self.__selenium_to_str(info[::3])
        work_days = self.__selenium_to_str(info[1::3])
        working_hours = self.__selenium_to_str(info[2::3])

        list_info = []
        for i in range(len(cities)):
            self.driver.get(self.driver.find_element(by=By.CLASS_NAME, value='v-data-table__wrapper')
                            .find_element(by=By.LINK_TEXT, value=cities[i]).get_attribute('href'))

            address = self.driver.find_element(by=By.ID, value='section_2') \
                .find_element(By.CLASS_NAME, value='renderer-content').text

            self.driver.back()

            list_info.append({'city': cities[i],
                              'work days': work_days[i],
                              'working hours': working_hours[i],
                              'address': address})

        self.driver.quit()
        return list_info

    @staticmethod
    def __selenium_to_str(info):
        return list(map(lambda x: x.text, info))
