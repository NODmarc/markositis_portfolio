from selenium.webdriver.common.by import By


class ModalDialogsLocators:

    SMALL_MODAL_BTN = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    SMALL_MODAL_WINDOW = (By.CSS_SELECTOR, "div[class='modal-content']")
    SMALL_MODAL_TEXT = (By.CSS_SELECTOR, "div[class='modal-body']")
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")
    SMALL_MODAL_BTN_CLOSE = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
    SMALL_MODAL_ICON_CLOSE = (By.CSS_SELECTOR, "button[class='close']")

    LARGE_MODAL_BTN = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    LARGE_MODAL_WINDOW = (By.CSS_SELECTOR, "div[role='document]")
    LARGE_MODAL_TEXT = (By.CSS_SELECTOR, "p[class]")
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")
    LARGE_MODAL_BTN_CLOSE = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
    LARGE_MODAL_ICON_CLOSE = (By.CSS_SELECTOR, "button[class='close']")

