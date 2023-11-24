import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def run_browser():
    with sync_playwright() as p:
        yield p

def test_authorization(run_browser):
    playwright = run_browser
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Перейти на главную www.sima-land.ru
    page.goto("https://www.sima-land.ru/")

    # В хедере нажать на кнопку "Войти"
    page.get_by_test_id("nav-item:cabinet").get_by_test_id("link").click()

    # Ввести логин: qa_test@test.ru
    page.get_by_test_id("login-field").get_by_test_id("text-field:field").click()
    page.get_by_test_id("login-field").get_by_test_id("text-field:field").fill("qa_test@test.ru")

    # Ввести пароль: qa_test
    page.get_by_test_id("password-field").get_by_test_id("text-field:field").click()
    page.get_by_test_id("password-field").get_by_test_id("text-field:field").fill("qa_test")

    # Нажать кнопку "Войти"
    page.get_by_test_id("button").click()

    # Дождаться появления элемента "nav-item:favorites", свидетельствующего об успешной авторизации
    page.wait_for_selector("[data-testid=nav-item:favorites]")

    # Закрыть браузер и контекст
    context.close()
    browser.close()
