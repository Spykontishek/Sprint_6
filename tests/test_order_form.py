import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import Locators
from constants import Constants
from pages.order_page import OrderPage
from conftest import driver
from datetime import datetime, timedelta


class TestOrderForm:
    @allure.title('Проверка оформления заказа')
    @allure.description('Позитивный тест прогонка 2-ух тестовых сценариев с помощью параметризации для формы заказа и проверка, что в конце появляется окно "Заказ оформлен"')
    @pytest.mark.parametrize("name, surname, address, phone_number, data, comment", [
        ["Артем", "Петров", "Москва, ул. Комсомольская, д. 10", "+79161234567",
         (datetime.now() + timedelta(days=5)).strftime('%d.%m.%Y'), "Коммент"],
        ["Петр", "Иванов", "Санкт-Петербург, ул. Ленина, д. 20", "+79167654321",
         (datetime.now() + timedelta(days=6)).strftime('%d.%m.%Y'), "Комментарий"]])

    def test_order_form(self, driver, name, surname, address, phone_number, data, comment):
        driver.get(Constants.ORDER_URL)
        order_page = OrderPage(driver)
        order_page.order_form(name, surname, address, phone_number, data, comment)
        assert 'Заказ оформлен' in driver.find_element(*Locators.WINDOW_ORDER_COMPLETED).text


