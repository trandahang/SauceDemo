from selenium.webdriver.common.by import By


class LoginpageLocators:
    """A class for main page locators.All main page locators should come here"""
    INPUT_USERNAME = (By.ID, 'user-name')
    INPUT_PASSWORD = (By.ID, 'password')
    BUTTON_LOGIN = (By.ID, 'login-button')
    LABEL_ERROR = (By.XPATH, '//h3[@data-test="error"]')
