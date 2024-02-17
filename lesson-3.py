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
# def test_loc(page):
#     page.goto('https://textinput.antonzimaiev.repl.co/?')
#     page.get_by_label("Email address").fill("qa@example.com")
#     page.get_by_title("username").fill("Anton")
#     page.get_by_placeholder('password').fill("secret")
#     page.get_by_role('checkbox').click()


# = Locator locator.or_
# def test_or(page):
#     selector = page.locator("input").or_(page.locator("text"))
#     selector.fill("Hello Stepik")

# = Locator locator.and_
# def test_locator_and(page):
#     page.goto("https://locatorand.antonzimaiev.repl.co/")
#     selector = page.get_by_role("button", name="Sing up").and_(page.get_by_title("Sing up today"))
#     selector.click()


# def test_nav(page):
#     page.goto('https://navbar.antonzimaiev.repl.co/#')
#     # page.locator("#navbarNavDropdown >> li:has-text('Company')").click()
#     # nav_bar = page.locator('div#navbarNavDropdown')
#     # nav_bar.locator("li:has-text('Products')").click()
#     # page.locator("li").filter(has_text='Company').click()
#     page.locator('li').filter(has=page.locator('.dropdown-toggle')).click()

# == locator.count(), locator.first, locator.last или locator.nth(index)

# def test_checkbox_cycle(page):
#     page.goto('https://checks-radios.antonzimaiev.repl.co/')
#     # checkbox = page.locator("input")
#     # for i in range(checkbox.count()):
#     #     checkbox.nth(3).click()
#     checkboxes = page.locator("input")
#     for checkbox in checkboxes.all():
#         checkbox.check()

# == locator.fill(value, **kwargs)
# def test_login(page):
#     page.goto('https://exaltedplushadware.antonzimaiev.repl.co/?')
#     page.locator("#exampleInputEmail1").fill("admin@example.com")

# = locator.type(text, **kwargs)
# def test_login(page):
#     page.goto('https://exaltedplushadware.antonzimaiev.repl.co/?')
#     page.locator("#exampleInputEmail1").type("admin@example.com")

# = locator.press(key, **kwargs)
# Keys:  (F1 - F12, Backspace, Tab, Delete, Escape, ArrowDown,
# End, Enter, Home, Insert, PageDown, PageUp, ArrowRight, ArrowUp..

