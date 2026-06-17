from playwright.sync_api import Page, expect
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from config import Config


def test_login_valid(page):
    homepage = HomePage(page)
    login_page = LoginPage(page)

    homepage.navigate()
    homepage.enter_login_test()

    login_page.login_click(Config.valid_username, Config.valid_password)

    expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/",timeout=3000)
    expect(login_page.success_login_message).to_be_visible(timeout=3000)


def test_login_invalid(page):
    homepage = HomePage(page)
    login_page = LoginPage(page)

    homepage.navigate()
    homepage.enter_login_test()

    login_page.login_click(Config.invalid_username, Config.invalid_password)

    expect(login_page.error_message).to_be_visible(timeout=2000)
    expect(login_page.error_message).to_contain_text("Your username is invalid!", timeout=2000)

