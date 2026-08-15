from Pages.Basepage import BasePage
from playwright.sync_api import Page,expect
class MyInfoPage(BasePage):

    items=[
        "Personal Details",
        "Contact Details",
        "Emergency Contacts",
        "Dependents",
        "Immigration",
        "Job",
        "Salary",
        "Report-to",
        "Qualifications",
        "Memberships"
    ]

    def verify_items(self):
        tabs = "a.orangehrm-tabs-item"

        def verify_items(self):
            for item in self.items:
                tab = self.page.locator(self.tabs).filter(has_text=item)

                expect(tab).to_be_visible()
                expect(tab).to_be_clickable()

                tab.click()
