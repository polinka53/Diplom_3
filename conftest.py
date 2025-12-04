import pytest
from selenium import webdriver


BROWSERS = ["chrome", "firefox"]


@pytest.fixture(params=BROWSERS)
def driver(request):
    browser = request.param

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")          
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        drv = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")              
        options.set_preference("browser.tabs.warnOnClose", False)
        drv = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Неизвестный браузер: {browser}")

    drv.maximize_window()
    yield drv
    drv.quit()