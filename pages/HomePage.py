from playwright.sync_api import sync_playwright, Playwright, Page, expect

class HomePage:

    def __init__(self, page:Page):
        self.page = page
        self.login_link = page.get_by_role("link", name="Test Login Page")
        self.test_exceptions = page.locator("//a[contains(text(), 'Test Exceptions']")


    def navigate(self):
        self.page.goto("https://practicetestautomation.com/practice/")


    def enter_login_test(self):
        self.login_link.click()


    def enter_test_exceptions(self):
        self.test_exceptions.click()









