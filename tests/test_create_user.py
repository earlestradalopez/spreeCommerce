import pytest
from pages.login_page import LoginPage
from utils.helpers import generateRandomWord

def test_sign_up(page):
    login_page = LoginPage(page)
    login_page.gotoSignUp("https://demo.spreecommerce.org")    
    username = generateRandomWord() + '@test.com'
    password = generateRandomWord()
    login_page.signUp( username, password)
    login_page.validate_flash_message('Welcome! You have signed up successfully.')

    login_page.logOut()
    # Validate created User

    login_page.gotoLogin("https://demo.spreecommerce.org")    
    login_page.login( username, password)
    login_page.validate_flash_message('Signed in successfully.')

