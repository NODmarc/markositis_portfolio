import random
import time

from selenium.webdriver.support.select import Select

from enums.years import YEAR_LIST
from generator.generator import generated_date
from locators.widgets_locators import AccordianPageLocators, \
    DataPickerPageLocators, SliderPageLocators, ProgressBarLocators
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
        value_before = self.element_is_visible(self.locators.SLIDER_RESULT).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.drag_and_drop(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_RESULT).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarLocators()

    def check_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        progress_bar_start = self.element_is_visible(self.locators.START_STOP_BUTTON)
        progress_bar_start.click()
        time.sleep(random.randint(4, 6))
        self.element_is_visible(self.locators.START_STOP_BUTTON).click()
        value_after_stop = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        progress_bar_start.click()
        time.sleep(5)
        self.element_is_visible(self.locators.RESET_BUTTON).click()
        value_after_reset = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        return value_before, value_after_stop, value_after_reset


