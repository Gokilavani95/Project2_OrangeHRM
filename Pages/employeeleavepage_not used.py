class EmployeeLeavePage:

    def __init__(self, page):
        self.page = page


        self.my_leave_menu = page.get_by_text(
            "My Leave",
            exact=True
        )


        self.records_table = page.locator(
            ".oxd-table"
        )


    def open_my_leave(self):

        self.my_leave_menu.click()

        self.page.wait_for_load_state(
            "networkidle"
        )


    def verify_leave_record(self, leave_type):

        return self.page.get_by_text(
            leave_type,
            exact=True
        ).is_visible()