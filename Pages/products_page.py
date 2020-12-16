import logging

from Pages.base_page import BasePage
from Locators.products_page_locators import ProductPageLocators


class ProductsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def get_product_url(self):
        return self.get_current_url()

    def click_badge_icon(self):
        self.click(ProductPageLocators.IMG_BAGDE_SHOPPING_CART)

    def get_badge_total(self):
        index = 0
        try:
            text = self.get_text(ProductPageLocators.LABEL_BAGDE_SHOPPING_CART, 0)
            index = int(text)
        except:
            pass
        return index

    def click_add_to_cart_button(self, index):
        self.click(ProductPageLocators.BUTTON_ADD_TO_CART(index))

    def click_remove_button(self, index):
        self.click(ProductPageLocators.BUTTON_REMOVE(index))




