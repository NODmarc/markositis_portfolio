from locators.form_page_locators import RegistrationFormPageLocators
from pages.form_page import RegistrationFormPage


class TestStudentRegistrationFrom:
    def test_submit_registration_form(self, driver):
        submit_form = RegistrationFormPage(driver,
                                           "https://demoqa.com/"
                                           "automation-practice-form")
        submit_form.open()
        input_result = submit_form.fill_registration_form()
        output_result = submit_form.check_filled_form()
        assert input_result == output_result
