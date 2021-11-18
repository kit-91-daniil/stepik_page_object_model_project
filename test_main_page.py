from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    assert True


def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
    assert True


def test_guest_should_see_login_link(browser):
    login_link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, login_link)
    page.open()
    page.should_be_login_link()
