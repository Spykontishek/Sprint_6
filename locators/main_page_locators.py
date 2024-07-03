from selenium.webdriver.common.by import By


class Locators:
    # Подвал страницы с "Вопросами о важном"
    FIRST_QUESTION = (By.ID, "accordion__heading-0")
    SECOND_QUESTION = (By.ID, "accordion__heading-1")
    THIRD_QUESTION = (By.ID, "accordion__heading-2")
    FOURTH_QUESTIONS = (By.ID, "accordion__heading-3")
    FIFTH_QUESTIONS = (By.ID, "accordion__heading-4")
    SIXTH_QUESTIONS = (By.ID, "accordion__heading-5")
    SEVENTH_QUESTIONS = (By.ID, "accordion__heading-6")
    EIGHTH_QUESTIONS = (By.ID, "accordion__heading-7")
    ANSWER_TO_1_ST_QUESTION = (By.XPATH, "//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    ANSWER_TO_2_ND_QUESTION = (By.XPATH, "//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")
    ANSWER_TO_3_RD_QUESTION = (By.XPATH, "//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")
    ANSWER_TO_4_TH_QUESTION = (By.XPATH, "//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    ANSWER_TO_5_TH_QUESTION = (By.XPATH, "//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")
    ANSWER_TO_6_TH_QUESTION = (By.XPATH, "//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")
    ANSWER_TO_7_TH_QUESTION = (By.XPATH, "//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")
    ANSWER_TO_8_TH_QUESTION = (By.XPATH, "//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")

    # Верхняя и нижняя кнопки "Заказать"
    TOP_BUTTON_ORDER = (By.XPATH, "//button[text()='Статус заказа']/preceding-sibling::button")
    BOTTOM_BUTTON_ORDER = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button")