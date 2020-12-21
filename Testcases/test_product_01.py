import sys
import unittest

sys.path.append(".")

from Pages.login_page import LoginPage
from Testcases.base_test import BaseTest
from Objects.account import Account
from Testdata.data import Data
from Pages.products_page import ProductsPage
import time

class SauceDemoProduct1(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    def teaDown(self):
        super().teaDown()

    def test_product1(self):
        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_STANDARD_USER, Data.PASSWORD)
        login_page.login(account)

        products_page = ProductsPage(self.driver)
        #total = products_page.get_badge_total()
        #print(total)
        #products_page.click_badge_icon()
        #products_page.click_add_to_cart_button(1)
        #products_page.click_remove_button(1)
        time.sleep(10)
        products_page.get_all_products_info()

if __name__ == '__main__':
    unittest.main()
