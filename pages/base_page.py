from playwright.async_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def navigate(self, url: str):
        await self.page.goto(url)

    async def click(self, selector: str):
        await self.page.click(selector)

    async def fill(self, selector: str, text: str):
        await self.page.fill(selector, text)

    async def get_text(self, selector: str) -> str:
        return await self.page.text_content(selector)
