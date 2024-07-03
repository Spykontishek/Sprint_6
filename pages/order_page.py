from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import Locators
from constants import Constants


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*Locators.NAME).send_keys(name)

    def set_surname(self,surname):
        self.driver.find_element(*Locators.SURNAME).send_keys(surname)

    def set_address(self,address):
        self.driver.find_element(*Locators.ADDRESS).send_keys(address)

    def click_on_station(self):
        self.driver.find_element(*Locators.STATION).click()

    def choice_station_sokolniki(self):
        self.driver.find_element(*Locators.STATION_SOKOLNIKI).click()

    def set_phone_number(self,phone_number):
        self.driver.find_element(*Locators.PHONE_NUMBER).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*Locators.NEXT_BUTTON).click()

    def wait_2_nd_order_form_is_enabled(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Locators.DATA))

    def set_data(self, data):
        element = self.driver.find_element(*Locators.DATA)
        element.send_keys(data)
        element.send_keys(Keys.ENTER)

    def click_rental_period(self):
        self.driver.find_element(*Locators.RENTAL_PERIOD).click()

    def choice_rental_period(self):
        self.driver.find_element(*Locators.RENTAL_PERIOD_1_SUTKI).click()

    def click_color_black(self):
        self.driver.find_element(*Locators.COLOR_BLACK).click()

    def set_comment(self,comment):
        self.driver.find_element(*Locators.COMMENT).send_keys(comment)

    def click_button_order(self):
        self.driver.find_element(*Locators.BUTTON_ORDER).click()

    def wait_confirmation_window_is_enabled(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Locators.BUTTON_YES))

    def click_button_yes(self):
        self.driver.find_element(*Locators.BUTTON_YES).click()

    def wait_window_order_completed(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Locators.WINDOW_ORDER_COMPLETED))

    def click_logo_scooter(self):
        self.driver.find_element(*Locators.LOGO_SCOOTER).click()

    def wait_to_go_to_main_url(self):
        WebDriverWait(self.driver, 3).until(EC.url_to_be(Constants.URL))

    def click_logo_yandex(self):
        self.driver.find_element(*Locators.LOGO_YANDEX).click()

    def wait_to_go_to_dzen_url(self):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(Constants.DZEN_URL))

    def order_form(self, name, surname, address, phone_number, data, comment):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_on_station()
        self.choice_station_sokolniki()
        self.set_phone_number(phone_number)
        self.click_next_button()
        self.wait_2_nd_order_form_is_enabled()
        self.set_data(data)
        self.click_rental_period()
        self.choice_rental_period()
        self.click_color_black()
        self.set_comment(comment)
        self.click_button_order()
        self.wait_confirmation_window_is_enabled()
        self.click_button_yes()
        self.wait_window_order_completed()





















