import logging

from Pages.base_page import BasePage
from Locators.products_page_locators import ProductPageLocators
from Objects.product import Product

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

    def get_product_info(self, index):
        name = self.get_text(ProductPageLocators.LABEL_PRODUCT_NAME(index))
        desc = self.get_text(ProductPageLocators.LABEL_PRODUCT_DESCRIPTION(index))
        price = self.get_text(ProductPageLocators.LABEL_PRODUCT_PRICE(index))
        product = Product(name, desc, price)
        print(product)
        return product

    def get_all_products_info(self):
        products = []
        for index in range(1, 7):
            print(index)
            product = self.get_product_info(index)
            products.append(product)
        return products



