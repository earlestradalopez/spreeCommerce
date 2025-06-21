from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def gotoLogin(self, url: str):
        self.page.goto(url, wait_until="networkidle")        
        self.page.click("#section-3942 > header > nav > div.page-container > div > div.flex.items-center.gap-4.flex-1.justify-end > div:nth-child(2) > button > svg")

    def logOut(self):        
        self.page.click("#section-3942 > header > nav > div.page-container > div > div.flex.items-center.gap-4.flex-1.justify-end > div:nth-child(2) > a > svg")
        self.page.locator("button", has_text="Log out").click()
        
    def gotoSignUp(self, url: str):
        self.page.goto(url, wait_until="networkidle")        
        self.page.click("#section-3942 > header > nav > div.page-container > div > div.flex.items-center.gap-4.flex-1.justify-end > div:nth-child(2) > button > svg")
        self.page.wait_for_selector("a:has-text('Sign Up')")
        self.page.click("a:has-text('Sign Up')")
        waitText = True
        while(waitText):
            actual_text = self.page.inner_text("h2")
            if actual_text == 'Sign Up':
                waitText = False

    def get_title(self):
        return self.page.title()
    
    def validate_flash_message(self, text: str):
        flash_message = self.page.locator("p.flash-message")    
        expect(flash_message).to_have_text(text)
    
