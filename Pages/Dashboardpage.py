from Pages.Basepage import BasePage
from playwright.sync_api import Page,expect

class DashboardPage(BasePage):
    admin_menu = "//span[text()='Admin']"
    menus=[
        "Admin",
        "PIM",
        "Leave",
        "Time",
        "Recruitment",
        "My Info",
        "Performance",
        "Dashboard"
    ]
    def __init__(self,page):
        self.page = page
        self.leave_menu = page.get_by_role(
            "link",
            name="Leave",
            exact=True
        )

        self.assign_leave = page.get_by_text(
            "Assign Leave",
            exact=True
        )

    def verify_menu(self):

        for menu in self.menus:

            self.page.locator(f"text={menu}").wait_for()

            assert self.page.locator(f"text={menu}").is_visible()

            self.page.locator(f"text={menu}").click()

    def open_admin(self):
        self.click(self.admin_menu)
        self.page.wait_for_url("**/admin/viewSystemUsers")

    def getusername(self,page):
        self.profile_menu = page.locator(".oxd-userdropdown-tab")
        self.username_text = page.locator(".oxd-userdropdown-name")
        username = self.username_text.text_content()
        return username.strip() if username else ""

    def open_leave(self):
        self.leave_menu.click()

        self.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList")


