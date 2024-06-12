from locators.frames_page_locators import FramesPageLocators
from pages.base_page import BasePage


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            iframe = self.element_is_present(self.locators.FRAME_1)
            width = iframe.get_attribute('width')
            height = iframe.get_attribute('height')
            self.switch_to_frame(iframe)
            frame_text = self.element_is_present(self.locators.FRAMES_TEXT).text
            self.switch_to_default_content()
            return [frame_text, width, height]
        if frame_num == 'frame2':
            iframe = self.element_is_present(self.locators.FRAME_2)
            width = iframe.get_attribute('width')
            height = iframe.get_attribute('height')
            self.switch_to_frame(iframe)
            frame_text = self.element_is_present(self.locators.FRAMES_TEXT).text
            return [frame_text, width, height]


