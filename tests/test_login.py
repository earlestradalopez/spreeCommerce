import pytest
from pages.login_page import LoginPage

@pytest.mark.asyncio
async def test_valid_login(page):
    login_page = LoginPage(page)
    await login_page.navigate("https://demo.spreecommerce.org")
    await login_page.login("test_email@test.com", "TestPassword")
    assert "Spree Commerce DEMO" in await page.title()
