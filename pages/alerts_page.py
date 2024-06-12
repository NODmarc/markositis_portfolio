import random
import time

from locators.alerts_page_locators import AlertsPageLocators
from pages.base_page import BasePage


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BTN).click()
        alert_window = self.switch_to_alert()
        alert_text = alert_window.text
        return alert_text

    def check_delayed_alert(self):
        self.element_is_visible(self.locators.ALERT_AFTER_5SEC_BTN).click()
        time.sleep(5)
        alert_window = self.switch_to_alert()
        alert_text = alert_window.text
        return alert_text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BTN).click()
        alert_window = self.switch_to_alert()
        if random.choice([True, False]):
            alert_window.accept()
        else:
            alert_window.dismiss()
        confirm_result_text = self.element_is_visible(
            self.locators.CONFIRM_RESULT).text
        return confirm_result_text

    def check_prompt_alert(self):
        test_data = f'Autotest{random.randint(0, 999)}'
        self.element_is_visible(self.locators.PROMPT_BTN).click()
        alert_window = self.switch_to_alert()
        alert_window.send_keys(test_data)
        alert_window.accept()
        prompt_result_text = self.element_is_visible(
            self.locators.PROMPT_RESULT).text
        return test_data, prompt_result_text
