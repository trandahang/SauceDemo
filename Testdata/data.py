
from Objects.product import Product
from Utils.utility import Utility


class Data:
    BASE_URL = 'https://www.saucedemo.com/'
    USERNAME_STANDARD_USER = 'standard_user'
    USERNAME_LOCKED_OUT_USER = 'locked_out_user'
    USERNAME_PROBLEM_USER = 'problem_user'
    USERNAME_PERFORMANCE_USER = 'performance_glitch_user'
    PASSWORD = 'secret_sauce'
    BROWSER = 'Chrome'

    PRODUCT_FILE = 'Testdata/products.json'

    """def read_products_from_json(self):
        products = []
        with open(Data.PRODUCT_FILE) as json_file:
            data = json.load(json_file)
            for obj in data['products']:
                product = Product(obj['name'], obj['desc'], obj['price'])
                products.append(product)
        json_file.close()"""

    def read_products_from_json(sefl):
        products = []
        data = Utility.read_json(Data.PRODUCT_FILE)
        for item in data['products']:
            product = Product(item['name'], item['desc'], item['price'])
            products.append(product)
        return products
