import base64
import os
import random
import time

import requests
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, \
    CheckBoxPageLocators, RadioButtonLocators, WebTablePageLocators, \
    ButtonPageLocators, LinksPageLocators, FilePageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(
            current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(
            permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = \
            self.element_is_present(
                self.locators.CREATED_FULL_NAME).text.split(
                ':')[1]
        email = \
            self.element_is_present(self.locators.CREATED_EMAIL).text.split(
                ':')[1]
        current_address = self.element_is_present(
            self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(
            self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.element_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.',
                                                                     '').lower()

    def get_output_result(self):
        result_list = self.element_are_present(
            self.locators.OUTPUT_RESULT_CHECKBOX)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).lower().replace(' ', '')


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_on_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_RADIO_BTN,
            'impressive': self.locators.IMPRESSIVE_RADIO_BTN,
            'no': self.locators.NO_RADIO_BTN
        }
        self.element_is_visible(choices[choice]).click()

    def get_selected_radio_button(self):
        result_list = self.element_are_present(self.locators.CHECKED_RADIO_BTN)
        data = []
        for item in result_list:
            data.append(item.text)
        return data

    def get_selected_result(self):
        return self.element_is_present(
            self.locators.OUTPUT_RESULT_RADIOBUTTON).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self, count=1):
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(
                firstname)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(
                lastname)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.AGE).send_keys(age)
            self.element_is_visible(self.locators.SALARY).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT).send_keys(
                department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary),
                    department]

    def check_new_added_person(self):
        people_list = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_person(self, keyword):
        self.element_is_visible(self.locators.SEARCH).send_keys(keyword)

    def check_searched_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        """Function can update random input fields. Own code."""
        person_info = next(generated_person())
        person_data = [person_info.firstname,
                       person_info.age,
                       person_info.lastname,
                       person_info.email,
                       person_info.salary,
                       person_info.department]
        random_data = person_data[random.randint(0, 5)]
        if random_data == person_info.age:
            self.element_is_visible(self.locators.EDIT_BUTTON).click()
            self.element_is_visible(self.locators.AGE).clear()
            self.element_is_visible(self.locators.AGE).send_keys(random_data)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return str(random_data)
        elif random_data == person_info.firstname:
            self.element_is_visible(self.locators.EDIT_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).clear()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(
                random_data)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return str(random_data)
        elif random_data == person_info.lastname:
            self.element_is_visible(self.locators.EDIT_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).clear()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(
                random_data)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return str(random_data)
        elif random_data == person_info.email:
            self.element_is_visible(self.locators.EDIT_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).clear()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(
                random_data)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return str(random_data)
        elif random_data == person_info.salary:
            self.element_is_visible(self.locators.EDIT_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).clear()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(
                random_data)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return str(random_data)
        elif random_data == person_info.department:
            self.element_is_visible(self.locators.EDIT_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).clear()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(
                random_data)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return str(random_data)
        else:
            print('Error: No change field found')

        '''Function for update only one input field. Code from course'''
        # person_info = next(generated_person())
        # age = person_info.age
        # self.element_is_visible(self.locators.EDIT_BUTTON).click()
        # self.element_is_visible(self.locators.AGE).clear()
        # self.element_is_visible(self.locators.AGE).send_keys(age)
        # self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        # return str(age)

    def delete_person_info(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):
        return self.element_is_present(self.locators.NO_DATA_TEXT).text

    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_btn = self.element_is_visible(
                self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_btn)
            count_row_btn.click()
            self.element_is_visible(
                (By.CSS_SELECTOR, f'option[value="x"]')).click()
            data.append(self.check_count_rows())

    def check_count_rows(self):
        list_rows = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonPageLocators()

    def click_on_diff_btn(self, type_click):
        if type_click == "double":
            self.action_double_click(
                self.element_is_visible(self.locators.DOUBLE_BTN))
            return self.check_clicked_on_button(self.locators.SUCCESS_DOUBLE)
        if type_click == "right":
            self.action_right_click(
                self.element_is_visible(self.locators.RIGHT_CLICK_BTN))
            return self.check_clicked_on_button(self.locators.SUCCESS_RIGHT)
        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME).click()
            return self.check_clicked_on_button(self.locators.SUCCESS_CLICK_ME)

    def check_clicked_on_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab(self, link):
        if link == "simple":
            simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
            link_href = simple_link.get_attribute('href')
            request = requests.get(link_href)
            if request.status_code == 200:
                simple_link.click()
                new_tab_url = BasePage.switch_to_new_tab(self)
                return link_href, new_tab_url
            else:
                return link_href, request.status_code
        if link == 'dynamic':
            simple_link = self.element_is_visible(self.locators.DYNAMIC_LINK)
            link_href = simple_link.get_attribute('href')
            request = requests.get(link_href)
            if request.status_code == 200:
                simple_link.click()
                new_tab_url = BasePage.switch_to_new_tab(self)
                return link_href, new_tab_url
            else:
                return link_href, request.status_code

    def check_request_status_code(self, endpoint):
        url = 'https://demoqa.com'
        if endpoint == '/invalid-url':
            self.element_is_present(self.locators.INVALID_URL_LINK).click()
            response = requests.get(f'{url}'+f'{endpoint}')
            return response.status_code
        if endpoint == "/forbidden":
            self.element_is_present(self.locators.FORBIDDEN_LINK).click()
            response = requests.get(f'{url}' + f'{endpoint}')
            return response.status_code
        if endpoint == '/unauthorized':
            self.element_is_present(self.locators.UNAUTHORIZED_LINK).click()
            response = requests.get(f'{url}' + f'{endpoint}')
            return response.status_code
        if endpoint == '/moved':
            self.element_is_present(self.locators.MOVED_LINK).click()
            response = requests.get(f'{url}' + f'{endpoint}')
            return response.status_code
        if endpoint == '/no-content':
            self.element_is_present(self.locators.NO_CONTENT_LINK).click()
            response = requests.get(f'{url}' + f'{endpoint}')
            return response.status_code
        if endpoint == '/created':
            self.element_is_present(self.locators.CREATED_LINK).click()
            response = requests.get(f'{url}' + f'{endpoint}')
            return response.status_code

    def check_broken_link(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST_LINK).click()
        else:
            return r.status_code


class FilePage(BasePage):
    locators = FilePageLocators()

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        text = self.element_is_present(self.locators.UPLOADED_FILE).text
        os.remove(path)
        return file_name.split('/')[-1], text.split('\\')[-1]

    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'/Users/markositis/Downloads/filetest{random.randint(0, 999)}.jpeg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file

