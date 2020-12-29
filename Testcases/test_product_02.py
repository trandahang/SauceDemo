import sys
import unittest

from Utils.utility import Utility

sys.path.append(".")

from Objects.account import Account
from Pages.login_page import LoginPage
from Testcases.base_test import BaseTest
from Pages.products_page import ProductsPage
from Pages.cart_page import CartPage
from Testdata.data import Data
from Utils.assertions import Assertion
from Pages.checkout_step_one_page import CheckoutStepOnePage
from Pages.checkout_step_two_page import CheckoutStepTwoPage
from Objects.checkout_step_one import CheckoutStepOne


class SauceDemoProduct2(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    def teaDown(self):
        super().teaDown()

    def test_product2(self):
        products = Data.read_products_from_json(self)
        assertion = Assertion()

        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_STANDARD_USER, Data.PASSWORD)
        login_page.login(account)
        product_page = ProductsPage(self.driver)

        for index in [1, 2, 3]:
            product_page.click_add_to_cart_button(index)

        product_page.click_badge_icon()
        cart_page = CartPage(self.driver)

        for index in [1, 2, 3]:
            actual_product = cart_page.get_product_info(index)
            expected_product = products[index - 1]
            assertion.compare_products(actual_product, expected_product)

        cart_page.click_checkout_button()
        checkout_step_one_page = CheckoutStepOnePage(self.driver)
        checkout_step_one = CheckoutStepOne('a', 'b', 123)
        checkout_step_one_page.add_checkout_info(checkout_step_one)
        checkout_step_one_page.click_continue_button()

        checkout_step_two_page = CheckoutStepTwoPage(self.driver)
        total_price = 0.00
        for index in [1, 2, 3]:
            actual_product = checkout_step_two_page.get_product_info(index)
            expected_product = products[index - 1]
            assertion.compare_products(actual_product, expected_product)
            print(actual_product.quantity)
            total_price += Utility().multiple(actual_product.quantity, actual_product.price)

        actual_tax = total_price * 0.08004
        self.assertEqual(float("{:.2f}".format(actual_tax)), checkout_step_two_page.get_tax())

        actual_total = total_price + actual_tax
        self.assertEqual(float("{:.2f}".format(actual_total)), checkout_step_two_page.get_total())

        print(checkout_step_two_page.get_item_total())
        print(checkout_step_two_page.get_tax())
        print(checkout_step_two_page.get_total())
        checkout_step_two_page.click_finish()


if __name__ == '__main__':
    unittest.main()
