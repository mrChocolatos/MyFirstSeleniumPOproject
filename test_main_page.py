import pytest
from Pages.main_page import MainPage
from Pages.login_page import LoginPage
from Pages.basket_page import BasketPage

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_form_login1(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

@pytest.mark.skip
def test_form_login2(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

@pytest.mark.skip
def test_form_login3(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket = BasketPage(browser, link)
    basket.agree_that_basket_is_empty()
    basket.check_basket_is_empty_negative()
