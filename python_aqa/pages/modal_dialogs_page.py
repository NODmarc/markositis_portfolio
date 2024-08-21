import random

from locators.modal_dialogs_locators import ModalDialogsLocators
from pages.base_page import BasePage


class ModalDialogsPage(BasePage):

    locators = ModalDialogsLocators()

    def check_modal_dialogs(self, btn, title, body, size):
        self.element_is_visible(btn).click()
        title_small = self.element_is_visible(title).text
        body_small = self.element_is_visible(body).text
        if size == 'sm':
            if random.choice([True, False]):
                self.element_is_visible(self.locators.SMALL_MODAL_BTN_CLOSE).click()
            else:
                self.element_is_visible(self.locators.SMALL_MODAL_ICON_CLOSE).click()
        if size == 'lm':
            if random.choice([True, False]):
                self.element_is_visible(self.locators.LARGE_MODAL_BTN_CLOSE).click()
            else:
                self.element_is_visible(self.locators.LARGE_MODAL_ICON_CLOSE).click()
        return title_small, body_small

