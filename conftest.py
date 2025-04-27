import pytest

pytest.fixture(scope="session")

# browser size
def browser_context_args(browser_context_args):
    return {
        "viewport": {
            "width": 1920,
            "height": 1080
        }
    }
# browser cookie
# def browser_context_args(browser_context_args):
#     response = authenticate(user)
#     return {
#         **browser_context_args
#         "storage_state": {
#             "cookies": [
#                 {
#                     "name": "token",
#                     "value": "sd4fFfv!x_cfc",
#                 },
#             ]
#         },
#     }

# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(channel="chromium",executable_path="путь до яндекс браузера", headless=False)
#         yield browser
#         browser.close()
#
# def test_yandex(browser):
#     page = browser.new_page()
#     page.goto("https://ya.ru/")

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)