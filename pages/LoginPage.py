from playwright.sync_api import Page,expect

class LoginPage:
    def __init__(self,page :Page):
        self.page = page
        self.username_textbox = page.get_by_label("Username")
        self.password_textbox = page.get_by_label("Password")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.error_message = page.locator("#error")
        self.success_login_message = page.get_by_text("Congratulations student. You successfully logged in!")

    def login_click(self, username, password):
       self.username_textbox.fill("")
       self.username_textbox.fill(username)
       self.password_textbox.fill("")
       self.password_textbox.fill(password)
       self.submit_button.click()
