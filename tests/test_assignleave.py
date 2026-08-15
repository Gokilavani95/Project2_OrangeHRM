from Pages.Leavepage import LeavePage
from Pages.Loginpage import LoginPage
from Pages.Dashboardpage import DashboardPage

#Test case:9-Assign leave to an employee and verify assignment
def test_assign_leave(page):


     login = LoginPage(page)
     dashboard = DashboardPage(page)
     start_date = "2026-10-20"
     end_date = "2026-10-21"
     leave_type = "CAN - Personal"
     login.login(
         "Admin",
         "admin123"

     )

     employee_name = dashboard.getusername(page)

     leave = LeavePage(page)

     leave.open_assign_leave()

     leave.assign_leave_to_employee(
         employee=employee_name,
         leave_type=leave_type
     )

     leave.assign_leave_date(
         start_date=start_date,
         end_date=end_date
     )

     #leave.verify_success_message()
     leave.navigate_myleave()

     records = leave.get_leave_records()
     print(records)

     leave.verify_assigned_leave_date(
         start_date=start_date,
         end_date=end_date
     )

