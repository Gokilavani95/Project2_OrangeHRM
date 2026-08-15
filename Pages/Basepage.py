class BasePage:

    def __init__(self,page):
        self.page=page

    def click(self,locator):
        self.page.locator(locator).click()

    def fill(self,locator,value):
        self.page.locator(locator).fill(value)

    def text(self,locator):
        return self.page.locator(locator).text_content()

    def visible(self,locator):
        return self.page.locator(locator).is_visible()

    def wait(self,locator):
        self.page.locator(locator).wait_for(state="visible")