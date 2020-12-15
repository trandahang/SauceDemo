import logging

from Pages.base_page import BasePage
from Locators.products_page_locators import ProductPageLocators

class ProductsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def get_product_url(self):
        return self.get_current_url()

    def count_broken_images(self):
        return self.get_elements_size(ProductPageLocators.IMG_BROKEN)



