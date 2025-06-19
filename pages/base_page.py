import re
import allure
from playwright.sync_api import expect
from config import TIMEOUT_VALUE


class BasePage:

    def __init__(self, page):
        self.page = page

    @allure.step('Загрузить страницу')
    def load_page(self, url):
        self.page.goto(url)

    @allure.step('Подождать видимость элемента')
    def wait_for_element(self, locator, timeout=TIMEOUT_VALUE):
        expect(self.page.locator(locator)).to_be_visible(timeout=timeout)

    @allure.step('Подождать невидимость элемента')
    def wait_for__invisible_element(self, locator, timeout=TIMEOUT_VALUE):
        expect(self.page.locator(locator)).to_be_hidden(timeout=timeout)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator, timeout=TIMEOUT_VALUE):
        self.page.locator(locator).click(timeout=timeout)

    @allure.step('Ввести текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout=TIMEOUT_VALUE):
        element = self.page.locator(locator)
        element.clear(timeout=timeout)
        element.fill(keys)

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator, timeout=TIMEOUT_VALUE):
        element = self.page.locator(locator)
        return element.inner_text(timeout=timeout)

    @allure.step('Переключится на другое окно')
    def switch_to_another_window(self, title_contains=None, timeout=TIMEOUT_VALUE):
        new_page = self.page.context.wait_for_event("page", timeout=timeout)
        expect(new_page).to_have_title(
            re.compile(title_contains),
            timeout=timeout)
        new_page.bring_to_front()
        return new_page

    @allure.step('Вернуть текущий URL')
    def return_url(self):
        return self.page.url
