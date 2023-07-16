# def test_loc(page):
#     page.goto('https://textinput.antonzimaiev.repl.co/?')
#     page.get_by_label("Email address").fill("qa@example.com")
#     page.get_by_title("username").fill("Anton")
#     page.get_by_placeholder('password').fill("secret")
#     page.get_by_role('checkbox').click()

# def test_nav(page):
#     page.goto('https://navbar.antonzimaiev.repl.co/#')
#     # page.locator("#navbarNavDropdown >> li:has-text('Company')").click()
#     # nav_bar = page.locator('div#navbarNavDropdown')
#     # nav_bar.locator("li:has-text('Products')").click()
#     # page.locator("li").filter(has_text='Company').click()
#     page.locator('li').filter(has=page.locator('.dropdown-toggle')).click()

# == locator.count(), locator.first, locator.last или locator.nth(index)

def test_checkbox_cycle(page):
    page.goto('https://checks-radios.antonzimaiev.repl.co/')
    # checkbox = page.locator("input")
    # for i in range(checkbox.count()):
    #     checkbox.nth(3).click()
    checkboxes = page.locator("input")
    for checkbox in checkboxes.all():
        checkbox.check()
