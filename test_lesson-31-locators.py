# = Locators get_by_*
# page.get_by_text(text,**kwargs)
# - page.get_by_text("switch checkbox").click()
# page.get_by_label(text, **kwargs)
# - page.get_by_label("Email address").fill("qa@example.com")
# page.get_by_placeholder(text, **kwargs)
# - page.get_by_placeholder("password")
# page.get_by_test_id(test_id)
# - page.get_by_test_id('todo-title').click()
# page.get_by_alt_text(text, **kwargs)
# - page.get_by_alt_text('logo').click()
# page.get_by_title(text, **kwargs)
# - page.get_by_title("username").fill("Anton")
# page.get_by_role(role, **kwargs)
# - page.get_by_role("button", name="Submit").click()
#

from playwright.sync_api import Playwright, sync_playwright, expect

# == 3.1 ====
# def test_loc(page):
#     page.goto('https://zimaev.github.io/text_input/')
#     page.get_by_label("Email address").fill("qa@example.com")
#     page.get_by_title("username").fill("Anton")
#     page.get_by_placeholder('password').fill("secret")
#     page.get_by_role('checkbox').click(delay=2000)
#
# = Locator locator.or_
# def test_or(page):
#     selector = page.locator("input").or_(page.locator("text"))
#     selector.fill("Hello Stepik")

# = Locator locator.and_
# def test_locator_and(page):
#     page.goto("https://zimaev.github.io/locatorand/")
#     selector = page.get_by_role("button", name="Sing up").and_(page.get_by_title("Sing up today"))
#     selector.click()


# def test_nav(page):
#    page.goto('https://zimaev.github.io/navbar/')
#    page.locator("#navbarNavDropdown >> li:has-text('Company')").click()
#
#    nav_bar = page.locator('div#navbarNavDropdown')
#    nav_bar.locator("li:has-text('Products')").click()
#
#    page.locator("li").filter(has_text='Company').click(delay=3000)
#
#    page.locator('li').filter(has=page.locator('.dropdown-toggle')).click()
#
#     page.goto("https://zimaev.github.io/filter/")
#     row_locator = page.locator('tr')
#     row_locator.filter(has_text='helicopter').click()
#     row_locator.filter(has=page.get_by_role("button", name="Edit")).click()

# == locator.count(), locator.first, locator.last или locator.nth(index)

# def test_checkbox_cycle(page):
#     page.goto('https://zimaev.github.io/checks-radios/')
#     checkbox = page.locator("input")
#     for i in range(checkbox.count()):
#         checkbox.nth(i).click()
#
#     checkboxes = page.locator("input")
#     for checkbox in checkboxes.all():
#         checkbox.check()


