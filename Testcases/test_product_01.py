import sys
import unittest

sys.path.append(".")

from Pages.login_page import LoginPage
from Testcases.base_test import BaseTest
from Objects.account import Account
from Pages.products_page import ProductsPage
from Utils.assertions import Assertion
from Testdata.data import Data


class SauceDemoProduct1(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    def teaDown(self):
        super().teaDown()

    def test_products_display_correctly(self):
        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_STANDARD_USER, Data.PASSWORD)
        login_page.login(account)
        product_page = ProductsPage(self.driver)
        products = Data.read_products_from_json(self)

        for index, expected_product in enumerate(products, start=1):
            '''Add & remove all products'''
            product_page.click_add_to_cart_button(index)
            self.assertTrue(product_page.does_remove_button_exist(index))
            self.assertEqual(1, product_page.get_badge_total())

            product_page.click_remove_button(index)
            self.assertTrue(product_page.does_add_to_cart_button_exist(index))
            self.assertTrue(product_page.is_product_badge_invisible())

            actual_product = product_page.get_product_info(index)
            assertion = Assertion()
            assertion.compare_products(actual_product, expected_product)


if __name__ == '__main__':
    unittest.main()
