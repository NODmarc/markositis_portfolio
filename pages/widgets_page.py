from locators.widgets_locators import AccordianPageLocators
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
        section_title = self.element_is_visible(accordian[accordian_name]['title']).text
        self.element_is_visible(accordian[accordian_name]['title']).click()
        section_text = self.element_is_visible(accordian[accordian_name]['text']).text
        return [section_title, len(section_text)]
