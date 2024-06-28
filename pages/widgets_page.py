import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from enums.years import YEAR_LIST
from generator.generator import generated_date
from locators.widgets_locators import AccordianPageLocators, \
    DataPickerPageLocators, SliderPageLocators, ProgressBarLocators, \
    TabsPageLocators, TooltipPageLocators, MenuPageLocators, SelectMenuLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_name):
        accordian = {
            'what':
                {
                    'title': self.locators.SECTION_WHAT_TITLE,
                    'text': self.locators.SECTION_WHAT_TEXT
                },
            'where':
                {
                    'title': self.locators.SECTION_WHERE_TITLE,
                    'text': self.locators.SECTION_WHERE_TEXT
                },
            'why':
                {
                    'title': self.locators.SECTION_WHY_TITLE,
                    'text': self.locators.SECTION_WHY_TEXT
                }
        }
        section_title = self.element_is_visible(
            accordian[accordian_name]['title']).text
        self.element_is_visible(accordian[accordian_name]['title']).click()
        section_text = self.element_is_visible(
            accordian[accordian_name]['text']).text
        return [section_title, len(section_text)]


class DataPickerPage(BasePage):
    locators = DataPickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_PICKER_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_PICKER_SELECT_MONTH,
                              date.month)
        self.set_date_by_text(self.locators.DATE_PICKER_SELECT_YEAR,
                              date.year)
        self.set_date_item_from_list(self.locators.DATE_PICKER_SELECT_DAY_LIST,
                                     date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.element_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def select_date_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST,
                                     date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST,
                                     random.choice(YEAR_LIST))
        self.set_date_item_from_list(self.locators.DATE_PICKER_SELECT_DAY_LIST,
                                     date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST,
                                     date.time)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(
            self.locators.SLIDER_RESULT).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.drag_and_drop(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(
            self.locators.SLIDER_RESULT).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarLocators()

    def check_progress_bar_value(self):
        value_before = self.element_is_present(
            self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        progress_bar_start = self.element_is_visible(
            self.locators.START_STOP_BUTTON)
        progress_bar_start.click()
        time.sleep(random.randint(4, 6))
        self.element_is_visible(self.locators.START_STOP_BUTTON).click()
        value_after_stop = self.element_is_present(
            self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        progress_bar_start.click()
        time.sleep(5)
        self.element_is_visible(self.locators.RESET_BUTTON).click()
        value_after_reset = self.element_is_present(
            self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        return value_before, value_after_stop, value_after_reset


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, tab_name):
        tabs_name = {
            'what':
                {
                    'title': self.locators.WHAT_TAB,
                    'text': self.locators.WHAT_TAB_TEXT
                },
            'origin':
                {
                    'title': self.locators.ORIGIN_TAB,
                    'text': self.locators.ORIGIN_TAB_TEXT
                },
            'use':
                {
                    'title': self.locators.USE_TAB,
                    'text': self.locators.USE_TAB_TEXT
                },
            'more':
                {
                    'title': self.locators.MORE_TAB,
                    'text': self.locators.MORE_TAB_TEXT
                }
        }
        tab_title = self.element_is_visible(tabs_name[tab_name]['title']).text
        self.element_is_visible(tabs_name[tab_name]['title']).click()
        tab_content = self.element_is_visible(tabs_name[tab_name]['text']).text
        return [tab_title, len(tab_content)]

    def get_tab_title(self, locator):
        get_title = self.element_is_visible(locator).text
        return get_title


class TooltipsPage(BasePage):
    locators = TooltipPageLocators()

    def get_text_from_tooltip(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_el(element)
        self.element_is_visible(wait_elem)
        time.sleep(1)
        tooltip_text = self.element_is_visible(self.locators.TOOLTIPS)
        text = tooltip_text.text
        return text

    def check_tooltips(self):
        tooltip_button = self.get_text_from_tooltip(self.locators.BUTTON,
                                                    self.locators.BUTTON_TOOLTIP)
        tooltip_field = self.get_text_from_tooltip(self.locators.INPUT_FIELD,
                                                   self.locators.INPUT_TOOLTIP)
        tooltip_contrary = self.get_text_from_tooltip(
            self.locators.CONTRARY_TEXT, self.locators.CONTRARY_TOOLTIP)
        tooltip_section = self.get_text_from_tooltip(
            self.locators.SECTION_TEXT, self.locators.SECTION_TOOLTIP)
        return tooltip_button, tooltip_field, tooltip_contrary, tooltip_section


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_item_list = self.element_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_el(item)
            data.append(item.text)
        return data


class SelectMenuPage(BasePage):
    locators = SelectMenuLocators()

    def select_value(self, field, options, value):
        self.element_is_visible(field).click()
        self.element_is_visible(options).click()
        value = self.element_is_visible(value).text
        return value

    def get_old_menu_options(self):
        data = self.element_are_visible(self.locators.OLD_SELECT_MENU_OPTIONS)
        list_opt = []
        for i in data:
            list_opt.append(i.text)
        return list_opt

    def select_value_old(self):
        self.element_is_visible(self.locators.OLD_SELECT_MENU).click()
        self.element_is_visible(self.locators.OLD_MENU_OPTIONS).click()
        value = self.element_is_visible(self.locators.OLD_MENU_OPTIONS).text
        return value

    def select_multi_dropdown(self, colors):
        select_dropdown = self.element_is_visible(self.locators.MULTISELECT_INPUT)
        output = []
        for color in colors:
            select_dropdown.send_keys(color)
            select_dropdown.send_keys(Keys.ENTER)
            output.append(color)
        return output

    def select_standard_multiselect(self, value):
        self.select_multi_options(self.element_is_visible(self.locators.STANDARD_MULTI_SELECT), value)
        opt = self.get_all_selected_opt(self.element_is_visible(self.locators.STANDARD_MULTI_SELECT))
        return opt

