from selenium.webdriver.common.by import By


class CartLocators(object):
  """A class for cart page locators. All cart page locators should come here"""
  BUTTON_CHECKOUT = (By.XPATH, "//div[@class='cart_footer']/a[text()='CHECKOUT']")
  BUTTON_CONTINUE = (By.XPATH, "//div[@class='cart_footer']/a[text()='Continue Shopping']")
  ICON_CART_BADGE = (By.ID, "shopping_cart_container")
  CART_ITEM = "//div[@class='cart_list']//div[@class='cart_item']["

  def BUTTON_REMOVE(index):
    ITEM = "]//button[text()='REMOVE']"
    return (By.XPATH, (CartLocators.CART_ITEM + str(index) + ITEM))

  def LABEL_PRODUCT_QUANTITY(index):
    ITEM = "]//div[@class='cart_quantity']"
    return (By.XPATH, (CartLocators.CART_ITEM + str(index) + ITEM))

  def LABEL_PRODUCT_NAME(index):
    ITEM = "]//div[@class='inventory_item_name']"
    return (By.XPATH, (CartLocators.CART_ITEM + str(index) + ITEM))

  def LABEL_PRODUCT_DESC(index):
    ITEM = "]//div[@class='inventory_item_desc']"
    return (By.XPATH, (CartLocators.CART_ITEM + str(index) + ITEM))

  def LABEL_PRODUCT_PRICE(index):
    ITEM = "]//div[@class='inventory_item_price']"
    return (By.XPATH, (CartLocators.CART_ITEM + str(index) + ITEM))
