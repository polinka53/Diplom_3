import allure
from typing import List

from web_locators.order_feed_locators import OrderFeedLocators
from web_pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Проверяем видимость заголовка Ленты заказов")
    def is_feed_header_visible(self, timeout: int = 20) -> bool:
        return self.is_visible(OrderFeedLocators.FEED_HEADER, timeout)

    @allure.step("Получаем значение 'Выполнено за всё время'")
    def get_done_all_time(self) -> int:
        text = self.get_text(OrderFeedLocators.DONE_ALL_TIME_VALUE, timeout=40)
        return int(text.replace(" ", ""))

    @allure.step("Получаем значение 'Выполнено за сегодня'")
    def get_done_today(self) -> int:
        text = self.get_text(OrderFeedLocators.DONE_TODAY_VALUE, timeout=40)
        return int(text.replace(" ", ""))

    @allure.step("Получаем номера заказов в разделе 'В работе'")
    def get_in_progress_numbers(self) -> List[str]:
        elements = self.find_elements_or_empty(
            OrderFeedLocators.IN_PROGRESS_ORDER_NUMBERS, timeout=40
        )

        numbers = []
        for el in elements:
            txt = el.text.strip()
            if txt:
                numbers.append(txt.lstrip("0"))

        return numbers

    def get_in_progress_order_numbers(self) -> List[str]:
        return self.get_in_progress_numbers()