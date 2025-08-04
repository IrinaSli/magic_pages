from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


selected_item_loc = (By.XPATH, '//li[contains(@class, "product-item")]//a[@class="product-item-link"]')
add_to_compare_loc = (By.XPATH, '//a[@class="action tocompare"]')
product_link_loc = (By.XPATH, "//ol[@id='compare-items']//a[contains(@class, 'product-item-link')]")


class ProductPage(BasePage):
    page_url = "/collections/eco-friendly.html"


    def add_to_compare(self):
        selected_item = self.find(selected_item_loc)
        selected_item_name = selected_item.text.strip()
        add_to_compare = self.find(add_to_compare_loc)
        ActionChains(self.driver).move_to_element(selected_item).click(add_to_compare).perform()
        # (WebDriverWait(self.driver, 10).
        #  until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-labelledby="block-compare-heading"]'))))
        product_link = self.find(product_link_loc)
        item_in_compare_name = product_link.text.strip()
        assert item_in_compare_name == selected_item_name


    def remove_all_from_compare(self):
        clear_all_button = self.driver.find_element(By.ID, "compare-clear-all")
        clear_all_button.click()
        (WebDriverWait(self.driver, 10).
         until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.action-primary.action-accept"))))
        modal_ok_button = self.driver.find_element(By.CSS_SELECTOR, "button.action-primary.action-accept")
        modal_ok_button.click()


    def check_alert_text(self, expected_message):
        alert = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@role='alert']//div[contains(text(), 'cleared the comparison')]"))
        )
        alert_text = alert.text.strip()
        assert alert_text == expected_message


    def hover_over_product(self):
        selected_item = self.driver.find_element(By.XPATH,
                                                 '//li[contains(@class, "product-item")]//a[@class="product-item-link"]')
        ActionChains(self.driver).move_to_element(selected_item).perform()


    def check_add_to_card_actions_is_displayed(self):
        self.hover_over_product()
        add_to_cart_btn = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        assert add_to_cart_btn.is_displayed()


    def check_add_to_wishlist_actions_is_displayed(self):
        self.hover_over_product()
        add_to_wishlist = self.driver.find_element(By.XPATH, '//a[@class="action towishlist"]')
        assert add_to_wishlist.is_displayed()


    def check_add_to_compare_actions_is_displayed(self):
        self.hover_over_product()
        add_to_compare = self.driver.find_element(By.XPATH, '//a[@class="action tocompare"]')
        assert add_to_compare.is_displayed()
