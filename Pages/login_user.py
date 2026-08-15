from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):

        self.page = page

        self.username_input = page.locator(
            "input[name='username']"
        )

        self.password_input = page.locator(
            "input[name='password']"
        )

        self.login_button = page.locator(
            "button[type='submit']"
        )

        self.error_message = page.locator(
            "p.oxd-alert-content-text"
        )

    def navigate(self):

        self.page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
            wait_until="domcontentloaded"
        )

        self.username_input.wait_for(
            state="visible"
        )

    def login(self, username, password):

        print(f"\nUsername: [{username}]")
        print(f"Password: [{password}]")

        self.username_input.fill(
            str(username).strip()
        )

        self.password_input.fill(
            str(password).strip()
        )

        self.login_button.click()

    def is_login_successful(self):

        try:

            self.page.wait_for_url(
                "**/web/index.php/dashboard/index",
                timeout=10000
            )

            return True

        except:

            return False

    def get_error_message(self):

        try:

            self.error_message.wait_for(
                state="visible",
                timeout=3000
            )

            return self.error_message.inner_text()

        except:

            return ""