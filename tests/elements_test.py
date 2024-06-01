import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, \
    WebTablePage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            full_name, email, current_address, permanent_address = text_box_page.check_filled_form()
            output_name, output_email, output_current_address, output_permanenet_address = text_box_page.check_filled_form()
            assert full_name == output_name, "The full name does not match"
            assert email == output_email, "The email does not match"
            assert current_address == output_current_address, "The current address does not match"
            assert permanent_address == output_permanenet_address, "The permanent address does not match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'Checkboxes have not been selected'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_radio_button('yes')
            output_result_yes = radio_button_page.get_selected_result()
            radio_button_page.click_on_radio_button('impressive')
            output_result_impressive = radio_button_page.get_selected_result()
            radio_button_page.click_on_radio_button('no')
            output_result_no = radio_button_page.get_selected_result()
            assert 'Yes' == output_result_yes, 'Yes have not been select'
            assert 'Impressive' == output_result_impressive, 'Impressive have not been select'
            assert 'No' == output_result_no, 'No have not been select'

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person(count=1)
            person_in_table = web_table_page.check_new_added_person()
            assert new_person in person_in_table, 'Person not added in table'

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            keyword = web_table_page.add_new_person(count=1)[random.randint(0,5)]
            web_table_page.search_person(keyword)
            searched_person = web_table_page.check_searched_person()
            assert keyword in searched_person, 'Person non exist in table'





        # def test_web_table_edit_person(self):
        # def test_web_table_delete_person(self):
        # def test_web_table_row_adding(self):
