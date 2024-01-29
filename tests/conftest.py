import pytest
from playwright.sync_api import sync_playwright

from config import BaseUrl
from constans import USER_LOGIN, USER_PASSWORD
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture()
def f_main_page():
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute('data-ftid')
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BaseUrl.BASE_URL)
        main_page = MainPage(page)
        yield main_page
        context.close()
        browser.close()


@pytest.fixture()
def f_login_user(f_main_page: MainPage) -> MainPage:
    f_main_page.click_login_button()
    login_page = LoginPage(f_main_page.page)
    login_page.fill_login(USER_LOGIN)
    login_page.fill_password(USER_PASSWORD)
    login_page.click_enter_button()
    yield f_main_page
