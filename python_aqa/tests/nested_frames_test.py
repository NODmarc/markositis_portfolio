from locators.nested_frames_locators import NestedFramesLocators as nfl
from pages.nested_frames_page import NestedFramesPage


class TestNestedFramesPage:

    def test_nested_frames_fix(self, driver):
        nested_frames_page = NestedFramesPage(driver,
                                              'https://demoqa.com/nestedframes')
        nested_frames_page.open()
        parent_text = nested_frames_page.check_nested_frames(nfl.PARENT_FRAME,
                                                             nfl.PARENT_FRAME_TEXT)
        child_text = nested_frames_page.check_nested_frames(nfl.CHILD_FRAME,
                                                            nfl.CHILD_FRAME_TEXT)
        assert parent_text == 'Parent frame', 'Cannot get parent frame'
        assert child_text == 'Child Iframe', 'Cannot get child frame'
