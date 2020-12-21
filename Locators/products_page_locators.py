from selenium.webdriver.common.by import By


class ProductPageLocators:
    """A class for main page locators.All main page locators should come here"""
    IMG_BROKEN = (By.XPATH, "//img[@class='inventory_item_img' and contains(@src, 'WithGarbageOnItToBreakTheUrl')]")

    BUTTON_ADD_TO_CART = (By.XPATH, '')
    BUTTON_REMOVE = (By.XPATH, '')

    IMG_BAGDE_SHOPPING_CART = (By.XPATH, '//div[@class="shopping_cart_container"]/a')
    LABEL_BAGDE_SHOPPING_CART = (By.XPATH, '//div[@class="shopping_cart_container"]/a/span')
    PART1 = '//div[@class="inventory_item"]['

    def BUTTON_ADD_TO_CART(self, index=1):
        part2 = ']//button[text()="ADD TO CART"]'
        return By.XPATH, (ProductPageLocators.PART1 + str(index) + part2)

    def BUTTON_REMOVE(self, index=1):
        part2 = ']//button[text()="REMOVE"]'
        return By.XPATH, (ProductPageLocators.PART1 + str(index) + part2)

    def LABEL_PRODUCT_NAME(index):
        part2 = ']//div[@class="inventory_item_name"]'
        return By.XPATH, (ProductPageLocators.PART1 + str(index) + part2)

    def LABEL_PRODUCT_DESCRIPTION(index):
        part2 = ']//div[@class="inventory_item_desc"]'
        return By.XPATH, (ProductPageLocators.PART1 + str(index) + part2)

    def LABEL_PRODUCT_PRICE(index):
        part2 = ']//div[@class="inventory_item_price"]'
        return By.XPATH, (ProductPageLocators.PART1 + str(index) + part2)