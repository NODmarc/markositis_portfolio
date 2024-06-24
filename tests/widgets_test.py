from enums import accordians as acc
from pages.autocomplete_page import AutocompletePage
from pages.widgets_page import AccordianPage, SliderPage, DataPickerPage, \
    ProgressBarPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver,
                                           'https://demoqa.com/accordian')
            accordian_page.open()
            accordian_what_title, accordian_what_text = accordian_page \
                .check_accordian('what')
            accordian_where_title, accordian_where_text = accordian_page \
                .check_accordian('where')
            accordian_why_title, accordian_why_text = accordian_page \
                .check_accordian('why')
            assert accordian_what_title == acc.WHAT_ACCORDIAN_TITLE and accordian_what_text > 0, "Title or content does not match"
            assert accordian_where_title == acc.WHERE_ACCORDIAN_TITLE and accordian_where_text > 0, "Title or content does not match"
            assert accordian_why_title == acc.WHY_ACCORDIAN_TITLE and accordian_why_text > 0, "Title or content does not match"

    class TestAutocomplete:

        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver,
                                                 "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            input_color = autocomplete_page.fill_multi_input()
            output_color = autocomplete_page.get_values_from_multi_autocomplete()
            assert input_color == output_color, 'The added color is missing in the input.'

        def test_remove_all_values_multi_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver,
                                                 "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            input_color = autocomplete_page.fill_multi_input()
            output_result = autocomplete_page.remove_all_values_from_multi()
            assert input_color != output_result, 'The added colors are not removed.'

        def test_remove_one_by_one_value_multi_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver,
                                                 "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            input_color = autocomplete_page.fill_multi_input()
            output_result = autocomplete_page.removal_one_by_one_values_from_multi()
            print(input_color)
            print(output_result)
            assert input_color != output_result, 'The added colors are not removed.'

        def test_single_fill_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver,
                                                 "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            input_result = autocomplete_page.fill_single_input()
            output_result = autocomplete_page.check_single_color()
            assert input_result == output_result, 'The added color is missing in the input.'

    class TestDataPicker:

        def test_select_date(self, driver):
            date_picker_page = DataPickerPage(driver,
                                              "https://demoqa.com/date-picker")
            date_picker_page.open()
            date_before, date_after = date_picker_page.select_date()
            assert date_before != date_after, 'Date not changed'

        def test_select_date_time(self, driver):
            date_picker_page = DataPickerPage(driver,
                                              "https://demoqa.com/date-picker")
            date_picker_page.open()
            date_before, date_after = date_picker_page.select_date_time()
            assert date_before != date_after, 'Date and time not changed'

    class TestSlider:

        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            value_before, value_after = slider_page.change_slider_value()
            assert value_before != value_after, 'The values does not match.'

    class TestProgressBar:

        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver,'https://demoqa.com/progress-bar')
            progress_bar.open()
            value_before, value_after_stop, value_after_reset = progress_bar.check_progress_bar_value()
            assert value_before == '0', 'Incorrect start value in progress bar'
            assert value_after_stop == '40' or '50' or '60', 'Incorrect stop value in progress bar'
            assert value_after_reset == '0', 'Incorrect reset value in progress bar'
