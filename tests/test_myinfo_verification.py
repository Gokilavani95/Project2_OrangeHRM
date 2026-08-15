from Pages.Dashboardpage import DashboardPage
from Pages.Myinfopage import MyInfoPage
from Pages.Loginpage import LoginPage
#Test-Case-8: Scenario: Validate the presence of menu items under “My Info”
def test_myinfo(page):
    dashboard = DashboardPage(page)
    login = LoginPage(page)
    myinfo = MyInfoPage(page)
    login.login("Admin","admin123")
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("networkidle")

    myinfo.verify_items()
    print("My info sub-menu's are visible and clickable")