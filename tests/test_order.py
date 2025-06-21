import pytest
import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.helpers import generateRandomWord

def test_order(page):
    login_page = LoginPage(page)
    login_page.gotoLogin("https://demo.spreecommerce.org")    
    login_page.login("test_email@test.com", "TestPassword")    
    login_page.validate_flash_message('Signed in successfully.')

    main_page = MainPage(page)
    main_page.shopAllBrowse()
    time.sleep(2)
    main_page.validate_page('SHOP ALL')
    
    
    main_page.selectshopAllproduct()    
    main_page.validate_text("Ripped T-Shirt", "#product-details-page > div.lg\:col-span-5.lg\:col-start-8 > div > div.hidden.lg\:block")
    
    main_page.selectSize('SMALL')
    main_page.addToCartItem()
    main_page.validate_text("Shipping & taxes calculated at checkout", "#cart_summary")

    main_page.checkout()
    main_page.validate_text("This is the Spree Commerce DEMO checkout", "#checkout-message")

    main_page.saveAndContinue()
    main_page.validate_text("Delivery method from Shop location", "#methods > div > h5")
    main_page.saveAndContinue()
    main_page.validate_text("All transactions are secure and encrypted", "#checkout_payment_methods")

    main_page.select_paycheck()
    main_page.proceedCheckOut()
    main_page.validate_order()
