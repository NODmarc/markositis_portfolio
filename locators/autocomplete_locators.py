from selenium.webdriver.common.by import By


class AutocompleteLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTI_INPUT_VALUE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")
    MULTI_INPUT_DELETE_BTN = (By.CSS_SELECTOR, "div[class='css-xb97g8 auto-complete__multi-value__remove'] svg path")
    MULTI_INPUT_DELETE_ALL_BTN = (By.CSS_SELECTOR, "div[class='auto-complete__indicators css-1wy0on6'] svg path")
    SINGLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")
    SINGLE_INPUT_VALUE = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")
    SINGLE_FIELD = (By.CSS_SELECTOR, "input[id='autoCompleteSingleContainer']")
