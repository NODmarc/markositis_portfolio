from locators.modal_dialogs_locators import ModalDialogsLocators as mdl
from pages.modal_dialogs_page import ModalDialogsPage
from enums.modal_window import LARGE_MODAL_WINDOW_TEXT

class TestModalDialogsPage:
    class TestModalDialogs:
        def test_small_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver,
                                                  "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            title, body = modal_dialogs_page.check_modal_dialogs(
                mdl.SMALL_MODAL_BTN, mdl.SMALL_MODAL_TITLE,
                mdl.SMALL_MODAL_TEXT, 'sm')
            assert title == 'Small Modal', 'Incorrect title in small modal window'
            assert body == 'This is a small modal. It has very less content', 'Incorrect body text in small modal window'

        def test_large_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver,
                                                  "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            title, body = modal_dialogs_page.check_modal_dialogs(
                mdl.LARGE_MODAL_BTN,
                mdl.LARGE_MODAL_TITLE,
                mdl.LARGE_MODAL_TEXT,
                'lm')
            assert title == 'Large Modal', 'Incorrect title in large modal window'
            assert body == LARGE_MODAL_WINDOW_TEXT, 'Incorrect body text in large modal window'
