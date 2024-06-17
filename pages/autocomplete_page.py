import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from generator.generator import generated_color
from locators.autocomplete_locators import AutocompleteLocators
from pages.base_page import BasePage


class AutocompletePage(BasePage):
    locators = AutocompleteLocators()

    def fill_multi_input(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            multi_input = self.element_is_visible(self.locators.MULTI_INPUT)
            multi_input.send_keys(color)
            multi_input.send_keys(Keys.ENTER)
        return colors

    def remove_all_values_from_multi(self):
        self.element_is_visible(self.locators.MULTI_INPUT_DELETE_ALL_BTN).click()
        try:
            return self.element_are_visible(self.locators.MULTI_INPUT_VALUE)
        except TimeoutException:
            return []

    def removal_one_by_one_values_from_multi(self):
        self.element_is_visible(self.locators.MULTI_INPUT_DELETE_BTN).click()
        self.element_is_visible(self.locators.MULTI_INPUT_DELETE_BTN).click()
        self.element_is_visible(self.locators.MULTI_INPUT_DELETE_BTN).click()
        try:
            return self.element_are_visible(self.locators.MULTI_INPUT_VALUE)
        except TimeoutException:
            return []

    def get_values_from_multi_autocomplete(self):
        color_list = self.element_are_visible(self.locators.MULTI_INPUT_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_single_input(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_single_color(self):
        color = self.element_is_visible(self.locators.SINGLE_INPUT_VALUE)
        return color.text


