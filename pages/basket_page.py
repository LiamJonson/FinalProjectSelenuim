from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_watch_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_WATCH), "Add to basket is not found"
    def should_be_no_product(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_IN_BASKET), "There is a product in the basket"
    def should_be_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.BASKET_IS_EMPTY), "There is a product in the basket"


