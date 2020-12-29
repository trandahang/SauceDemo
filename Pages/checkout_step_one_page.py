import logging

from Pages.base_page import BasePage
from Locators.checkout_step_one_page_locators import CheckOutStepOneLocators


class CheckoutStepOnePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def click_cancel_button(self):
        self.click(CheckOutStepOneLocators.BUTTON_CANCEL)

    def click_continue_button(self):
        self.click(CheckOutStepOneLocators.BUTTON_CONTINUE)

    def add_checkout_info(self, Checkout):
        self.enter_text(CheckOutStepOneLocators.FIRST_NAME, Checkout.firstname)
        self.enter_text(CheckOutStepOneLocators.LAST_NAME, Checkout.lastname)
        self.enter_text(CheckOutStepOneLocators.ZIP_CODE, Checkout.zipcode)
