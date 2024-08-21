from pages.browser_windows_page import BrowserWindowsPage


class TestBrowserWindowsAlertsFrame:
    class TestBrowserWindows:

        def test_open_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver,
                                                      'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.get_session_windows('tab')
            assert text_result == 'This is a sample page', 'Incorrect text in tab or tab is not opened'

        def test_open_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver,
                                                      'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.get_session_windows('windows')
            assert text_result == 'This is a sample page', 'Incorrect text in window or window is not opened'
