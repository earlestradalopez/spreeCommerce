from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("#user_email")
        self.password_input = page.locator("#user_password")
        self.password_input_confirmation = page.locator("#user_password_confirmation")
        self.login_button = page.locator('input[type="submit"][value="Login"]')
        self.signup_button = page.locator('input[type="submit"][value="Sign Up"]')

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def signUp(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.password_input_confirmation.fill(password)
        self.signup_button.click()
