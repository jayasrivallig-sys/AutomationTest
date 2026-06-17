from playwright.sync_api import Page, Playwright, expect
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.ExceptionPage import ExceptionPage


def test_exception(page:Page):
    homepage = HomePage(page)
    homepage.navigate()

    expectionpage = ExceptionPage(page)
    expectionpage.navigate()
    expectionpage.click_add_button()

