from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_page_has_main_heading(driver, page_url):
    driver.get(page_url)

    heading = driver.find_element(By.TAG_NAME, "h1")

    assert heading.text == "Заявка на консультацию"


def test_form_fields_are_visible(driver, page_url):
    driver.get(page_url)

    assert driver.find_element(By.ID, "name").is_displayed()
    assert driver.find_element(By.ID, "email").is_displayed()
    assert driver.find_element(By.ID, "direction").is_displayed()
    assert driver.find_element(By.ID, "submit-button").text == "Отправить заявку"


def test_success_message_after_submit(driver, page_url):
    driver.get(page_url)

    driver.find_element(By.ID, "name").send_keys("Иван")
    driver.find_element(By.ID, "email").send_keys("ivan@example.com")
    Select(driver.find_element(By.ID, "direction")).select_by_value("testing")
    driver.find_element(By.ID, "comment").send_keys("Нужна консультация")
    driver.find_element(By.ID, "submit-button").click()

    result = driver.find_element(By.ID, "result")

    assert "Заявка отправлена, Иван!" in result.text
    assert "Тестирование" in result.text


def test_reset_button_clears_result(driver, page_url):
    driver.get(page_url)

    driver.find_element(By.ID, "name").send_keys("Ольга")
    driver.find_element(By.ID, "email").send_keys("olga@example.com")
    Select(driver.find_element(By.ID, "direction")).select_by_value("frontend")
    driver.find_element(By.ID, "submit-button").click()
    driver.find_element(By.ID, "reset-button").click()

    assert driver.find_element(By.ID, "result").text == ""
