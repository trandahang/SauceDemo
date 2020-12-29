import sys
import unittest

sys.path.append(".")

from Pages.login_page import LoginPage
from Testcases.base_test import BaseTest
from Objects.account import Account
from Testdata.data import Data
from Pages.products_page import ProductsPage


class SauceDemoLogin1(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    def teaDown(self):
        super().teaDown()

    @unittest.skip
    def test_login_with_standard_user(self):
        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_STANDARD_USER, Data.PASSWORD)
        login_page.login(account)

        product_page = ProductsPage(self.driver)
        url = product_page.get_product_url()
        print(url)
        self.assertEqual(url, 'https://www.saucedemo.com/inventory.html')

    @unittest.skip
    def test_login_with_locked_out_user(self):
        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_LOCKED_OUT_USER, Data.PASSWORD)
        login_page.login(account)
        error_locked_out_user = login_page.get_error_message()
        self.assertIn('Sorry, this user has been locked out.', error_locked_out_user)

    @unittest.skip
    def test_login_with_test_error(self):
        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_STANDARD_USER, Data.USERNAME_STANDARD_USER)
        login_page.login(account)
        error_user_pass = login_page.get_error_message()
        self.assertIn('Username and password do not match any user in this service', error_user_pass)

    def test_login_with_problem_user(self):
        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_PROBLEM_USER, Data.PASSWORD)
        login_page.login(account)
        products_page = ProductsPage(self.driver)
        total = products_page.count_broken_images()
        self.assertEqual(0, total)

    @unittest.skip
    def test_login_with_performance_glitch_user(self):
        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_PERFORMANCE_USER, Data.PASSWORD)
        login_page.login(account)

    @unittest.skip
    def test_login_with_invalid_username(self):
        login_page = LoginPage(self.driver)
        account = Account('Hang123', Data.PASSWORD)
        login_page.login(account)

    @unittest.skip
    def test_login_with_invalid_password(self):
        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_STANDARD_USER, 'Hang123')
        login_page.login(account)


if __name__ == '__main__':
    unittest.main()
