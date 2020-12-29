from selenium.webdriver.common.by import By


class CheckOutStepTwoLocators(object):
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    BUTTON_FINISH = (By.XPATH, "//div[@class='cart_footer']/a[contains(@class,'btn_action cart_button')]")
    LABEL_PAYMENT_INFO = (By.XPATH, "//div[@class='summary_value_label'][1]")
    LABEL_SHIPPING_INFO = (By.XPATH, "//div[@class='summary_value_label'][2]")
    LABEL_ITEM_TOTAL = (By.XPATH, "//div[@class='summary_subtotal_label']")
    LABEL_TAX = (By.XPATH, "//div[@class='summary_tax_label']")
    LABEL_TOTAL = (By.XPATH, "//div[@class='summary_total_label']")

    PART1 = '//div[@class="cart_item"]['

    def LABEL_PRODUCT_NAME(index):
        part2 = ']//div[@class="inventory_item_name"]'
        return By.XPATH, (CheckOutStepTwoLocators.PART1 + str(index) + part2)

    def LABEL_PRODUCT_DESCRIPTION(index):
        part2 = ']//div[@class="inventory_item_desc"]'
        return By.XPATH, (CheckOutStepTwoLocators.PART1 + str(index) + part2)

    def LABEL_PRODUCT_PRICE(index):
        part2 = ']//div[@class="inventory_item_price"]'
        return By.XPATH, (CheckOutStepTwoLocators.PART1 + str(index) + part2)
