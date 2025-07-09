from selenium import webdriver
import pytest

from pages.create_account_page import CreateAccount
from pages.products_page import ProductPage
from pages.sale_page import SalePage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver


@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)
