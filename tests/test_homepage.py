from playwright.sync_api import sync_playwright, expect, Page
from pages.HomePage import HomePage

def test_homepage(page:Page):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.enter_login_test()

    expect(page).to_have_url("https://practicetestautomation.com/practice-test-login/", timeout=3000)

    #
    #
    # expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    # expect(page.get_by_text("Congratulations student. You successfully logged in!")).to_be_visible()
    # logout_button = page.get_by_role("link", name="Log out").click()


