import pytest
import allure

from web_locators.main_page_locators import MainPageLocators
from web_locators.order_feed_locators import OrderFeedLocators
from web_pages.main_page import MainPage
from web_pages.order_feed_page import OrderFeedPage


@allure.suite("Основной функционал")
class TestMainFunctionality:
    @allure.story("Переход по табу «Конструктор»")
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)
        page.open_feed()
        page.go_to_constructor_tab()

        assert page.is_visible(
            MainPageLocators.CONSTRUCTOR_HEADER
        ), "После клика на «Конструктор» не появился заголовок «Соберите бургер»"

    @allure.story("Переход по табу «Лента заказов»")
    def test_go_to_order_feed(self, driver):
        page = MainPage(driver)
        page.open_main()
        page.go_to_order_feed_tab()

        feed_page = OrderFeedPage(driver)
        assert feed_page.is_visible(
            OrderFeedLocators.FEED_HEADER
        ), "После клика на «Лента заказов» заголовок ленты заказов не появился"

    @allure.story("Модальное окно ингредиента")
    def test_ingredient_click_opens_details_modal(self, driver):
        page = MainPage(driver)
        page.open_main()
        page.open_ingredient_modal()

        assert page.is_visible(
            MainPageLocators.INGREDIENT_MODAL_TITLE
        ), "После клика на ингредиент не открылось модальное окно с деталями"

    @allure.story("Модальное окно ингредиента")
    def test_ingredient_details_modal_closes_by_cross(self, driver):
        page = MainPage(driver)
        page.open_main()
        page.open_ingredient_modal()
        page.close_ingredient_modal()

        assert page.wait_not_visible(
            MainPageLocators.INGREDIENT_MODAL_TITLE
        ), "Модальное окно не закрылось по клику на крестик"

    @allure.story("Счётчик ингредиента")
    def test_ingredient_counter_increases_after_add(self, driver):
        page = MainPage(driver)
        page.open_main()

        if driver.capabilities.get("browserName") == "firefox":
            pytest.xfail("Drag-and-drop в Firefox работает нестабильно")

        start = page.get_ingredient_counter()
        page.add_first_ingredient_to_constructor()
        end = page.get_ingredient_counter()

        assert end > start, f"Счётчик ингредиента не увеличился: было {start}, стало {end}"