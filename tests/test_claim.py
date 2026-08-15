from Pages.Claimpage import ClaimPage
from Pages.Loginpage import LoginPage

#Test-Case-10: Scenario: Initiate a claim request

username = "Admin"
password = "admin123"
event_name = "Medical Reimbursement"
currency_value="Indian Rupee"

expense_type = "Planned Surgery"
exp_date = "2026-08-05"
amount =10000
def test_claim_validation(page):

    login=LoginPage(page)
    claim = ClaimPage(page)

    login.login(username,password)

    claim.go_to_claim_page()

    claim.navigate_to_submit_claim()
    claim.create_claim(
        event_name=event_name,
        currency=currency_value
    )

    print("pass")
    ref_id = claim.get_ref_id()
    print("Reference ID:", ref_id)

    event = claim.get_event()
    print("Event ID:", event)

    currency = claim.get_currency()
    print("Currency:", currency)

    status = claim.get_status()
    print("Status:", status)


    claim.add_expense()
    success_message = claim.exp_details(
        expense_type,
        exp_date,
        amount
    )

   #print("Expense Details:")

    #Success message after save
    print("Success Message:", success_message)

    #Submit claim
    submit_success_message = claim.claim_submit()
    assert submit_success_message == "Successfully Saved"
    print("Submit Success Message:", submit_success_message)

    #verify my claim
    display_ref_id = claim.verify_submitted_claim(ref_id)
    assert display_ref_id == ref_id
    print(display_ref_id)