from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_buy_product(self):
        self.should_be_add_to_basket_btn()
        self.add_to_basket()
        self.should_price_check()
        self.should_name_comparison()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_ADD_BTN), "Add to basket is not found"

    def add_to_basket(self):
        add_item_btn = self.browser.find_element(*ProductPageLocators.BASKET_ADD_BTN)
        add_item_btn.click()
        self.solve_quiz_and_get_code()

    def should_price_check(self):
        product_price_check = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price_check = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert basket_price_check.text == product_price_check.text, "Prices in basket and in product page isn't equal"

    def should_name_comparison(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_name = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET)

        print(basket_name, product_name)
        assert product_name in basket_name.text, "Name in basket and product are not equal"
