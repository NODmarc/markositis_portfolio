from selenium.webdriver.common.by import By


class AlertsPageLocators:
    SEE_ALERT_BTN = (By.CSS_SELECTOR, "button[id='alertButton']")
    ALERT_AFTER_5SEC_BTN = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BTN = (By.CSS_SELECTOR, "button[id='confirmButton']")
    PROMPT_BTN = (By.CSS_SELECTOR, "button[id='promtButton']")
    CONFIRM_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_RESULT = (By.CSS_SELECTOR, "span[id='promptResult']")
