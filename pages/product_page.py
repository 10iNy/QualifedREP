from .base_page import BasePage
from .basket_page import BasketPage
from .locators import ProductPageLocators
from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def click_to_basket_button(self):
        try:
            login_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
            login_link.click()
        except (NoSuchElementException):
            print(f"Add to basket button not found.")
            
    def check_correctly_buy(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_in_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MESSAGE).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET).text
        assert book_name_in_message == book_name, f"{book_name_in_message}\n{book_name}\n{self.browser.current_url}"
        assert book_price == book_price_in_basket, f"{book_price} not equals {book_price_in_basket}"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be."
    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is not disappeared, but it should have."
