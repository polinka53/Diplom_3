from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException

from data.urls import Urls
from data.user_data import TestUser
from web_locators.main_page_locators import MainPageLocators
from web_pages.base_page import BasePage


class MainPage(BasePage):
    def open_main(self):
        self.open(Urls.BASE_URL)

    def open_feed(self):
        self.open(Urls.FEED_URL)

    def go_to_constructor_tab(self):
        self.click(MainPageLocators.CONSTRUCTOR_TAB)

    def go_to_order_feed_tab(self):
        try:
            self.click(MainPageLocators.ORDER_FEED_TAB)
        except TimeoutException:
            self.open(Urls.FEED_URL)

    def login_from_main(self):
        self.open(Urls.LOGIN_URL)
        self.find_element(MainPageLocators.LOGIN_EMAIL_INPUT).send_keys(TestUser.EMAIL)
        self.find_element(MainPageLocators.LOGIN_PASSWORD_INPUT).send_keys(
            TestUser.PASSWORD
        )
        self.click(MainPageLocators.LOGIN_SUBMIT_BUTTON)

    def open_ingredient_modal(self):
        card = self.find_element(MainPageLocators.FIRST_INGREDIENT_CARD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", card)
        card.click()

    def close_ingredient_modal(self):
        try:
            btn = self.find_element(MainPageLocators.INGREDIENT_MODAL_CLOSE)
            self.driver.execute_script("arguments[0].click();", btn)
        except TimeoutException:
            # если не нашли кнопку — считаем, что модалка уже закрыта
            pass

    def get_ingredient_counter(self) -> int:
        try:
            text = self.get_text(MainPageLocators.FIRST_INGREDIENT_COUNTER)
        except Exception:
            return 0
        text = text.strip()
        return int(text) if text else 0

    def add_first_ingredient_to_constructor(self):
        card = self.find_element(MainPageLocators.FIRST_INGREDIENT_CARD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", card)
        drop_zone = self.find_element(MainPageLocators.CONSTRUCTOR_DROP_ZONE)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(card, drop_zone).perform()

    def create_order_and_get_number(self) -> str:
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)
        self.wait_visible(MainPageLocators.ORDER_MODAL, timeout=40)
        number = self.get_text(MainPageLocators.ORDER_NUMBER)
        self.click(MainPageLocators.ORDER_MODAL_CLOSE)
        return number