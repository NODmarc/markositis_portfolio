
from locators.browser_windows_locators import BrowserWindowsLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsLocators()

    def get_session_windows(self, parameter):
        if parameter == 'tab':
            self.element_is_visible(self.locators.NEW_TAB_BTN).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            text_title = self.element_is_present(self.locators.NEW_TAB_TITLE).text
            return text_title
        elif parameter == 'windows':
            self.element_is_visible(self.locators.NEW_WINDOW_BTN).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            text_title = self.element_is_present(
                self.locators.NEW_WINDOW_TEXT).text
            return text_title
