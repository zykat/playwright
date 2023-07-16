import pytest
pytest.fixture(scope="session")

# browser size
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1920,
            "height": 1080,
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