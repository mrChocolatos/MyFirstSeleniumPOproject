from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        login_link.click()

    def get_product_name(self):
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_product_text = name_product.text
        return name_product_text

    def get_product_name_alert(self):
        name_product = self.browser.find_element(*ProductPageLocators.ALERT_ADD_PROD)
        alert_product_text = name_product.text
        return alert_product_text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ADD_PROD), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_ADD_PROD), \
            "Element was not disappeared"

    def write_code(self):
        self.solve_quiz_and_get_code()

    def corrected_add_product(self):
        assert self.get_product_name() == self.get_product_name_alert()

    def corrected_add_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert product_price.text == f'{basket_price.text}', f'{product_price.text} dont equal {basket_price.text}'
