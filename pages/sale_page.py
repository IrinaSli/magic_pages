from selenium.webdriver.common.by import By
from pages.base_page import BasePage


page_header_loc = (By.CSS_SELECTOR, 'h1')
side_bar_loc = (By.CLASS_NAME, 'sidebar-main')
promo_block_loc = (By.CSS_SELECTOR, 'a.block-promo.sale-main')


class SalePage(BasePage):
    page_url = "/sale.html"


    def check_page_header(self, text):
        page_header = self.find(page_header_loc)
        assert page_header.text == text


    def check_side_bar_menu(self):
        page_side_bar = self.find(side_bar_loc)
        assert page_side_bar.is_displayed()


    def click_on_promo_women(self):
        self.find(promo_block_loc).click()


    def check_women_sale_page_url(self):
        self.driver.implicitly_wait(10)
        page_url = self.driver.current_url
        assert "/women-sale.html" in page_url
