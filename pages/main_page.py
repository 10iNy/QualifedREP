from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
from .locators import BasePageLocators
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
