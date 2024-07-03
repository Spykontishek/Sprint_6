import allure
from constants import Constants
from pages.main_page import MainPage
from conftest import driver


class TestButtonsOrder:
    @allure.title('Проверка верхней кнопки "Заказать"')
    @allure.description('Нажатие на кнопку и проверка, что она переведет на форму заказа')
    def test_go_to_order_form_from_top_button_order(self, driver):
        main_page = MainPage(driver)
        main_page.click_top_button_order()
        main_page.wait_to_go_to_order_form()
        current_url = driver.current_url
        assert current_url == Constants.ORDER_URL

    @allure.title('Проверка нижней кнопки "Заказать"')
    @allure.description('Нажатие на кнопку и проверка, что она переведет на форму заказа')
    def test_go_to_order_form_from_bottom_button_order(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_bottom_button_order()
        main_page.click_bottom_button_order()
        main_page.wait_to_go_to_order_form()
        current_url = driver.current_url
        assert current_url == Constants.ORDER_URL