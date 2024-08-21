from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    NEW_TAB_BTN = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_TAB_TITLE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    NEW_WINDOW_BTN = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_WINDOW_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")

