import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнить поле "Имя"')
    def set_name(self, keys):
        self.send_keys_to_input(OrderPageLocators.NAME_FIELD, keys)

    @allure.step('Заполнить поле "Фамилия"')
    def set_surname(self, keys):
        self.send_keys_to_input(OrderPageLocators.SURNAME_FIELD, keys)

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, keys):
        self.send_keys_to_input(OrderPageLocators.ADDRESS_FIELD, keys)

    @allure.step('Заполнить поле "Станция метро"')
    def set_metro(self, keys):
        self.send_keys_to_input(OrderPageLocators.METRO_FIELD, keys)
        self.click_on_element(OrderPageLocators.METRO_FIELD_SELECT)

    @allure.step('Заполнить поле "Телефон"')
    def set_phone(self, keys):
        self.send_keys_to_input(OrderPageLocators.PHONE_FIELD, keys)

    @allure.step('Нажимаем на кнопку "Далее"')
    def click_on_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить поле "Когда привезти самокат?"')
    def set_date(self, day):
        self.click_on_element(OrderPageLocators.DATE_FIELD)
        self.click_on_element(OrderPageLocators.choose_date(day))

    @allure.step('Заполнить поле "Срок аренды"')
    def set_rental_period(self, days):
        self.click_on_element(OrderPageLocators.RENTAL_FIELD)
        self.click_on_element(OrderPageLocators.rental_value(days))

    @allure.step('Заполнить поле "Цвет самоката"')
    def set_color(self, color):
        self.click_on_element(OrderPageLocators.color_field(color))

    @allure.step('Заполнить поле "Комментарий для курьера"')
    def set_comment(self, keys):
        self.send_keys_to_input(OrderPageLocators.COMMENT_FIELD, keys)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_on_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.wait_for_element(OrderPageLocators.ORDER_CONFIRMATION_BUTTON)

    @allure.step('Нажать на кнопку "Да" в окне "Хотите оформить заказ?"')
    def click_on_yes_button(self):
        self.wait_for_element(OrderPageLocators.ORDER_CONFIRMATION_BUTTON)
        self.click_on_element(OrderPageLocators.ORDER_CONFIRMATION_BUTTON)

    @allure.step('Получить текст в окне "Заказ оформлен"')
    def check_order_registration(self):
        return self.get_text_on_element(OrderPageLocators.ORDER_SUCCESSFUL)
