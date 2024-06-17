from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_WHAT_TITLE = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECTION_WHAT_TEXT = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    SECTION_WHERE_TITLE = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECTION_WHERE_TEXT = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    SECTION_WHY_TITLE = (By.CSS_SELECTOR, "div[id='section3Heading']")
    SECTION_WHY_TEXT = (By.CSS_SELECTOR, "div[id='section3Content'] p")
