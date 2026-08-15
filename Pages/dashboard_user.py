from playwright.sync_api import Page


class DashboardPage:

    def __init__(self, page: Page):

        self.page = page

        self.user_dropdown = page.locator(
            "span.oxd-userdropdown-tab"
        )

        self.logout_link = page.get_by_text(
            "Logout",
            exact=True
        )

    def is_dashboard_displayed(self):

        return "dashboard/index" in self.page.url

    def logout(self):

        self.user_dropdown.click()

        self.logout_link.click()

        self.page.wait_for_url(
            "**/web/index.php/auth/login",
            timeout=10000
        )