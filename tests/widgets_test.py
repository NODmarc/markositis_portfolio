import time

from enums import accordians as acc
from generator.generator import generated_color
from pages.autocomplete_page import AutocompletePage
from pages.widgets_page import AccordianPage


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
            autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            input_color = autocomplete_page.fill_multi_input()
            output_color = autocomplete_page.get_values_from_multi_autocomplete()
            assert input_color == output_color, 'The added color is missing in the input.'

        def test_remove_all_values_multi_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            input_color = autocomplete_page.fill_multi_input()
            output_result = autocomplete_page.remove_all_values_from_multi()
            assert input_color != output_result, 'The added colors are not removed.'

        def test_remove_one_by_one_value_multi_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            input_color = autocomplete_page.fill_multi_input()
            output_result = autocomplete_page.removal_one_by_one_values_from_multi()
            print(input_color)
            print(output_result)
            assert input_color != output_result, 'The added colors are not removed.'

        def test_single_fill_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            input_result = autocomplete_page.fill_single_input()
            output_result = autocomplete_page.check_single_color()
            assert input_result == output_result, 'The added color is missing in the input.'









