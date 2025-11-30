from typing import List

from web_locators.order_feed_locators import OrderFeedLocators
from web_pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def get_done_all_time(self) -> int:
        text = self.get_text(OrderFeedLocators.DONE_ALL_TIME_VALUE, timeout=40)
        return int(text.replace(" ", ""))

    def get_done_today(self) -> int:
        text = self.get_text(OrderFeedLocators.DONE_TODAY_VALUE, timeout=40)
        return int(text.replace(" ", ""))

    def get_in_progress_numbers(self) -> List[str]:
        elements = self.driver.find_elements(
            *OrderFeedLocators.IN_PROGRESS_ORDER_NUMBERS
        )
        return [el.text.strip() for el in elements if el.text.strip()]