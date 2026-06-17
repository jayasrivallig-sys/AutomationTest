from playwright.sync_api import Page, Playwright

class ExceptionPage:
    def __init__(self, page):
        self.page = page
        self.button_add = page.get_by_role("button", name="Add")
        self.button_edit = page.get_by_role("button", name="Edit")
        self.textbox_edit = page.get_by_role("textbox")
        self.button_save = page.get_by_role("button", name="Save")
        self.save_success_message = page.get_by_text("Row 1 was saved", exact=True)
        self.add_new_row_message = page.get_by_text("Row 2 was added", exact=True)
        self.new_row_textbox = page.locator("//div[@id='row2']//input[@type='text']")
        self.button_edit2= page.locator("#edit_btn:visible")
        self.button_remove = page.get_by_role("button", name="Remove")
        self.remove_success_message = page.get_by_text("Row 2 was removed", exact=True)
        self.textbox_message = page.locator("//input[@value='Pizza']")


    def click_add_button(self):
        self.button_add.click()

    def navigate(self):
        self.page.goto("https://practicetestautomation.com/practice-test-exceptions/")


    def click_edit_button(self):
        self.textbox_edit.click()


    def clear_text(self):
        self.textbox_message.clear()


    def click_save_button(self):
        self.button_save.click()




