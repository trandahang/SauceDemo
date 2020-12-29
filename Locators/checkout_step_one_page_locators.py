from selenium.webdriver.common.by import By
from Locators.products_page_locators import ProductPageLocators


class CheckOutStepOneLocators(object):
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    BUTTON_CONTINUE = (By.XPATH, '//input[@class="btn_primary cart_button"]')
    BUTTON_CANCEL = (By.XPATH, '//a[@class="cart_cancel_link btn_secondary"]')

    def LABEL_PRODUCT_NAME(index):
        part2 = ']//div[@class="inventory_item_name"]'
        return By.XPATH, (ProductPageLocators.PART1 + str(index) + part2)

    def LABEL_PRODUCT_DESCRIPTION(index):
        part2 = ']//div[@class="inventory_item_desc"]'
        return By.XPATH, (ProductPageLocators.PART1 + str(index) + part2)

    def LABEL_PRODUCT_PRICE(index):
        part2 = ']//div[@class="inventory_item_price"]'
        return By.XPATH, (ProductPageLocators.PART1 + str(index) + part2)
