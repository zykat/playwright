from playwright.sync_api import Playwright, sync_playwright, expect

# def test_add_todo(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://demo.playwright.dev/todomvc/#/")
#     page.get_by_placeholder("What needs to be done?").click()
#     page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
#     page.get_by_placeholder("What needs to be done?").press("Enter")
#     page.get_by_role("checkbox", name="Toggle Todo").check()
#     # ---------------------
#     context.close()
#     browser.close()


def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter", delay=3000)

