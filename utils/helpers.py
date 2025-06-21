import random
import string

def wait_for_and_click(page, selector):
    page.wait_for_selector(selector)
    page.click(selector)

def generateRandomWord():
    random_word = ''.join(random.choices(string.ascii_lowercase, k=8))
    return random_word