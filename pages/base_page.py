from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None
    def __init__(self, driver: WebDriver):
        self.driver = driver


    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened for this page class')
        # WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, '//button[@aria-label="Consent"]'))
        # ).click()


    def find(self, locator: tuple):
        return self.driver.find_element(*locator)


    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)
