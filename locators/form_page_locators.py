from selenium.webdriver.common.by import By


class RegistrationFormPageLocators:
    # form fields
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER_MALE_INPUT = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE_INPUT = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_OTHER_INPUT = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    MOBILE_INPUT = (By.CSS_SELECTOR, "input[id='userNumber']")
    DOB_INPUT = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    DOB_DIV = (By.CSS_SELECTOR, "div[class='react-datepicker__input-container']")
    DATE = (By.CSS_SELECTOR, "div[class='react-datepicker__day react-datepicker__day--013']")
    SUBJECTS_INPUT = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBIES_CHECKBOX_SPORT = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_CHECKBOX_READING = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    HOBBIES_CHECKBOX_MUSIC = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    UPLOAD_PICTURE_INPUT = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS_INPUT = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    STATE_INPUT = (By.CSS_SELECTOR, "div[id='state']")
    CITY_INPUT = (By.CSS_SELECTOR, "div[id='city']")
    STATE_CITY_INPUT_OPTIONS = (By.CSS_SELECTOR, "div[class=' css-26l3qy-menu']")
    STATE_TEXT = (By.CSS_SELECTOR, "div[id='state']")
    CITY_TEXT = (By.CSS_SELECTOR, "div[id='city']")

    # button
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[id='submit']")

    # modal form fields
    TABLE_FULL_NAME = (By.XPATH, "//tr[1]/td[2]")
    TABLE_EMAIL = (By.XPATH, "//tr[2]/td[2]")
    TABLE_GENDER = (By.XPATH, "//tr[3]/td[2]")
    TABLE_MOBILE = (By.XPATH, "//tr[4]/td[2]")
    TABLE_DOB = (By.XPATH, "//tr[5]/td[2]")
    TABLE_SUBJECTS = (By.XPATH, "//tr[6]/td[2]")
    TABLE_HOBBIES = (By.XPATH, "//tr[7]/td[2]")
    TABLE_PICTURE = (By.XPATH, "//tr[8]/td[2]")
    TABLE_ADDRESS = (By.XPATH, "//tr[9]/td[2]")
    TABLE_STATE_CITY = (By.XPATH, "//tr[10]/td[2]")


    # modal form button
    CLOSE_BTN = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
