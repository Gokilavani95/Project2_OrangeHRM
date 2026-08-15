import suggestion

from Pages.Basepage import BasePage
from playwright.sync_api import Page,expect

class AdminPage(BasePage):

    add_btn = "//button[normalize-space()='Add']"

    user_role = "(//div[contains(@class,'oxd-select-text')])[1]"
    employee_name = "//input[@placeholder='Type for hints...']"
    status = "(//div[contains(@class,'oxd-select-text')])[4]"
    username = "(//input[@class='oxd-input oxd-input--active'])[2]"
    password = "(//input[@type='password'])[1]"
    confirm_password = "(//input[@type='password'])[2]"

    save_btn = "//button[@type='submit']"
    success = "//p[contains(text(),'Successfully')]"
    search_username = "(//input[@class='oxd-input oxd-input--active'])[2]"
    search_btn = "button:has-text('Search')"

    def create_user(self, emp_name, username, password):

        self.click(self.add_btn)

        self.page.wait_for_url("**/admin/saveSystemUser")

        # User Role
        self.click(self.user_role)
        self.page.get_by_role("option", name="Admin").click()

        # Employee
        self.fill(self.employee_name, emp_name)

        employee_suggestion = self.page.get_by_text(emp_name.strip(), exact=False).first
        employee_suggestion.wait_for()
        employee_suggestion.click()
        actual = self.page.locator(self.employee_name).input_value()

        assert " ".join(actual.split()) == " ".join(emp_name.split())

        self.click(self.status)
        self.page.get_by_role("option", name="Enabled").click()

        # Credentials
        self.fill(self.username, username)
        self.fill(self.password, password)
        self.fill(self.confirm_password, password)

        self.click(self.save_btn)

        self.page.wait_for_url("**/admin/viewSystemUsers")

    def search_user(self,username):
        self.page.fill(self.search_username, username)
        self.page.click(self.search_btn)
        self.page.wait_for_load_state("networkidle")

    def is_user_present(self, username):
        rows = self.page.locator(".oxd-table-body .oxd-table-row")
        return rows.filter(has_text=username).count() > 0





