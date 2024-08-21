from locators.nested_frames_locators import NestedFramesLocators as nfl
from pages.base_page import BasePage


class NestedFramesPage(BasePage):

    def check_nested_frames(self, frame_locator, text_locator):
        iframe = self.element_is_present(frame_locator)
        self.switch_to_frame(iframe)
        text = self.element_is_present(text_locator).text
        return text
