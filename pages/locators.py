from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[value='Log In']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[value='Register']")
class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > .price_color")
    BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p > strong")
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")
