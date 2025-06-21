import pytest
from pages.login_page import LoginPage

def test_login_valid_user(page):
    login_page = LoginPage(page)
    login_page.gotoLogin("https://demo.spreecommerce.org")    
    login_page.login("test_email@test.com", "TestPassword")    
    login_page.validate_flash_message('Signed in successfully.')
