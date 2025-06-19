import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Нажать на кнопку "Заказать" в шапке')
    def click_on_order_button_in_header(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_IN_HEADER)

    @allure.step('Нажать на кнопку "Заказать" на странице')
    def click_on_main_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Нажать на вопрос')
    def click_on_the_question(self, number):
        self.click_on_element(MainPageLocators.question(number))

    @allure.step('Получить текст ответа на вопрос')
    def text_in_question(self, number):
        return self.get_text_on_element(MainPageLocators.answer(number))

    @allure.step('Нажать на логотип "Самокат"')
    def click_on_scooter_logo(self):
        self.click_on_element(MainPageLocators.SAMOKAT_LOGO)

    def click_on_yandex_logo(self, title_contains):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)
        new_page = self.switch_to_another_window(title_contains)
        return new_page
