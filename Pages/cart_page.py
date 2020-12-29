import logging

from Pages.base_page import BasePage
from Locators.cart_page_locators import CartPageLocators
from Objects.product import Product


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def click_remove_button(self, index):
        self.click(CartPageLocators.BUTTON_REMOVE(index))

    def get_product_info(self, index):
        name = self.get_text(CartPageLocators.LABEL_PRODUCT_NAME(index))
        desc = self.get_text(CartPageLocators.LABEL_PRODUCT_DESC(index))
        price = self.get_text(CartPageLocators.LABEL_PRODUCT_PRICE(index))
        quatity = self.get_text(CartPageLocators.LABEL_PRODUCT_QUANTITY(index))
        product = Product(name, desc, price, quatity)
        return product

    def click_checkout_button(self):
        self.click(CartPageLocators.BUTTON_CHECKOUT)

    def click_coutinue_button(self):
        self.click(CartPageLocators.BUTTON_CONTINUE)

