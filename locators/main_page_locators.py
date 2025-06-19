class MainPageLocators:

    ORDER_BUTTON_IN_HEADER = (
        "xpath=//button[@class='Button_Button__ra12g' and text()='Заказать']"
    )

    ORDER_BUTTON = (
        'css=.Button_Button__ra12g.Button_Middle__1CSJM'
    )

    SAMOKAT_LOGO = (
        'css=.Header_LogoScooter__3lsAR'
    )

    YANDEX_LOGO = (
            'css=.Header_LogoYandex__3TSOI'
    )

    @staticmethod
    def question(number):
        return f'//*[@id="accordion__heading-{number}"]'

    @staticmethod
    def answer(number):
        return f'xpath=//div[@id="accordion__panel-{number}"]/p'
