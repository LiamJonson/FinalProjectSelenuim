from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_WATCH = (By.CSS_SELECTOR, "header a.btn.btn-default")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "body th.total")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div#content_inner")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


#class MainPageLocators():
#    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REG = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ENTER = (By.CSS_SELECTOR, "input#id_registration-email")
    PAS1_ENTER = (By.CSS_SELECTOR, "input#id_registration-password1")
    PAS2_ENTER = (By.CSS_SELECTOR, "input#id_registration-password2")
    REG_BTN = (By.CSS_SELECTOR, "form button[name=registration_submit]")
    REG_COMPL = (By.CSS_SELECTOR, "div.alertinner.wicon")



class ProductPageLocators():
    BASKET_ADD_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
