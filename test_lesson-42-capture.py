from playwright.sync_api import Playwright, sync_playwright, expect, Page, Route
# def test_listen_network(page: Page):
#     page.on("request", lambda request: print(">>", request.method, request.url))
#     page.on("response", lambda response: print("<<", response.status, response.url))
#     page.goto('https://osinit.ru/')

# def test_network(page):
#     page.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}'))
#     page.goto('https://reqres.in/')
#     page.get_by_text(' Register - successful ').click()
#     # expect(page.locator('.response-code')).to_have_text('200')

# def test_mock_tags(page):
#     page.route("**/api/tags", lambda route: route.fulfill(path="data.json"))
#     page.goto('https://demo.realworld.io/')

# def test_intercepted(page: Page):
#     def handle_route(route: Route):
#         response = route.fetch()
#         json = response.json()
#         json["tags"] = ["open", "solutions"]
#         route.fulfill(json=json)
#
#     page.route("**/api/tags", handle_route)
#
#     page.goto("https://demo.realworld.io/")
#     sidebar = page.locator('css=div.sidebar')
#     expect(sidebar.get_by_role('link')).to_contain_text(["open", "solutions"])

# == HAR ==
# to create: playwright open --save-har=example.har --save-har-glob="**/api/**" https://reqres.in
# to open: F12 - tab Network - import HAR
# to use HAR file in test:  page.route_from_har("example.har")

# def test_replace_from_har(page):
#     page.goto("https://reqres.in/")
#     page.route_from_har("example.har")
#     users_single = page.locator('li[data-id="users-single"]')
#     users_single.click()
#     response = page.locator('[data-key="output-response"]')
#     expect(response).to_contain_text("Testing HAR file")

# == API ==
# GET: page.request.get()
# def test_inventory(page):
#     response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
#     print(response.status)
#     print(response.json())

# POST: page.request.post()
# to get response:  response.text(), response.json(), response.body()

def test_add_user(page):
    data = [
              {
                "id": 9743,
                "username": "fsd",
                "firstName": "fff",
                "lastName": "ggg",
                "email": "bbb",
                "password": "tt",
                "phone": "333",
                "userStatus": 0
              }
            ]
    header = {
        'accept': 'application/json',
        'content-Type': 'application/json'
    }
    response = page.request.post('https://petstore.swagger.io/v2/user/createWithArray',data=data, headers=header)
    resp = response.json()
    # expect(response).to_be_ok()
    # print(response.status)



