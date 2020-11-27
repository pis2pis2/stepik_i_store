import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_choice_button(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    # time.sleep(30)
    choice_button = browser.find_elements_by_css_selector('form#add_to_basket_form button[type="submit"].btn')
    assert choice_button, "Button is not found"