import allure
from conftest import driver
from pages.main_page import MainPage



class TestQuestionsInFooter:
    @allure.title('Проверка 1-ого вопроса в футере')
    @allure.description('Нажатие на 1-ый вопрос и проверка, что на него появился нужный ответ')
    def test_check_answer_to_1_st_question(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_footer()
        main_page.click_question_1()
        assert main_page.get_answer_to_question_1_text() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка 2-ого вопроса в футере')
    @allure.description('Нажатие на 2-ой вопрос и проверка, что на него появился нужный ответ')
    def test_check_answer_to_2_nd_question(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_footer()
        main_page.click_question_2()
        assert main_page.get_answer_to_question_2_text() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Проверка 3-его вопроса в футере')
    @allure.description('Нажатие на 3-ий вопрос и проверка, что на него появился нужный ответ')
    def test_check_answer_to_3_rd_question(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_footer()
        main_page.click_question_3()
        assert main_page.get_answer_to_question_3_text() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Проверка 4-ого вопроса в футере')
    @allure.description('Нажатие на 4-ый вопрос и проверка, что на него появился нужный ответ')
    def test_check_answer_to_4_th_question(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_footer()
        main_page.click_question_4()
        assert main_page.get_answer_to_question_4_text() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка 5-ого вопроса в футере')
    @allure.description('Нажатие на 5-ый вопрос и проверка, что на него появился нужный ответ')
    def test_check_answer_to_5_th_question(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_footer()
        main_page.click_question_5()
        assert main_page.get_answer_to_question_5_text() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Проверка 6-ого вопроса в футере')
    @allure.description('Нажатие на 6-ой вопрос и проверка, что на него появился нужный ответ')
    def test_check_answer_to_6_th_question(self, driver):
            main_page = MainPage(driver)
            main_page.scroll_to_footer()
            main_page.click_question_6()
            assert main_page.get_answer_to_question_6_text() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Проверка 7-ого вопроса в футере')
    @allure.description('Нажатие на 7-ой вопрос и проверка, что на него появился нужный ответ')
    def test_check_answer_to_7_th_question(self, driver):
            main_page = MainPage(driver)
            main_page.scroll_to_footer()
            main_page.click_question_7()
            assert main_page.get_answer_to_question_7_text() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Проверка 8-ого вопроса в футере')
    @allure.description('Нажатие на 8-ой вопрос и проверка, что на него появился нужный ответ')
    def test_check_answer_to_8_th_question(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_footer()
        main_page.click_question_8()
        assert main_page.get_answer_to_question_8_text() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'



