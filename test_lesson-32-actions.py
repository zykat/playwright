from playwright.sync_api import Playwright, sync_playwright, expect

# == 3.2 ====
# == locator.click(value, **kwargs)
# click(button='right')
# click(modifiers=["Shift"])
# def test_checkbox(page):
#     page.goto('https://zimaev.github.io/checks-radios/')
#     page.locator("text=Default checkbox").click()
#     page.locator("text=Checked checkbox").click()
#     page.locator("text=Default radio").click()
#     page.locator("text=Default checked radio").click()
#     page.locator("text=Checked switch checkbox input").click()

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

# = locator.check(**kwargs)
# def test_checkbox(page):
#     page.goto('https://zimaev.github.io/checks-radios/')
#     page.locator("text=Default checkbox").check()
#     page.locator("text=Checked checkbox").check()
#     page.locator("text=Default radio").check()
#     page.locator("text=Default checked radio").check()
#     page.locator("text=Checked switch checkbox input").check()

# = locator.select_option(**kwargs)
# index
# value
# label
# def test_select(page):
#     page.goto('https://zimaev.github.io/select/')
#     page.select_option('#floatingSelect', value="3")
#     page.select_option('#floatingSelect', index=1)
#     page.select_option('#floatingSelect', label="Нашел и завел bug")

# def test_select_multiple(page):
#     page.goto('https://zimaev.github.io/select/')
#     page.select_option('#skills', value=["Git", "Linux"])

# = page.drag_and_drop(source, target, **kwargs)
# def test_drag_and_drop(page):
#     page.goto('https://zimaev.github.io/draganddrop/')
#     page.drag_and_drop("#drag", "#drop")

# = dialog-windows (alert, confirm, promt)
# from playwright.sync_api import Page
# dialog.accept() - OK
# dialog.dismiss() - Cancel (default)
# dialog.accept('value') - input value for prompt dialog
# def test_dialogs(page: Page):
#     page.goto("https://zimaev.github.io/dialog/")
#     page.get_by_text("Диалог Alert").click()
#     page.on("dialog", lambda dialog: dialog.accept())
#     page.get_by_text("Диалог Confirmation").click()
#     page.get_by_text("Диалог Prompt").click()

# = upload file =
# def test_select_multiple(page):
#     page.goto('https://zimaev.github.io/upload/')
#     page.set_input_files("#formFile", "hello.txt")
#     page.locator("#file-submit").click()

# def test_select_multiple(page):
#     page.goto('https://zimaev.github.io/upload/')
#     page.on("filechooser", lambda file_chooser: file_chooser.set_files("hello.txt"))
#     page.locator("#formFile").click()

# def test_select_multiple(page):
#     page.goto('https://zimaev.github.io/upload/')
#     with page.expect_file_chooser() as fc_info:
#         page.locator("#formFile").click()
#     file_chooser = fc_info.value
#     file_chooser.set_files("hello.txt")

# = download file =
from playwright.sync_api import sync_playwright, expect
import os

# def test_download(page):
#     page.goto("https://demoqa.com/upload-download")
#
#     with page.expect_download() as download_info:
#         #page.get_by_role("link", name="Download").click()
#         #page.get_by_role("button", name="Download").click()
#         #page.locator("a:has-text(\"Download\")").click()
#         page.locator("a#downloadButton").click()
#         #page.locator("text=Download").click()
#
#     download = download_info.value
#     file_name = download.suggested_filename
#     destination_folder_path = "data"
#     download.save_as(os.path.join(destination_folder_path, file_name))

# = getting element values =
# element.inner_text()
# element.text_content()

# = creating screenshot =
# page.screenshot(path="screenshot.png", full_page=True)
# page.locator(".header").screenshot(path="screenshot.png")
# page.screenshot(path="example.jpeg", type="jpeg")
# page.screenshot(path="example.jpeg", type="jpeg", quality=80)
# page.screenshot(path="clipped_image.png", clip={"x": 50, "y": 0, "width": 400, "height": 300})

# = switching tabs =
# def test_new_tab(page):
#     page.goto("https://zimaev.github.io/tabs/")
#     with page.context.expect_page() as tab:
#         page.get_by_text("Переход к Dashboard").click()
#
#     new_tab = tab.value
#     assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
#     sign_out = new_tab.locator('.nav-link', has_text='Sign out')
#     assert sign_out.is_visible()

# def test_download(page):
#     page.goto("https://demoqa.com/upload-download")
#     download = page.locator("a:has-text(\"Download\")")
#     assert download.is_visible()

