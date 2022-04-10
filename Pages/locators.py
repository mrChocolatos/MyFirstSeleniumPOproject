from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_EMPTY_TEXT = (By.XPATH, '//*[@id="content_inner"]/p')
    PRODUCT_IN_BASKET = (By.XPATH, ' // *[ @ id = "basket_formset"] / div / div')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGIST_FORM = (By.CSS_SELECTOR, "#register_form")
    RESIST_EMAIL_INPUT = (By.XPATH, ' //*[@id="id_registration-email"]')
    RESIST_PASS1_INPUT = (By.XPATH, ' //*[@id="id_registration-password1"]')
    RESIST_PASS2_INPUT = (By.XPATH, ' //*[@id="id_registration-password2"]')
    RESIST_SUBMIT = (By.XPATH, ' //*[@id="register_form"]/button')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    ALERT_ADD_PROD = (By.XPATH, '// *[ @ id = "messages"] / div[1] / div / strong')
    BASKET_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
