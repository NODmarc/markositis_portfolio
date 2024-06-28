import random

from enums import accordians as acc
from enums.select_menu_values import OPTIONS, PREFIX_OPTIONS, COLORS
from locators.widgets_locators import SelectMenuLocators as sml
from locators.widgets_locators import TabsPageLocators as tpl
from pages.autocomplete_page import AutocompletePage
from pages.widgets_page import AccordianPage, SliderPage, DataPickerPage, \
    ProgressBarPage, TabsPage, TooltipsPage, MenuPage, SelectMenuPage


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
            progress_bar = ProgressBarPage(driver,
                                           'https://demoqa.com/progress-bar')
            progress_bar.open()
            value_before, value_after_stop, value_after_reset = progress_bar.check_progress_bar_value()
            assert value_before == '0', 'Incorrect start value in progress bar'
            assert value_after_stop == '40' or '50' or '60', \
                'Incorrect stop value in progress bar'
            assert value_after_reset == '0', \
                'Incorrect reset value in progress bar'

    class TestTabs:
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            what_tab_title, what_tab_content = tabs_page.check_tabs('what')
            origin_tab_title, origin_tab_content = tabs_page.check_tabs(
                'origin')
            use_tab_title, use_tab_content = tabs_page.check_tabs('use')
            more_tab_title = tabs_page.get_tab_title(tpl.MORE_TAB)
            assert what_tab_title == 'What' and what_tab_content != 0, \
                'The tab "what" was not pressed or the text is missing'
            assert origin_tab_title == 'Origin' and origin_tab_content != 0, \
                'The tab "origin" was not pressed or the text is missing'
            assert use_tab_title == 'Use' and use_tab_content != 0, \
                'The tab "use" was not pressed or the text is missing'
            assert more_tab_title == 'More', 'The tab "more" text is missing'

    class TestTooltips:
        def test_tooltips(self, driver):
            tooltip_page = TooltipsPage(driver, 'https://demoqa.com/tool-tips')
            tooltip_page.open()
            button, field, contrary, section = tooltip_page.check_tooltips()
            assert button == 'You hovered over the Button', \
                'Text in tooltip is not correct or hover is missing'
            assert field == 'You hovered over the text field', \
                'Text in tooltip is not correct or hover is missing'
            assert contrary == 'You hovered over the Contrary', \
                'Text in tooltip is not correct or hover is missing'
            assert section == 'You hovered over the 1.10.32', \
                'Text in tooltip is not correct or hover is missing'

    class TestMenu:
        def test_menu(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu")
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item',
                            'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3'], \
                'Menu text is incorrect or menu not clickable'

    class TestSelectMenu:
        def test_select_value(self, driver):
            select_menu_page = SelectMenuPage(driver,
                                              'https://demoqa.com/select-menu')
            select_menu_page.open()
            value = select_menu_page.select_value(sml.SELECT_FIELD,
                                                  random.choice(
                                                      [sml.SELECT_OPTIONS_1,
                                                       sml.SELECT_OPTIONS_2,
                                                       sml.SELECT_OPTIONS_3,
                                                       sml.SELECT_OPTIONS_4]),
                                                  sml.SELECT_VALUE)
            assert value in OPTIONS, \
                'Cannot select value or text is not correct'

        def test_select_one(self, driver):
            select_menu_page = SelectMenuPage(driver,
                                              'https://demoqa.com/select-menu')
            select_menu_page.open()
            value = select_menu_page.select_value(sml.SELECT_ONE,
                                                  sml.SELECT_TITLE,
                                                  sml.SELECT_VALUE)
            assert value in PREFIX_OPTIONS, \
                'Cannot select value or text is not correct'

        def test_old_style_select_menu(self, driver):
            select_menu_page = SelectMenuPage(driver,
                                              'https://demoqa.com/select-menu')
            select_menu_page.open()
            options = select_menu_page.get_old_menu_options()
            value = select_menu_page.select_value_old()
            assert value in options, 'Cannot select value or text is not correct'

        def test_multi_select_drop_down(self, driver):
            select_menu_page = SelectMenuPage(driver,
                                              'https://demoqa.com/select-menu')
            select_menu_page.open()
            output = select_menu_page.select_multi_dropdown(COLORS)
            assert output == COLORS, 'Cannot input colors in select or colors text is incorrect'
