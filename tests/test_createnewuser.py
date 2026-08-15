#Test-Case-5: Scenario: Create a new user and validate login
from Pages.Basepage import BasePage
from Pages.Dashboardpage import DashboardPage
from Pages.ForgotPasswordPage import ForgotPasswordPage
from Pages.Loginpage import LoginPage
from Pages.Adminpage import AdminPage
import time

username = f"test_G12"
def test_create_newuser(page):

    login = LoginPage(page)
    admin = AdminPage(page)
    dashboard = DashboardPage(page)

    login.login("Admin", "admin123")
    print("login success")
    dashboard.open_admin()
    print("Navigated to admin page")

    #employee_name = dashboard.getusername(page)

    admin.create_user(
        emp_name="Ravi M B ",
        username=username,
        password="Test@12345"
    )

    login.logout_user()

    # Test-Case-6: Scenario: Validate presence of the newly created user in the admin user list
    login.login(username, "Test@12345")

    assert "dashboard" in page.url.lower()
    dashboard.open_admin()

    admin.search_user(username)
    print("username")
    assert admin.is_user_present(username)
    print("username is present")

#Test-Case-7: Scenario: Verify "Forgot Password" link functionality
def test_forgot_password(page):

    forgot_pswd = ForgotPasswordPage(page)
    forgot_pswd.verify_forgot_password(username)
    forgot_pswd.verify_reset_password_success_page()
    print("Test Passed")






