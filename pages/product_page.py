from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def should_be_success_message_after_add_product_to_basket(self):
        self.should_be_success_message_product_add_to_basket()
        self.should_be_product_name_in_message()
        self.should_be_success_message_of_basket_total()
        self.should_be_product_price_in_message()

    def should_be_success_message_of_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_BASKET_TOTAL),\
            "Success message with basket total is not presented"

    def should_be_success_message_product_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT_TO_BASKET),\
            "Success message that product add to basket is not presented"

    def should_be_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_AFTER_ADD_TO_BASKET).text
        assert product_name == message, f"Expected '{product_name}' in success message instead of {message}"

    def should_be_product_price_in_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE_AFTER_ADD_TO_BASKET).text
        assert product_price == message, f"Expected '{product_price}' in success message instead of {message}"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappear"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
