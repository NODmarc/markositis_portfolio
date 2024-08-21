import os
import random

from selenium.webdriver.common.keys import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import RegistrationFormPageLocators
from pages.base_page import BasePage


class RegistrationFormPage(BasePage):
    locators = RegistrationFormPageLocators()

    def fill_registration_form(self):
        # Test data
        person_info = next(generated_person())
        first_name = person_info.firstname
        last_name = person_info.lastname
        email = person_info.email
        gender = random.choice(['Male', 'Female', 'Other'])
        mobile = person_info.mobile
        subjects = random.choice(['Maths', 'Hindi', 'English'])
        hobbies = random.choice([self.locators.HOBBIES_CHECKBOX_MUSIC,
                                 self.locators.HOBBIES_CHECKBOX_SPORT,
                                 self.locators.HOBBIES_CHECKBOX_READING])
        current_address = person_info.current_address
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(
            first_name)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(
            last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
        self.click_on_radio_button(gender)
        self.element_is_visible(self.locators.MOBILE_INPUT).send_keys(mobile)
        dob = self.select_date_picker()
        self.select_subject_autocomplete(subjects)
        self.element_is_visible(hobbies).click()
        hobbies_text = self.element_is_visible(hobbies).text
        picture = self.upload_file()
        self.element_is_visible(self.locators.CURRENT_ADDRESS_INPUT).send_keys(
            current_address)
        first_option_state = self.select_state_in_autocomplete()
        first_option_city = self.select_city_in_autocomplete()
        self.element_is_visible(self.locators.SUBMIT_BTN).click()
        return first_name, last_name, email, gender, mobile[0:10], dob.replace(
            'Jun', 'June'), subjects, \
            hobbies_text, picture, current_address, first_option_state, first_option_city

    def click_on_radio_button(self, choice):
        locators = RegistrationFormPageLocators()
        choices = {
            'Male': locators.GENDER_MALE_INPUT,
            'Female': locators.GENDER_FEMALE_INPUT,
            'Other': locators.GENDER_OTHER_INPUT,
        }
        self.element_is_visible(choices[choice]).click()

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_PICTURE_INPUT).send_keys(
            path)
        os.remove(path)
        return file_name.split('/')[-1]

    def select_state_in_autocomplete(self):
        elem = self.element_is_visible(self.locators.STATE_INPUT)
        elem.click()
        first_option_state = self.element_is_visible(
            self.locators.STATE_CITY_INPUT_OPTIONS)
        first_option_state.click()
        data = self.element_is_visible(self.locators.STATE_TEXT).text
        state = data.split()[1].replace(',', '')
        return state

    def select_city_in_autocomplete(self):
        elem = self.element_is_visible(self.locators.CITY_INPUT)
        elem.click()
        first_option_city = self.element_is_visible(
            self.locators.STATE_CITY_INPUT_OPTIONS)
        first_option_city.click()
        data = self.element_is_present(self.locators.CITY_TEXT).text
        city = data.split()[1].replace(',', '')
        return city

    def select_subject_autocomplete(self, subject):
        self.element_is_visible(self.locators.SUBJECTS_INPUT).click()
        select_autocomplete = self.element_is_visible(
            self.locators.SUBJECTS_INPUT)
        select_autocomplete.click()
        select_autocomplete.send_keys(subject)
        select_autocomplete.send_keys(Keys.ENTER)

    def select_date_picker(self):
        self.element_is_visible(self.locators.DOB_INPUT).click()
        self.element_is_visible(self.locators.DATE).click()
        save_date = self.element_is_visible(
            self.locators.DOB_INPUT).get_attribute('value')
        return save_date

    def check_filled_form(self):
        full_name_output = self.element_is_present(
            self.locators.TABLE_FULL_NAME).text
        first_name = full_name_output.split()[0]
        last_name = full_name_output.split()[1]
        email_output = self.element_is_present(self.locators.TABLE_EMAIL).text
        gender_output = self.element_is_present(
            self.locators.TABLE_GENDER).text
        mobile_output = self.element_is_present(
            self.locators.TABLE_MOBILE).text
        dob_output = self.element_is_present(self.locators.TABLE_DOB).text
        subjects_output = self.element_is_present(
            self.locators.TABLE_SUBJECTS).text
        hobbies_output = self.element_is_present(
            self.locators.TABLE_HOBBIES).text
        picture_output = self.element_is_present(
            self.locators.TABLE_PICTURE).text
        address_output = self.element_is_present(
            self.locators.TABLE_ADDRESS).text
        state_city_output = self.element_is_present(
            self.locators.TABLE_STATE_CITY).text
        state = state_city_output.split()[0]
        city = state_city_output.split()[1]
        return first_name, last_name, email_output, gender_output, mobile_output, \
            dob_output.replace(',', ' '), subjects_output, hobbies_output, picture_output, address_output, state, city
