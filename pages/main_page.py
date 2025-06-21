from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.shopall_button = page.locator('#block-6467 > a > span') # SHOP ALL
        self.fashion_button = page.locator('#block-6468 > a > span') # FASHION
        self.wellnes_button = page.locator('#block-6469 > a > span') # WELLNESS
        self.new_arrival_button = page.locator('#block-6470 > a > span') #NEW ARRIVAL

        self.shopall_product1 = page.locator('#product-254')
        self.shopall_product2 = page.locator('#product-255')

        self.select_size = page.locator('#product-variant-picker > fieldset:nth-child(3) > div > div.flex.items-center.justify-between > button')
        self.small_size = page.locator('#product-variant-picker > fieldset:nth-child(3) > div > div.absolute.top-11.left-0.z-\[9999\].flex.w-screen.max-w-max.shadow-xs > div > label:nth-child(2)')        
        self.medium_size = page.locator('#product-variant-picker > fieldset:nth-child(3) > div > div.absolute.top-11.left-0.z-\[9999\].flex.w-screen.max-w-max.shadow-xs > div > label:nth-child(3)')        
        self.large_size = page.locator('#product-variant-picker > fieldset:nth-child(3) > div > div.absolute.top-11.left-0.z-\[9999\].flex.w-screen.max-w-max.shadow-xs > div > label:nth-child(4)')        

        self.addtocart = page.locator('#product-details-page > div.lg\:col-span-5.lg\:col-start-8 > div > div.h-full.w-full.waitlist-modal > form > div.flex.w-full.my-5 > div.w-full.bottom-0.flex.flex-col.gap-4.z-10 > button')
        self.checkout_button = page.locator("a.btn-primary[data-cart-target='checkoutButton']")
        self.save_continue_button = page.locator("button:has-text('Save and Continue')")
        self.selectCheck = page.locator("#order_payments_attributes__payment_method_id_24")
        self.proceedCheckout = page.locator("#checkout-payment-submit")

    def shopAllBrowse(self):
        self.shopall_button.click()

    def fashionBrowse(self):
        self.fashion_button.click()

    def wellnessBrowse(self):
        self.wellnes_button.click()

    def newArrivalBrowse(self):
        self.new_arrival_button.click()

    def selectshopAllproduct(self):
        self.shopall_product1.click()

    def selectSize(self, size: str):
        self.select_size.click()
        if size == 'SMALL':
            self.small_size.click()
    
    def addToCartItem(self):
        self.addtocart.click()

    def checkout(self):
        self.checkout_button.click()

    def saveAndContinue(self):
        self.save_continue_button.click()

    def select_paycheck(self):
        self.selectCheck.click()

    def proceedCheckOut(self):
        self.proceedCheckout.click()

    def validate_page(self, text: str):
        actual_text = self.page.inner_text("h1")
        assert actual_text == text, f"Text mismatch: {actual_text}"
    
    def validate_order(self):
        actual_text = ''
        waitText = True
        while(waitText):
            actual_text = self.page.inner_text("h5")
            if actual_text == 'Your order is confirmed!':
                waitText = False
            
        assert actual_text == 'Your order is confirmed!'