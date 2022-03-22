from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class BasketPageLocators():
    TITLE_OF_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-title")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE_AFTER_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > div.alert > div > p:nth-child(1)")
    PRODUCT_PRICE_IN_SUCCESS_MESSAGE_AFTER_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
