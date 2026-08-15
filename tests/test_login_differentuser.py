import os
import pytest

from Pages.login_user import LoginPage
from Pages.dashboard_user import DashboardPage
from Utils.excel_utils import ExcelUtils

#Test-Case-1: Scenario: Validate login functionality using multiple sets of credentials

EXCEL_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "test_data",
    "Data.xlsx"
)


def get_test_data():

    excel = ExcelUtils(
        EXCEL_FILE,
        "LoginData"
    )

    data = excel.get_login_data()

    excel.close()

    return data


@pytest.mark.parametrize(
    "login_data",
    get_test_data()
)
def test_login_with_multiple_credentials(page, login_data):

    excel = ExcelUtils(
        EXCEL_FILE,
        "LoginData"
    )

    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    username = login_data["username"]
    password = login_data["password"]
    excel_row = login_data["row"]

    try:

        login_page.navigate()


        print(f"Row: {excel_row}")
        print(f"Username: {username!r}")
        print(f"Password: {password!r}")
        login_page.login(
            username,
            password
        )



        if login_page.is_login_successful():

            # Valid login

            if dashboard_page.is_dashboard_displayed():

                actual_result = (
                    f"Login successful for user: {username}"
                )

                excel.write_result(
                    excel_row,
                    "PASS",
                    actual_result
                )

                dashboard_page.logout()

            else:

                actual_result = (
                    f"Login URL reached but Dashboard "
                    f"was not displayed for: {username}"
                )

                excel.write_result(
                    excel_row,
                    "FAIL",
                    actual_result
                )

                pytest.fail(actual_result)

        else:
            # Invalid login
            error_message = login_page.get_error_message()

            actual_result = (
                f"Login rejected for user: {username}. "
                f"Message: {error_message}"
            )

            excel.write_result(
                excel_row,
                "PASS",
                actual_result
            )

    except Exception as e:
        # Unexpected failure

        actual_result = (
            f"Test execution failed for user: "
            f"{username}. Error: {str(e)}"
        )

        excel.write_result(
            excel_row,
            "FAIL",
            actual_result
        )

        raise

    finally:

        excel.close()