from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "#user_email"
        self.password_input = "#user_password"
        self.login_button = 'input[type="submit"][value="Login"]'

    async def login(self, username: str, password: str):
        await self.fill(self.username_input, username)
        await self.fill(self.password_input, password)
        await self.click(self.login_button)
