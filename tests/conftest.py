import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='class', params=['firefox', 'msedge', 'opera'])
def page(request):
    with sync_playwright() as p:
        launch_options = {
            'headless': False
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
