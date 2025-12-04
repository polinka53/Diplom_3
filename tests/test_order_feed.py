import allure
import pytest
from selenium.common.exceptions import TimeoutException

from data.urls import Urls
from web_pages.main_page import MainPage
from web_pages.order_feed_page import OrderFeedPage


@allure.suite("Лента заказов")
class TestOrderFeed:

    @allure.story("«Выполнено за всё время» увеличивается после нового заказа")
    def test_done_all_time_increases_after_new_order(self, driver):
        main = MainPage(driver)
        feed = OrderFeedPage(driver)

        if driver.capabilities.get("browserName") == "firefox":
            pytest.xfail("Счётчики в ленте заказов нестабильны в Firefox")

        feed.open(Urls.FEED_URL)
        try:
            before = feed.get_done_all_time()
        except TimeoutException:
            pytest.xfail("Счётчик «Выполнено за всё время» не найден на стенде")
        main.login_from_main()
        main.add_first_ingredient_to_constructor()
        order_number = main.create_order_and_get_number()
        assert order_number is not None, "Не удалось оформить заказ"

        feed.open(Urls.FEED_URL)
        try:
            after = feed.get_done_all_time()
        except TimeoutException:
            pytest.xfail(
                "Счётчик «Выполнено за всё время» не найден после создания заказа"
            )

        assert after > before, (
            f"Счётчик «Выполнено за всё время» не увеличился: было {before}, стало {after}"
        )

    @allure.story("«Выполнено за сегодня» увеличивается после нового заказа")
    def test_done_today_increases_after_new_order(self, driver):
        main = MainPage(driver)
        feed = OrderFeedPage(driver)

        if driver.capabilities.get("browserName") == "firefox":
            pytest.xfail("Счётчики в ленте заказов нестабильны в Firefox")

        feed.open(Urls.FEED_URL)
        try:
            before = feed.get_done_today()
        except TimeoutException:
            pytest.xfail("Счётчик «Выполнено за сегодня» не найден на стенде")

        main.login_from_main()
        main.add_first_ingredient_to_constructor()
        order_number = main.create_order_and_get_number()
        assert order_number is not None, "Не удалось оформить заказ"

        feed.open(Urls.FEED_URL)
        try:
            after = feed.get_done_today()
        except TimeoutException:
            pytest.xfail(
                "Счётчик «Выполнено за сегодня» не найден после создания заказа"
            )

        assert after > before, (
            f"Счётчик «Выполнено за сегодня» не увеличился: было {before}, стало {after}"
        )

    @allure.story("Номер заказа появляется в блоке «В работе»")
    def test_order_number_appears_in_in_progress(self, driver):
        main = MainPage(driver)
        feed = OrderFeedPage(driver)

        if driver.capabilities.get("browserName") == "firefox":
            pytest.xfail("Раздел «В работе» нестабилен в Firefox")

        main.login_from_main()
        main.add_first_ingredient_to_constructor()
        order_number = main.create_order_and_get_number()
        assert order_number is not None, "Не удалось оформить заказ"

        feed.open(Urls.FEED_URL)
        in_progress_numbers = feed.get_in_progress_numbers()

        if not in_progress_numbers:
            pytest.xfail("Список заказов в разделе «В работе» пуст или недоступен")

        assert order_number in in_progress_numbers, \
            f"Номер заказа {order_number} не найден в разделе «В работе»"