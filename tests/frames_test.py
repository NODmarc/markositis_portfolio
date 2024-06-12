from pages.frames_page import FramesPage


class TestFramePage:
    def test_frames(self, driver):
        frame_page = FramesPage(driver, 'https://demoqa.com/frames')
        frame_page.open()
        output_frame1 = frame_page.check_frame('frame1')
        output_frame2 = frame_page.check_frame('frame2')
        assert output_frame1 == ['This is a sample page', '500px', '350px'], "Frame is not visible"
        assert output_frame2 == ['This is a sample page', '100px', '100px'], "Frame is not visible"

