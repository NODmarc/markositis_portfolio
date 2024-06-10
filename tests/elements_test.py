import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, \
    WebTablePage, ButtonsPage, LinksPage, FilePage, DynamicPropertiesPage


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
            check_box_page = CheckBoxPage(driver,
                                          'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'Checkboxes have not been selected'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver,
                                                'https://demoqa.com/radio-button')
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
            web_table_page = WebTablePage(driver,
                                          'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person(count=1)
            person_in_table = web_table_page.check_new_added_person()
            assert new_person in person_in_table, 'Person not added in table'

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver,
                                          'https://demoqa.com/webtables')
            web_table_page.open()
            keyword = web_table_page.add_new_person(count=1)[
                random.randint(0, 5)]
            web_table_page.search_person(keyword)
            searched_person = web_table_page.check_searched_person()
            assert keyword in searched_person, 'Person non exist in table'

        def test_web_table_edit_person(self, driver):
            web_table_page = WebTablePage(driver,
                                          'https://demoqa.com/webtables')
            web_table_page.open()
            keyword = web_table_page.add_new_person(count=1)[
                random.randint(0, 5)]
            web_table_page.search_person(keyword)
            random_field = web_table_page.update_person_info()
            row = web_table_page.check_searched_person()
            assert random_field in row, 'Person card is not editable'

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver,
                                          'https://demoqa.com/webtables')
            web_table_page.open()
            keyword = web_table_page.add_new_person(count=1)[
                random.randint(0, 5)]
            web_table_page.search_person(keyword)
            web_table_page.delete_person_info()
            row = web_table_page.check_deleted()
            assert row == 'No rows found'

        def test_web_table_row_adding(self, driver):
            web_table_page = WebTablePage(driver,
                                          'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], 'The number of rows in the table has not been changed'

    class TestButtonPage:

        def test_different_click_on_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_diff_btn('double')
            right = button_page.click_on_diff_btn("right")
            click = button_page.click_on_diff_btn("click")
            assert double == 'You have done a double click', 'Double click was not pressed'
            assert right == 'You have done a right click', 'Right click was not pressed'
            assert click == 'You have done a dynamic click', 'Click was not pressed'

    class TestLinksPage:

        def test_simple_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, new_tab_url = links_page.check_new_tab(link='simple')
            assert href_link, new_tab_url == "https://demoqa.com/"

        def test_dynamic_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, new_tab_url = links_page.check_new_tab(link='dynamic')
            assert href_link, new_tab_url == 'https://demoqa.com/'

        def test_created_request(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_request_status_code(
                endpoint='/created')
            assert response_code == 201

        def test_no_content_request(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_request_status_code(
                endpoint='/no-content')
            assert response_code == 204

        def test_moved_request(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_request_status_code(
                endpoint='/moved')
            assert response_code == 301

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link(
                'https://demoqa.com/bad-request')
            assert response_code == 400

        def test_unauthorized_request(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_request_status_code(
                endpoint='/unauthorized')
            assert response_code == 401

        def test_forbidden_request(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_request_status_code(
                endpoint='/forbidden')
            assert response_code == 403

        def test_not_found_request(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_request_status_code(
                endpoint='/invalid-url')
            assert response_code == 404

    class TestUploadDownloadPage:

        def test_file_upload(self, driver):
            file_page = FilePage(driver, 'https://demoqa.com/upload-download')
            file_page.open()
            file_name, result = file_page.upload_file()
            assert file_name == result, 'the file has not uploaded'

        def test_file_download(self, driver):
            file_page = FilePage(driver, 'https://demoqa.com/upload-download')
            file_page.open()
            file = file_page.download_file()
            assert file is True, 'the file has not downloaded'

    class TestDynamicPropertiesPage:

        def test_clickable_btn(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver,
                                                            'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable_btn = dynamic_properties_page.check_enable_btn()
            assert enable_btn is True, "Button 'Will enable 5 seconds' is not clickable"

        def test_color_btn_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver,
                                                            'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_color()
            assert color_before != color_after, "Color is not changed"

        def test_appears_btn(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver,
                                                            'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appears_btn()
            assert appear is True, "Button 'Visible After 5 Seconds' is not visible"
