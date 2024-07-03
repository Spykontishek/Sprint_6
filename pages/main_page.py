from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import Locators
from constants import Constants


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_footer(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def click_question_1(self):
        self.driver.find_element(*Locators.FIRST_QUESTION).click()

    def get_answer_to_question_1_text(self):
        return self.driver.find_element(*Locators.ANSWER_TO_1_ST_QUESTION).text

    def click_question_2(self):
        self.driver.find_element(*Locators.SECOND_QUESTION).click()

    def get_answer_to_question_2_text(self):
        return self.driver.find_element(*Locators.ANSWER_TO_2_ND_QUESTION).text

    def click_question_3(self):
        self.driver.find_element(*Locators.THIRD_QUESTION).click()

    def get_answer_to_question_3_text(self):
        return self.driver.find_element(*Locators.ANSWER_TO_3_RD_QUESTION).text

    def click_question_4(self):
        self.driver.find_element(*Locators.FOURTH_QUESTIONS).click()

    def get_answer_to_question_4_text(self):
        return self.driver.find_element(*Locators.ANSWER_TO_4_TH_QUESTION).text

    def click_question_5(self):
        self.driver.find_element(*Locators.FIFTH_QUESTIONS).click()

    def get_answer_to_question_5_text(self):
        return self.driver.find_element(*Locators.ANSWER_TO_5_TH_QUESTION).text

    def click_question_6(self):
        self.driver.find_element(*Locators.SIXTH_QUESTIONS).click()

    def get_answer_to_question_6_text(self):
        return self.driver.find_element(*Locators.ANSWER_TO_6_TH_QUESTION).text

    def click_question_7(self):
        self.driver.find_element(*Locators.SEVENTH_QUESTIONS).click()

    def get_answer_to_question_7_text(self):
        return self.driver.find_element(*Locators.ANSWER_TO_7_TH_QUESTION).text

    def click_question_8(self):
        self.driver.find_element(*Locators.EIGHTH_QUESTIONS).click()

    def get_answer_to_question_8_text(self):
        return self.driver.find_element(*Locators.ANSWER_TO_8_TH_QUESTION).text

    def click_top_button_order(self):
        self.driver.find_element(*Locators.TOP_BUTTON_ORDER).click()

    def click_bottom_button_order(self):
        self.driver.find_element(*Locators.BOTTOM_BUTTON_ORDER).click()

    def wait_to_go_to_order_form(self):
        WebDriverWait(self.driver, 3).until(EC.url_to_be(Constants.ORDER_URL))

    def scroll_to_bottom_button_order(self):
        element = self.driver.find_element(*Locators.BOTTOM_BUTTON_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


