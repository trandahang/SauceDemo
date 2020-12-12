from Utils.utility import Utility


class Data:
    BASE_URL = 'https://www.saucedemo.com/'
    USERNAME_STANDARD_USER = 'standard_user'
    USERNAME_LOCKED_OUT_USER = 'locked_out_user'
    USERNAME_PROBLEM_USER = 'problem_user'
    USERNAME_PERFORMANCE_USER = 'performance_glitch_user'
    PASSWORD = 'secret_sauce'
    BROWSER = 'ff'

    DATA_JSON_FILE = './Testdata/data.json'

    def get_account_json(self):
        utility = Utility()
        return utility.read_json(Data.DATA_JSON_FILE)
