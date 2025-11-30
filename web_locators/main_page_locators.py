from selenium.webdriver.common.by import By


class MainPageLocators:
    # Табы в шапке
    CONSTRUCTOR_TAB = (
        By.XPATH,
        "//header//a[@href='/' and .//p[text()='Конструктор']]",
    )
    ORDER_FEED_TAB = (
        By.XPATH,
        "//header//a[@href='/feed' and .//p[contains(text(),'Лента заказов')]]",
    )

    # Заголовок конструктора
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")

    # Логин
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    LOGIN_EMAIL_INPUT = (
        By.XPATH,
        "//label[contains(., 'Email') or contains(., 'E-mail')]/following-sibling::input",
    )
    LOGIN_PASSWORD_INPUT = (
        By.XPATH,
        "//label[contains(., 'Пароль')]/following-sibling::input",
    )

    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//form//button[text()='Войти']")

    # Ингредиент (конкретная булка)
    FIRST_INGREDIENT_CARD = (
        By.XPATH,
        "//p[text()='Флюоресцентная булка R2-D3']/ancestor::a[1]",
    )
    FIRST_INGREDIENT_COUNTER = (
        By.XPATH,
        "//p[text()='Флюоресцентная булка R2-D3']"
        "/ancestor::a[1]//p[contains(@class,'counter_counter__num')]",
    )

    # Модалка ингредиента
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_MODAL_CLOSE = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal__')]//button",
    )

    # Область конструктора
    CONSTRUCTOR_DROP_ZONE = (
        By.XPATH,
        "//main//section[contains(@class,'BurgerConstructor')]",
    )

    # Заказ
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal__')]"
        "//p[contains(text(),'идентификатор заказа')]",
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal__')]"
        "//h2[contains(@class,'digits-large')]",
    )
    ORDER_MODAL_CLOSE = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal__')]"
        "//button[contains(@class,'close')]",
    )