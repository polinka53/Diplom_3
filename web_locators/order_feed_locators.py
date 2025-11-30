from selenium.webdriver.common.by import By


class OrderFeedLocators:
    FEED_HEADER = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")

    DONE_ALL_TIME_VALUE = (
        By.XPATH,
        "//p[contains(text(),'Выполнено за') and contains(text(),'время')]/following-sibling::p[1]",
    )
    DONE_TODAY_VALUE = (
        By.XPATH,
        "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p[1]",
    )

    IN_PROGRESS_ORDER_NUMBERS = (
        By.XPATH,
        "//h2[contains(text(),'В работе')]/following-sibling::ul[1]//li",
    )