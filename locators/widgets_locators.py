import random

from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_WHAT_TITLE = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECTION_WHAT_TEXT = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    SECTION_WHERE_TITLE = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECTION_WHERE_TEXT = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    SECTION_WHY_TITLE = (By.CSS_SELECTOR, "div[id='section3Heading']")
    SECTION_WHY_TEXT = (By.CSS_SELECTOR, "div[id='section3Content'] p")


class DataPickerPageLocators:
    DATE_PICKER_INPUT = (
        By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    DATE_PICKER_SELECT_MONTH = (
        By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    DATE_PICKER_SELECT_YEAR = (
        By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    DATE_PICKER_SELECT_DAY_LIST = (By.CSS_SELECTOR,
                                   "div[class^='react-datepicker__day react-datepicker__day']")

    DATE_AND_TIME_INPUT = (
        By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_AND_TIME_MONTH = (
        By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_AND_TIME_YEAR = (
        By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    DATE_AND_TIME_TIME_LIST = (
        By.CSS_SELECTOR, "li[class^='react-datepicker__time-list-item']")
    DATE_AND_TIME_MONTH_LIST = (
        By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    DATE_AND_TIME_YEAR_LIST = (
        By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")
    DATE_AND_TIME_DAY_LIST = (
        By.CSS_SELECTOR, "div[class='react-datepicker__week'] div")


class SliderPageLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR,
                    "input[class='range-slider range-slider--primary']")
    SLIDER_RESULT = (By.CSS_SELECTOR, "input[id='sliderValue']")


class ProgressBarLocators:
    START_STOP_BUTTON = (By.CSS_SELECTOR,
                    "button[id='startStopButton']")
    RESET_BUTTON = (By.CSS_SELECTOR,
                    "button[id='resetButton']")
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR,
                    "div[class='progress-bar bg-info']")


class TabsPageLocators:
    WHAT_TAB = (By.CSS_SELECTOR,
                    "a[id='demo-tab-what']")
    WHAT_TAB_TEXT = (By.CSS_SELECTOR,
                    "div[id='demo-tabpane-what'] p")
    ORIGIN_TAB = (By.CSS_SELECTOR,
                "a[id='demo-tab-origin']")
    ORIGIN_TAB_TEXT = (By.CSS_SELECTOR,
                     "div[id='demo-tabpane-origin'] p")
    USE_TAB = (By.CSS_SELECTOR,
                  "a[id='demo-tab-use']")
    USE_TAB_TEXT = (By.CSS_SELECTOR,
                       "div[id='demo-tabpane-use'] p")
    MORE_TAB = (By.CSS_SELECTOR,
               "a[id='demo-tab-more']")
    MORE_TAB_TEXT = (By.CSS_SELECTOR,
                       "div[id='demo-tabpane-more'] p")


class TooltipPageLocators:
    BUTTON = (By.CSS_SELECTOR,
                       "button[id='toolTipButton']")
    BUTTON_TOOLTIP = (By.CSS_SELECTOR,
                       "button[aria-describedby='buttonToolTip']")
    INPUT_FIELD = (By.CSS_SELECTOR,
                       "input[id='toolTipTextField']")
    INPUT_TOOLTIP = (By.CSS_SELECTOR,
                           "input[aria-describedby='textFieldToolTip']")
    CONTRARY_TEXT = (By.XPATH,
                       "//*[.='Contrary']")
    CONTRARY_TOOLTIP = (By.CSS_SELECTOR,
                           "a[aria-describedby='contraryTexToolTip']")
    SECTION_TEXT = (By.XPATH,
                        "//*[.='1.10.32']")
    SECTION_TOOLTIP = (By.CSS_SELECTOR,
                           "a[aria-describedby='sectionToolTip']")
    TOOLTIPS = (By.CSS_SELECTOR,
                           "div[class='tooltip-inner']")


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, "ul[id='nav'] li a")


class SelectMenuLocators:
    SELECT_FIELD = (By.CSS_SELECTOR, "div[id='withOptGroup']")
    SELECT_OPTIONS_LIST = (By.CSS_SELECTOR, "div[class=' css-11unzgr']")
    SELECT_OPTIONS_1 = (By.CSS_SELECTOR, "div[id='react-select-2-option-0-0']")
    SELECT_OPTIONS_2 = (By.CSS_SELECTOR, "div[id='react-select-2-option-0-1']")
    SELECT_OPTIONS_3 = (By.CSS_SELECTOR, "div[id='react-select-2-option-2']")
    SELECT_OPTIONS_4 = (By.CSS_SELECTOR, "div[id='react-select-2-option-3']")
    SELECT_VALUE = (By.CSS_SELECTOR, "div[class=' css-1uccc91-singleValue']")

    SELECT_ONE = (By.CSS_SELECTOR, "div[id='selectOne']")
    SELECT_TITLE = (By.CSS_SELECTOR, fr"div[id='react-select-3-option-0-{random.randint(0, 5)}']")

    OLD_SELECT_MENU = (By.CSS_SELECTOR, "select[id='oldSelectMenu']")
    OLD_SELECT_MENU_OPTIONS = (By.CSS_SELECTOR, "select[id='oldSelectMenu'] option")
    OLD_MENU_OPTIONS = (By.CSS_SELECTOR, f"option[value='{random.choice(['red', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}']")

    MULTISELECT_DROP_DOWN = (By.CSS_SELECTOR, "div[class=' css-1hwfws3']")
    MULTISELECT_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")

    STANDARD_MULTI_SELECT = (By.CSS_SELECTOR, "select[id='cars']")
