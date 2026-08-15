from Pages.Basepage import BasePage
from playwright.sync_api import Page, expect

class ForgotPasswordPage(BasePage):

    # Locators
    heading = "h6.oxd-text.oxd-text--h6.orangehrm-forgot-password-title"
    message = ".orangehrm-forgot-password-wrapper p"
    message_line2 = "//p[2]//p[1]"
    note = "//p[@class='oxd-text oxd-text--p orangehrm-sub-title']"
    note_msg = "//p[@class='oxd-text oxd-text--p orangehrm-card-note orangehrm-card-note--background orangehrm-forgot-password-card-note']//p[@class='oxd-text oxd-text--p']"
    forgot_link = "//p[contains(@class,'orangehrm-login-forgot-header')]"
    user_name = "input[name='username']"
    Reset_pswd_butn = "button[type='submit']"

    def verify_forgot_password(self,username):
        self.page.locator(self.forgot_link).click()
        self.page.locator(self.user_name).fill(username)
        self.page.locator(self.Reset_pswd_butn).click()

    def verify_reset_password_success_page(self):

        # Heading
        expect(self.page.locator(self.heading)).to_have_text(
            "Reset Password link sent successfully"
        )

        # Paragraphs
        expect(self.page.locator(self.message).nth(0)).to_have_text(
            "A reset password link has been sent to you via email."
        )

        expect(self.page.locator(self.message_line2)).to_have_text(
            "You can follow that link and select a new password."
        )

        #Note section (contains both title and message)
        expect(self.page.locator(self.note)).to_contain_text(
            "Note:"
        )

        expect(self.page.locator(self.note_msg)).to_contain_text(
            "If the email does not arrive, please contact your OrangeHRM Administrator."
        )