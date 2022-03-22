import pytest
import time

from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage


book_95_url = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
book_207_url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_207/"
book_209_url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"


@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer',
                         [pytest.param(i, marks=pytest.mark.xfail(i=7, reason="already known bug")) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message_after_add_product_to_basket()


@pytest.mark.xfail(reason="negative test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = book_207_url
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = book_207_url
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="negative test")
def test_success_message_disappeared_after_adding_product_to_basket(browser):
    link = book_207_url
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = book_95_url
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = book_95_url
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = book_95_url
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()

        email = str(time.time()) + "@fakemail.org"
        password = "qwe123456rty"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = book_209_url
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = book_209_url
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_success_message_after_add_product_to_basket()
