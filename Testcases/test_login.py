import sys
import unittest

sys.path.append(".")

from Pages.login_page import LoginPage
from Testcases.base_test import BaseTest
from Objects.account import Account
from Testdata.data import Data

class SauceDemoLogin1(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    def teaDown(self):
        super().teaDown()

    def test_login_with_standard_user(self):
        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_STANDARD_USER, Data.PASSWORD)
        login_page.login(account)

    def test_login_with_locked_out_user(self):
        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_LOCKED_OUT_USER, Data.PASSWORD)
        login_page.login(account)

    def test_login_with_problem_user(self):
        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_PROBLEM_USER, Data.PASSWORD)
        login_page.login(account)

    def test_login_with_performance_glitch_user(self):
        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_PERFORMANCE_USER, Data.PASSWORD)
        login_page.login(account)

    def test_login_with_invalid_username(self):
        login_page = LoginPage(self.driver)
        account = Account('Hang123', Data.PASSWORD)
        login_page.login(account)

    def test_login_with_invalid_password(self):
        login_page = LoginPage(self.driver)
        account = Account(Data.USERNAME_STANDARD_USER, 'Hang123')
        login_page.login(account)

if __name__ == '__main__':
    unittest.main()
