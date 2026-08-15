#Test-Case-3:Scenario: Validate presence of login fields


from Pages.Dashboardpage import DashboardPage
from Pages.Loginpage import LoginPage
def test_home(page):
    field = LoginPage(page)
    field.login_field(page)
    print("Login fields are visible")

#Test-Case-4:Scenario: Verify visibility and clickability of main menu items after login
def test_mainmenu_visibility(page):
    obj = LoginPage(page)
    obj1 = DashboardPage(page)
    obj.login("Admin","admin123")
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    obj1.verify_menu
    print("Application menu is visible")




