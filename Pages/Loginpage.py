from Pages.Basepage import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):

    username="//input[@name='username']"
    password="//input[@name='password']"
    loginBtn="//button[@type='submit']"
    error="//p[contains(@class,'alert')]"
    profile="//span[@class='oxd-userdropdown-tab']"
    logout="//a[text()='Logout']"

    def login_field(self,page):
        expect(self.page.locator(self.username)).to_be_visible()
        expect(self.page.locator(self.password)).to_be_visible()


    def login(self,user,pwd):

        self.wait(self.username)

        self.fill(self.username,user)
        self.fill(self.password,pwd)

        self.click(self.loginBtn)

    def logout_user(self):

        self.click(self.profile)

        self.click(self.logout)


