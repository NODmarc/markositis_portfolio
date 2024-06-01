from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    #  form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By. CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT_CHECKBOX = (By.CSS_SELECTOR, 'span[class="text-success"]')


class RadioButtonLocators:

    YES_RADIO_BTN = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_RADIO_BTN = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_RADIO_BTN = (By.CSS_SELECTOR, "label[for='noRadio']")
    CHECKED_RADIO_BTN = ".//ancestor::label[@class='custom-control-label']"
    OUTPUT_RESULT_RADIOBUTTON = (By.CSS_SELECTOR, 'p span[class="text-success"]')


class WebTablePageLocators:

    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE = (By.CSS_SELECTOR, "input[id='age']")
    SALARY = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class='close']")

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
