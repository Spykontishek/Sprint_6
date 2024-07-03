import allure
from constants import Constants
from pages.order_page import OrderPage
from conftest import driver


class TestClickONLogo:
    @allure.title('Проверка кнопки "Самокат" в логотипе')
    @allure.description('Нажатие на кнопку и проверка, что она переведет на главную страницу Яндекс Самоката "https://qa-scooter.praktikum-services.ru/"')
    def test_сlick_scooter(self, driver):
        driver.get(Constants.ORDER_URL)
        order_page = OrderPage(driver)
        order_page.click_logo_scooter()
        order_page.wait_to_go_to_main_url()
        assert driver.current_url == Constants.URL

    @allure.title('Проверка кнопки "Яндекс" в логотипе')
    @allure.description('Нажатие на кнопку и проверка, что она переведет на главную страницу Дзена "https://dzen.ru/?yredirect=true"')
    def test_сlick_yandex(self, driver):
        order_page = OrderPage(driver)
        order_page.click_logo_yandex()
        original_window = driver.current_window_handle
        new_window = [window for window in driver.window_handles if window != original_window][0]
        driver.switch_to.window(new_window)
        order_page.wait_to_go_to_dzen_url()
        assert driver.current_url == Constants.DZEN_URL

