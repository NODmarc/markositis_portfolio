import random

from locators.interactions_page_locators import InteractionPageLocators
from pages.base_page import BasePage


class InteractionsPage(BasePage):
    locators = InteractionPageLocators()

    def get_sortable_items(self, elements):
        item_list = self.element_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self, tab, items):
        self.element_is_visible(tab).click()
        order_before = self.get_sortable_items(items)
        item_list = random.sample(self.element_are_visible(items), k=2)
        self.drag_and_drop_to_element(item_list[0], item_list[1])
        order_after = self.get_sortable_items(items)
        return order_before, order_after

    def click_selectable_item(self, elements):
        item_list = self.element_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self, tab, items, active_item):
        self.element_is_visible(tab).click()
        self.click_selectable_item(items)
        active_element = self.element_is_visible(active_item)
        return active_element.text

    def get_pixels_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        self.drag_and_drop(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_pixels_from_width_height(self.get_max_min(self.locators.RESIZABLE_BOX))
        self.drag_and_drop(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -400, -200)
        min_size = self.get_pixels_from_width_height(self.get_max_min(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resizable(self):
        self.drag_and_drop(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_pixels_from_width_height(self.get_max_min(self.locators.RESIZABLE_BOX))
        self.drag_and_drop(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_pixels_from_width_height(self.get_max_min(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def drop_simple(self):
        drag_div = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        drop_div = self.element_is_visible(self.locators.SIMPLE_DROP_HERE)
        self.drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_acceptable = self.element_is_visible(self.locators.ACCEPT_ACCEPTABLE)
        drag_not_acceptable = self.element_is_visible(self.locators.ACCEPT_NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.ACCEPT_DROP_HERE)
        self.drag_and_drop_to_element(drag_not_acceptable, drop_div)
        drop_text_not_acceptable = drop_div.text
        self.drag_and_drop_to_element(drag_acceptable, drop_div)
        drop_text_acceptable = drop_div.text
        return drop_text_not_acceptable, drop_text_acceptable

