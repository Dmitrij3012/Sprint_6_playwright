import pytest
from playwright.sync_api import sync_playwright
from generators import fake_agent


# @pytest.fixture(scope='class', params=['firefox', 'msedge', 'opera'])
# def page(request):
#     with sync_playwright() as p:
#         if request.param == 'firefox':
#             browser = p.firefox.launch(headless=False,
#                                        firefox_user_prefs={
#                                            "dom.webdriver.enabled": False,
#                                            "useAutomationExtension": False
#                                        })
#             page = browser.new_page()
#             yield page
#             browser.close()
#         elif request.param == 'msedge':
#             browser = p.chromium.launch(headless=False, channel='msedge',
#                                         args=['--disable-blink-features=AutomationControlled'])
#             page = browser.new_page()
#             yield page
#             browser.close()
#         elif request.param == 'opera':
#             browser = p.chromium.launch(headless=False,
#                                         executable_path='C:/Users/paran/AppData/Local/Programs/Opera/opera.exe',
#                                         args=['--disable-blink-features=AutomationControlled'])
#             page = browser.new_page()
#             yield page
#             browser.close()


# @pytest.fixture(scope='class', params=['firefox', 'msedge', 'opera'])
# def page(request):
#     with sync_playwright() as p:
#         if request.param == 'firefox':
#             browser = p.firefox.launch(headless=False,
#                                        firefox_user_prefs={
#                                            "dom.webdriver.enabled": False,
#                                            "useAutomationExtension": False
#                                        }
#                                        )
#             page = browser.new_page(bypass_csp=True,
#                                     user_agent=fake_agent())
#             yield page
#             browser.close()
#         elif request.param == 'msedge':
#             browser = p.chromium.launch(headless=False, channel='msedge',
#                                         args=['--disable-blink-features=AutomationControlled'])
#             page = browser.new_page(bypass_csp=True,
#                                     user_agent=fake_agent())
#             yield page
#             browser.close()
#         elif request.param == 'opera':
#             browser = p.chromium.launch(headless=False,
#                                         executable_path='C:/Users/paran/AppData/Local/Programs/Opera/opera.exe',
#                                         args=['--disable-blink-features=AutomationControlled'])
#             page = browser.new_page(bypass_csp=True,
#                                     user_agent=fake_agent())
#             yield page
#             browser.close()

# @pytest.fixture(scope='class', params=['firefox', 'msedge', 'opera'])
# def page(request):
#     with sync_playwright() as p:
#         launch_options = {
#             'headless': False,
#             # 'args': [
#             #     '--disable-blink-features=AutomationControlled',
#             # ]
#         }
#
#         if request.param == 'firefox':
#             browser = p.firefox.launch(**launch_options)
#
#         elif request.param == 'msedge':
#             browser = p.chromium.launch(**launch_options)
#
#         elif request.param == 'opera':
#             browser = p.chromium.launch(**launch_options)
#
#         new_page = browser.new_page()
#         yield new_page
#         browser.close()

def page(request):
    with sync_playwright() as p:
        launch_options = {
            'headless': False,
            # 'args': [
            #     '--disable-blink-features=AutomationControlled',
            # ]
        }

        if request.param == 'firefox':
            browser = p.firefox.launch(**launch_options)

        elif request.param == 'msedge':
            browser = p.chromium.launch(**launch_options)

        elif request.param == 'opera':
            browser = p.chromium.launch(**launch_options)

        new_page = browser.new_page()
        yield new_page
        browser.close()
