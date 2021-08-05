from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[value='Log In']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[value='Register']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "[name='registration-email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='registration-password1']")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > .price_color")
    BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p > strong")
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators():
    EMPTY_MESSAGE =(By.CSS_SELECTOR, "#content_inner > p")
    BASKET_SUMMARY = (By.CSS_SELECTOR, ".basket_summary")
