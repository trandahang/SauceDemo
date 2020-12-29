import logging

from Objects.product import Product
from Pages.base_page import BasePage
from Locators.checkout_step_two_page_locators import CheckOutStepTwoLocators
from Utils.utility import Utility


class CheckoutStepTwoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def click_finish(self):
        self.click(CheckOutStepTwoLocators.BUTTON_FINISH)

    def click_cancel_button(self):
        self.click(CheckOutStepTwoLocators.BUTTON_CANCEL)

    def get_product_info(self, index):
        name = self.get_text(CheckOutStepTwoLocators.LABEL_PRODUCT_NAME(index))
        desc = self.get_text(CheckOutStepTwoLocators.LABEL_PRODUCT_DESCRIPTION(index))
        price = self.get_text(CheckOutStepTwoLocators.LABEL_PRODUCT_PRICE(index))
        product = Product(name, desc, price)
        return product

    def get_item_total(self):
        self.click(CheckOutStepTwoLocators.LABEL_ITEM_TOTAL)

    def get_item_total(self, auto_convert=True):
        text = self.get_text(CheckOutStepTwoLocators.LABEL_ITEM_TOTAL)
        if auto_convert:
            return Utility().convert_string_to_float(text)
        else:
            return

    def get_tax(self, auto_convert=True):
        text = self.get_text(CheckOutStepTwoLocators.LABEL_TAX)
        if auto_convert:
            return Utility().convert_string_to_float(text)
        else:
            return

    def get_total(self, auto_convert=True):
        text = self.get_text(CheckOutStepTwoLocators.LABEL_TOTAL)
        if auto_convert:
            return Utility().convert_string_to_float(text)
        else:
            return