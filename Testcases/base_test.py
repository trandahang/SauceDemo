import os
import unittest
from selenium import webdriver
import sys
sys.path.append('.')

from Utils.utility import Utility

class BaseTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        #Setting up how we want Chrome to run
        utility = Utility()
        browser = utility.get_browser()

        self.driver = self.startBrowser(browser)
        #self.driver = webdriver.Firefox(executable_path=r'Drivers\geckodriver.exe')
        self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        #To do
        try:
            self.driver.close()
            self.driver.quit()
        except Exception as e:
            pass

    def startBrowser(name):
        """
        browser, "filefox" "chrome" "ie" "phantomjs"
        :param name:
        :return:
        """
        try:
            if name.lower() == 'firefox' or name.lower() == 'ff':
                print('start browser name:Firefox')
                return webdriver.Firefox(executable_path=r'Drivers\geckodriver.exe')
            elif name.lower() == 'chrome':
                print('start browser name:Chrome')
                return webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')
            elif name.lower() == 'phantomjs':
                print('start browser name:Phantomjs')
                return webdriver.PhantomJS()
            else:
                print("Not found this browser, You can use'firefox'")
                return webdriver.Firefox(executable_path=r'Drivers\geckodriver.exe')
        except Exception as msg:
            print('message: %s' % str(msg))



