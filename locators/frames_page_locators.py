from selenium.webdriver.common.by import By


class FramesPageLocators:
    FRAME_1 = (By.CSS_SELECTOR, "iframe[id='frame1']")
    FRAME_2 = (By.CSS_SELECTOR, "iframe[id='frame2']")
    FRAMES_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
