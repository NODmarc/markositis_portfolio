import time
from pages.base_page import BasePage


def test(driver):
    url = 'https://demoqa.com/text-box'
    page = BasePage(driver, url)
    page.open()
    time.sleep(3)