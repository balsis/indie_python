def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = f"Open Browser [{browser_name}]"
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = f"Go To Companyname Homepage [{page_url}]"
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = f"Find Registration Button On Login Page [{page_url}, {button_text}]"
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"