import allure
import curl
from pages.main_page import MainPage


class TestTransition:

    @allure.title('Проверка перехода на главную страницу по клику на логотип "Самокат"')
    @allure.description('Кликаем на логотип "Самокат" и проверяем, что переходим на главную страницу "Яндекс.Самокат"')
    def test_scooter_logo(self, page):
        main_page = MainPage(page)
        main_page.load_page(curl.MAIN_PAGE_URL)
        main_page.click_on_scooter_logo()
        url = main_page.return_url()

        assert url == curl.MAIN_PAGE_URL

    @allure.title('Проверка перехода на главную страницу "Дзен" по клику на логотип "Яндекс"')
    @allure.description('Кликаем на логотип "Яндекс" и проверяем, что переходим на главную страницу "Дзен"')
    def test_yandex_logo(self, page):
        main_page = MainPage(page)
        main_page.load_page(curl.MAIN_PAGE_URL)
        new_page = main_page.click_on_yandex_logo('Дзен')

        assert curl.DZEN_MAIN_PAGE_URL in new_page.url

