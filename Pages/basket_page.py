from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def agree_that_basket_is_empty(self):
        basket_text_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT)
        basket_text = basket_text_empty.text
        assert basket_text == 'Ваша корзина пуста Продолжить покупки', f'{basket_text} is not equal "Ваша корзина пуста"'

    def check_basket_is_empty_negative(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), 'Basket is not empty!!!'



