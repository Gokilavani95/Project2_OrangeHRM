from datetime import datetime
from playwright.sync_api import Page, expect, TimeoutError


class LeavePage:

    def __init__(self, page: Page):
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

        self.employee_name = page.locator(
            "input[placeholder='Type for hints...']"
        )

        self.leave_type = page.locator(
            ".oxd-select-text"
        )

        self.from_date = page.locator(
            ".oxd-date-input input"
        ).nth(0)

        self.to_date = page.locator(
            ".oxd-date-input input"
        ).nth(1)

        self.assign_button = page.get_by_role(
            "button",
            name="Assign"
        )

        self.my_leave = page.get_by_role(
            "link",
            name="My Leave"
        )

        self.success_message = page.locator(
            "//div[contains(@class,'oxd-toast')]"
            "//p[contains(@class,'oxd-text--toast-message')]"
        )

        self.confirmation = page.locator(
            "//button[normalize-space()='Ok']"
        )


    # OPEN ASSIGN LEAVE

    def open_assign_leave(self):

        self.leave_menu.click()

        self.assign_leave.click()

        expect(
            self.assign_button
        ).to_be_visible(
            timeout=10000
        )


    # SELECT EMPLOYEE AND LEAVE TYPE

    def assign_leave_to_employee(
        self,
        employee,
        leave_type
    ):

        # Employee autocomplete
        self.employee_name.fill(employee)

        # Wait for autocomplete result
        self.page.wait_for_timeout(2000)

        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        # Select leave type
        self.leave_type.click()

        self.page.get_by_text(
            leave_type,
            exact=True
        ).click()

        # Wait until leave balance is loaded
        balance = self.page.locator(
            ".orangehrm-leave-balance-text"
        )

        expect(
            balance
        ).to_be_visible(
            timeout=10000
        )

        print(
            "Leave balance:",
            balance.inner_text()
        )


    # SET DATE

    def set_leave_date(
        self,
        locator,
        iso_date
    ):


        date_obj = datetime.strptime(
            iso_date,
            "%Y-%m-%d"
        )

        year = date_obj.strftime("%Y")
        month = date_obj.strftime("%m")
        day = date_obj.strftime("%d")

        print(
            f"Setting date: {year}-{month}-{day}"
        )

        ui_date = f"{year}-{day}-{month}"

        print(
            "OrangeHRM UI date:",
            ui_date
        )

        # Click the date input
        locator.click()

        # Fill date
        locator.fill(ui_date)

        # Trigger Angular/OrangeHRM change detection
        locator.press("Tab")

        print(
            "UI date value:",
            locator.input_value()
        )

    # ASSIGN LEAVE DATE

    def assign_leave_date(
        self,
        start_date,
        end_date
    ):

        self.set_leave_date(
            self.from_date,
            start_date
        )

        self.set_leave_date(
            self.to_date,
            end_date
        )

        # Check what OrangeHRM actually displays
        print(
            "FROM UI:",
            self.from_date.input_value()
        )

        print(
            "TO UI:",
            self.to_date.input_value()
        )

        # Submit
        self.assign_button.click()

        # Optional confirmation
        #self.confirmation.click()


    # VERIFY SUCCESS MESSAGE
    def verify_success_message(self):

        expect(
            self.success_message
        ).to_be_visible(
            timeout=1000
        )

        message = (
            self.success_message
            .inner_text()
            .strip()
        )

        print(
            "Submit Success Message:",
            message
        )

        expect(
            self.success_message
        ).to_contain_text(
            "Successfully Saved"
        )

        return message

    # NAVIGATE TO MY LEAVE
    def navigate_myleave(self):

        self.my_leave.click()

        expect(
            self.page
        ).to_have_url(
            "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewMyLeaveList",
            timeout=10000
        )

        print(
            "My Leave Page"
        )

    # GET COMPLETE LEAVE RECORDS
    def get_leave_records(self):

        rows = self.page.locator(
            ".oxd-table-body .oxd-table-row"
        )

        expect(
            rows.first
        ).to_be_visible(
            timeout=15000
        )

        # Get table headers
        headers = self.page.locator(
            ".oxd-table-header .oxd-table-cell"
        )

        header_count = headers.count()

        header_names = []

        for i in range(header_count):

            header_text = (
                headers.nth(i)
                .inner_text()
                .strip()
            )

            header_text = " ".join(
                header_text.split()
            )

            header_names.append(
                header_text
            )

        # Get all records

        records = []

        row_count = rows.count()

        print(
            f"\nNumber of leave rows: {row_count}"
        )

        for i in range(row_count):

            row = rows.nth(i)

            cells = row.locator(
                ".oxd-table-cell"
            )

            cell_count = cells.count()

            values = []

            for j in range(cell_count):

                value = (
                    cells.nth(j)
                    .inner_text()
                    .strip()
                )

                value = " ".join(
                    value.split()
                )

                values.append(
                    value
                )

            # Map header -> cell value

            record = {}

            for j in range(
                min(
                    len(header_names),
                    len(values)
                )
            ):

                header = header_names[j]

                if not header:
                    continue

                record[header] = values[j]

            records.append(
                record
            )

        print(
            "\nLEAVE RECORDS:"
        )

        for record in records:
            print(
                record
            )

        return records

    # NORMALIZE A SINGLE DATE

    def normalize_date(
        self,
        date_text
    ):


        date_text = date_text.strip()


        # First try standard ISO format
        try:

            date_obj = datetime.strptime(
                date_text,
                "%Y-%m-%d"
            )

            return date_obj.strftime(
                "%Y-%m-%d"
            )

        except ValueError:
            pass


        # try OrangeHRM format
        # YYYY-DD-MM
        try:

            parts = date_text.split("-")

            if len(parts) != 3:
                return date_text

            year = parts[0]
            day = parts[1]
            month = parts[2]

            date_obj = datetime.strptime(
                f"{year}-{month}-{day}",
                "%Y-%m-%d"
            )

            return date_obj.strftime(
                "%Y-%m-%d"
            )

        except ValueError:

            print(
                f"WARNING: Unable to normalize date: "
                f"{date_text}"
            )

            return date_text

    # GET DATE RECORDS

    def get_date_records(self):

        rows = self.page.locator(
            ".oxd-table-body .oxd-table-row"
        )

        expect(
            rows.first
        ).to_be_visible(
            timeout=15000
        )

        row_count = rows.count()

        date_records = []

        print(
            "\nNumber of leave rows:",
            row_count
        )

        for i in range(row_count):

            row = rows.nth(i)

            cells = row.locator(
                ".oxd-table-cell"
            )

            cell_count = cells.count()

            if cell_count < 2:
                continue



            date_value = (
                cells.nth(1)
                .inner_text()
                .strip()
            )

            date_value = " ".join(
                date_value.split()
            )

            if not date_value:
                continue



            if "to" in date_value:

                date_parts = date_value.split(
                    " to "
                )

                if len(date_parts) == 2:

                    start_ui = date_parts[0].strip()
                    end_ui = date_parts[1].strip()

                    start_normalized = (
                        self.normalize_date(
                            start_ui
                        )
                    )

                    end_normalized = (
                        self.normalize_date(
                            end_ui
                        )
                    )

                    normalized_record = (
                        f"{start_normalized} "
                        f"to "
                        f"{end_normalized}"
                    )

                    date_records.append(
                        normalized_record
                    )

                else:

                    date_records.append(
                        date_value
                    )

            else:

                # Single date
                normalized_date = (
                    self.normalize_date(
                        date_value
                    )
                )

                date_records.append(
                    normalized_date
                )

        print(
            "\nNormalized Date records "
            "from My Leave table:"
        )

        for date in date_records:
            print(
                date
            )

        return date_records


    # VERIFY ASSIGNED LEAVE DATE

    def verify_assigned_leave_date(
        self,
        start_date,
        end_date
    ):


        # Test dates remain in standard ISO format:

        start_obj = datetime.strptime(
            start_date,
            "%Y-%m-%d"
        )

        end_obj = datetime.strptime(
            end_date,
            "%Y-%m-%d"
        )


        expected_start = (
            start_obj.strftime(
                "%Y-%m-%d"
            )
        )

        expected_end = (
            end_obj.strftime(
                "%Y-%m-%d"
            )
        )

        expected_date = (
            f"{expected_start} "
            f"to "
            f"{expected_end}"
        )

        print(
            "\nExpected assigned date:",
            expected_date
        )


        # Get normalized dates from My Leave table


        actual_dates = (
            self.get_date_records()
        )

        print(
            "\nActual dates in table:",
            actual_dates
        )


        # Compare

        assert expected_date in actual_dates, (
            f"\nAssigned leave date mismatch!\n"
            f"Expected: {expected_date}\n"
            f"Actual: {actual_dates}"
        )

        print(
            "\nDate verification: PASS"
        )