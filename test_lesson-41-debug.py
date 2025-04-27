# == playwright inspector with debug ==
# pycharm env - set PWDEBUG=1 - Apply
# run test

# == playwright inspector browser and debug==
# pycharm env - set PWDEBUG=console - Apply
# page.pause() in code
# run test
# F12 - console:
# playwright.$(selector): first appearance
# playwright.$$(selector): all appearances
# eg from lesson-33. playwright.$$('[data-testid="todo-title"]')
# playwright.inspect(selector):  to display selector in DOM
# playwright.generateLocator($0): choose element and generzte locator

# == log API Playwright ==
# pycharm env - set DEBUG=pw:api - Apply

# == trace viewer playwright ==
# CLI --tracing on / retain-on-failure
# eg. test from lesson-33.py
#     pytest --tracing=retain-on-failure .\test_lesson-33-assert.py
#     playwright show-trace .\test-results\test-lesson-33-assert-py-test-todo-chromium\trace.zip







