class OrderPageLocators:

    NEXT_BUTTON = (
        "xpath=//button[text()='Далее']"
    )

    ORDER_BUTTON = (
        "xpath=//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"
    )

    ORDER_CONFIRMATION = (
        "xpath=//div[text()='Хотите оформить заказ?']"
    )

    ORDER_CONFIRMATION_BUTTON = (
        "xpath=//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"
    )

    ORDER_SUCCESSFUL = (
        "xpath=//div[contains(text(), 'Заказ оформлен')]"
    )

    NAME_FIELD = (
        "xpath=//input[@placeholder='* Имя']"
    )

    SURNAME_FIELD = (
        "xpath=//input[@placeholder='* Фамилия']"
    )

    ADDRESS_FIELD = (
        "xpath=//input[@placeholder='* Адрес: куда привезти заказ']"
    )

    METRO_FIELD = (
        'css=.select-search__input'
    )

    METRO_FIELD_SELECT = (
        "xpath=//div[@class='select-search__select']"
    )

    PHONE_FIELD = (
        "xpath=//input[@placeholder='* Телефон: на него позвонит курьер']"
    )

    DATE_FIELD = (
        "xpath=//input[@placeholder='* Когда привезти самокат']"
    )

    @staticmethod
    def choose_date(day):
        return f'xpath=//div[contains(@class, "react-datepicker__day") and text()={day}]'

    RENTAL_FIELD = (
        'css=.Dropdown-root'
    )

    OVERLAY = (
        'css.Order_Overlay__3KW-T'
    )

    @staticmethod
    def rental_value(days):
        return f'xpath=//div[text()="{days}"]'

    @staticmethod
    def color_field(color):
        return f'//*[@id="{color}"]'

    COMMENT_FIELD = (
        "xpath=//input[@placeholder='Комментарий для курьера']"
    )
