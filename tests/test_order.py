import pytest
import allure
import curl
from generators import *
from text_constants import ORDER_SUCCESSFUL_TEXT
from data import first_data_set_for_order_test, second_data_set_for_order_test
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @pytest.mark.parametrize(
        'name, surname, address, station, phone, day, rental_days, color, comment',
        first_data_set_for_order_test
    )
    @allure.title('Проверка заказа самоката по кнопке "Заказать" в шапке с двумя наборами данных')
    def test_order_scooter_by_button_in_header(self, page, name, surname, address, station,
                                               phone, day, rental_days, color, comment):
        main_page = MainPage(page)
        main_page.load_page(curl.MAIN_PAGE_URL)
        main_page.click_on_order_button_in_header()

        name, surname = fake_data()
        order_page = OrderPage(page)
        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_address(address)
        order_page.set_metro(station)
        order_page.set_phone(fake_phone())
        order_page.click_on_next_button()
        order_page.set_date(day)
        order_page.set_rental_period(rental_days)
        order_page.set_color(color)
        order_page.set_comment(comment)
        order_page.click_on_order_button()
        order_page.click_on_yes_button()
        order_text = order_page.check_order_registration()

        assert ORDER_SUCCESSFUL_TEXT in order_text

    @pytest.mark.parametrize(
        'name, surname, address, station, phone, day, rental_days, color, comment',
        second_data_set_for_order_test
    )
    @allure.title('Проверка заказа самоката по основной кнопке "Заказать" с двумя наборами данных')
    def test_order_scooter_by_main_button(self, page, name, surname, address, station,
                                          phone, day, rental_days, color, comment):
        main_page = MainPage(page)
        main_page.load_page(curl.MAIN_PAGE_URL)
        main_page.click_on_main_order_button()

        name, surname = fake_data()
        order_page = OrderPage(page)
        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_address(address)
        order_page.set_metro(station)
        order_page.set_phone(fake_phone())
        order_page.click_on_next_button()
        order_page.set_date(day)
        order_page.set_rental_period(rental_days)
        order_page.set_color(color)
        order_page.set_comment(comment)
        order_page.click_on_order_button()
        order_page.click_on_yes_button()
        order_text = order_page.check_order_registration()

        assert ORDER_SUCCESSFUL_TEXT in order_text
