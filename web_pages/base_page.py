from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
)

DEFAULT_TIMEOUT = 20


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def wait_visible(self, locator, timeout: int = DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout: int = DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator, timeout: int = DEFAULT_TIMEOUT):
        element = self.wait_clickable(locator, timeout)
        try:
            element.click()
        except (ElementClickInterceptedException, ElementNotInteractableException):
            self.driver.execute_script("arguments[0].click();", element)

    def is_visible(self, locator, timeout: int = DEFAULT_TIMEOUT) -> bool:
        try:
            element = self.wait_visible(locator, timeout)
            return element.is_displayed()
        except TimeoutException:
            return False

    def wait_not_visible(self, locator, timeout: int = DEFAULT_TIMEOUT) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_text(self, locator, timeout: int = DEFAULT_TIMEOUT) -> str:
        return self.wait_visible(locator, timeout).text

    def find_element(self, locator, timeout: int = DEFAULT_TIMEOUT):
        return self.wait_visible(locator, timeout)

    def find_elements(self, locator, timeout: int = DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def wait_url_contains(self, part: str, timeout: int = DEFAULT_TIMEOUT) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(part))
            return True
        except TimeoutException:
            return False