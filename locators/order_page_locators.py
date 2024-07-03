from selenium.webdriver.common.by import By


class Locators:
    # Форма заказа
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    STATION_SOKOLNIKI = (By.XPATH, "//button[@value='4']")
    PHONE_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATA = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATA_SET = (By.XPATH, "//div[@aria-label='Choose пятница, 26-е июля 2024 г.']")
    RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_PERIOD_1_SUTKI = (By.XPATH, "//div[text()='сутки']")
    COLOR_BLACK = (By.ID, "black")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.XPATH, "//button[text()='Назад']/following-sibling::button")
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    WINDOW_ORDER_COMPLETED = (By.XPATH, "//div[text()='Заказ оформлен']")
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")



