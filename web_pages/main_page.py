import allure
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException

from data.urls import Urls
from data.user_data import TestUser
from web_locators.main_page_locators import MainPageLocators
from web_pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открываем главную страницу")
    def open_main(self):
        self.open(Urls.BASE_URL)

    @allure.step("Открываем ленту заказов")
    def open_feed(self):
        self.open(Urls.FEED_URL)

    @allure.step("Переходим в таб Конструктор")
    def go_to_constructor_tab(self):
        self.click(MainPageLocators.CONSTRUCTOR_TAB)

    @allure.step("Переходим в таб Лента заказов")
    def go_to_order_feed_tab(self):
        self.click(MainPageLocators.ORDER_FEED_TAB)

    @allure.step("Проверяем видимость заголовка Конструктора")
    def is_constructor_header_visible(self) -> bool:
        return self.is_visible(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.step("Проверяем, что модалка ингредиента открыта")
    def is_ingredient_modal_opened(self) -> bool:
        return self.is_visible(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Ожидаем закрытие модалки ингредиента")
    def wait_ingredient_modal_closed(self) -> bool:
        return self.wait_not_visible(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Авторизация с главной страницы")
    def login_from_main(self):
        self.open(Urls.LOGIN_URL)
        email = self.find_element(MainPageLocators.LOGIN_EMAIL_INPUT)
        password = self.find_element(MainPageLocators.LOGIN_PASSWORD_INPUT)
        email.send_keys(TestUser.EMAIL)
        password.send_keys(TestUser.PASSWORD)
        self.click(MainPageLocators.LOGIN_SUBMIT_BUTTON)

    @allure.step("Открываем модалку ингредиента")
    def open_ingredient_modal(self):
        card = self.find_element(MainPageLocators.FIRST_INGREDIENT_CARD)
        self.scroll_into_view(card)
        self.click(MainPageLocators.FIRST_INGREDIENT_CARD)

    @allure.step("Закрываем модалку ингредиента")
    def close_ingredient_modal(self):
        try:
            self.click(MainPageLocators.INGREDIENT_MODAL_CLOSE)
        except TimeoutException:
            return

    @allure.step("Получаем счётчик первого ингредиента")
    def get_ingredient_counter(self) -> int:
        text = self.get_text(MainPageLocators.FIRST_INGREDIENT_COUNTER).strip()
        return int(text) if text else 0

    @allure.step("Добавляем первый ингредиент в конструктор")
    def add_first_ingredient_to_constructor(self):
        card = self.find_element(MainPageLocators.FIRST_INGREDIENT_CARD)
        self.scroll_into_view(card)
        drop_zone = self.find_element(MainPageLocators.CONSTRUCTOR_DROP_ZONE)
        ActionChains(self.driver).drag_and_drop(card, drop_zone).perform()

    @allure.step("Создаем заказ и получаем его номер")
    def create_order_and_get_number(self) -> str:
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)
        self.wait_visible(MainPageLocators.ORDER_MODAL, timeout=40)

        raw_number = self.get_text(MainPageLocators.ORDER_NUMBER).strip()
        number = raw_number.lstrip("0")

        self.click(MainPageLocators.ORDER_MODAL_CLOSE)
        return number