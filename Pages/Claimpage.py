
from Pages.Basepage import BasePage
from playwright.sync_api import Page, expect


class ClaimPage(BasePage):

    claim_page = "text=Claim"
    submit_claim = "text=Submit Claim"

    event = (
        "//label[normalize-space()='Event']"
        "/following::div[contains(@class,'oxd-select-text')][1]"
    )

    currency = (
        "//label[normalize-space()='Currency']"
        "/following::div[contains(@class,'oxd-select-text')][1]"
    )

    create = "//button[normalize-space()='Create']"

    Ref_id = (
        "//div[@class='orangehrm-card-container']"
        "//div[1]//div[1]//div[1]//div[1]//div[2]//input[1]"
    )

    # Selected Event value
    event_selected = (
        "//label[normalize-space()='Event']" 
        "/ancestor::div[contains(@class,'oxd-input-group')]" 
        "//input"
    )

    # Selected Currency value
    currency_check = (
        "//label[normalize-space()='Currency']" 
        "/ancestor::div[contains(@class,'oxd-input-group')]" 
        "//input"
    )

    # Selected Status value
    status = (
        "//label[normalize-space()='Status']" 
        "/ancestor::div[contains(@class,'oxd-input-group')]" 
        "//input"
    )

    #Add exp button
    expense_add = (
        "//h6[normalize-space()='Expenses']" 
        "/following::button[normalize-space()='Add'][1]"
    )

    #expenses Type dropdown
    expense_type_dropdown = (
        "//label[normalize-space()='Expense Type']" 
        "/following::div[contains(@class,'oxd-select-text')][1]"
    )
    def go_to_claim_page(self):
        self.page.locator(self.claim_page).click()

    def navigate_to_submit_claim(self):
        self.page.locator(self.submit_claim).click()

    def create_claim(self, event_name, currency):
        # Select Event
        self.page.locator(self.event).click()

        option = self.page.locator(
            f"//div[@role='listbox']//span[normalize-space()='{event_name}']"
        )

        expect(option).to_be_visible()
        option.click()

        # Select Currency
        self.page.locator(self.currency).click()

        option = self.page.locator(
            f"//div[@role='listbox']//span[normalize-space()='{currency}']"
        )

        expect(option).to_be_visible()
        option.click()

        # Create claim
        self.page.locator(self.create).click()

    def get_ref_id(self):
        ref_id_value = self.page.locator(self.Ref_id).input_value()
        return ref_id_value

    def get_event(self):
        return self.page.locator(self.event_selected).input_value()

    def get_currency(self):
        currency_selected = self.page.locator(self.currency_check)
        expect(currency_selected).to_be_visible()
        return currency_selected.input_value()

    def get_status(self):
        status_selected = self.page.locator(self.status)
        expect(status_selected).to_be_visible()
        return status_selected.input_value()

    def add_expense(self):
        self.page.locator(self.expense_add).click()

    def exp_details(self,expense_type,date,amount_value):
        # Click Expense Type dropdown
        dropdown =  self.page.locator(self.expense_type_dropdown)
        expect(dropdown).to_be_visible()
        dropdown.click()
        # Select option from dropdown
        option = self.page.locator(
            "//div[@role='listbox']" 
            f"//span[normalize-space()='{expense_type}']"
        )
        expect(option).to_be_visible()
        option.click()

        date_field = self.page.get_by_placeholder("yyyy-dd-mm")
        date_field.fill(date)

        #Add amount
        amount = self.page.locator(
            "//label[normalize-space()='Amount']"
            "/following::input[1]"
        )
        amount.fill(str(amount_value))

        #save expenses
        self.page.get_by_text(" Save ").click()

        #Success message
        success_message = self.page.locator(
            "//div[contains(@class,'oxd-toast')]" 
            "//p[contains(@class,'oxd-text--toast-message')]"
        )
        expect(success_message).to_be_visible()
        return success_message.inner_text().strip()

    def claim_submit(self):
        #submit the claim
        submit = self.page.get_by_role("button", name="Submit")
        submit.click()
        submit_success_message = self.page.locator(
            "//div[contains(@class,'oxd-toast')]" 
            "//p[contains(@class,'oxd-text--toast-message')]"
        )
        expect(submit_success_message).to_be_visible()
        return submit_success_message.inner_text().strip()

    def verify_submitted_claim(self,ref_id):
        myclaim_page = self.page.get_by_text("My Claims")
        myclaim_page.click()

        #find reference id record
        ref_id_locator = self.page.locator(
            "//div[contains(@class,'oxd-table-body')]" 
            f"//div[contains(@class,'oxd-table-cell')]" 
            f"[normalize-space()='{ref_id}']")
        expect(ref_id_locator).to_be_visible()
        return ref_id_locator.inner_text().strip()
