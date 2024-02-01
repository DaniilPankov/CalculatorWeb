import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def check_addition(driver):
    field = driver.find_element(By.ID, "first")
    field.send_keys("Aa")
    time.sleep(1)
    field = driver.find_element(By.ID, "second")
    field.send_keys("10")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button").click()
    txt = driver.find_element(By.ID, "error").text
    time.sleep(2)
    return txt == "Ошибка: Невалидный первый параметр"

def check_subtraction(driver):
    field = driver.find_element(By.ID, "first")
    field.send_keys("10")
    time.sleep(1)
    field = driver.find_element(By.ID, "second")
    field.send_keys("20")
    time.sleep(1)
    dropdown_element = driver.find_element(By.ID, "operation")
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Вычитание")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button").click()
    txt = driver.find_element(By.ID, "result").text
    time.sleep(2)
    return txt == f"Результат: {10 - 20}"

def check_multiplication(driver):
    field = driver.find_element(By.ID, "first")
    field.send_keys("100")
    time.sleep(1)
    field = driver.find_element(By.ID, "second")
    field.send_keys("70")
    time.sleep(1)
    dropdown_element = driver.find_element(By.ID, "operation")
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Умножение")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button").click()
    txt = driver.find_element(By.ID, "result").text
    time.sleep(2)
    return txt == f"Результат: {100 * 70}"


def check_division(driver):
    field = driver.find_element(By.ID, "first")
    field.send_keys("100")
    time.sleep(1)
    field = driver.find_element(By.ID, "second")
    field.send_keys("70")
    time.sleep(1)
    dropdown_element = driver.find_element(By.ID, "operation")
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Деление")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button").click()
    txt = driver.find_element(By.ID, "result").text
    time.sleep(2)
    return txt == f"Результат: {100 / 70}"

def check_mod(driver):
    field = driver.find_element(By.ID, "first")
    field.send_keys("100")
    time.sleep(1)
    field = driver.find_element(By.ID, "second")
    field.send_keys("70")
    time.sleep(1)
    dropdown_element = driver.find_element(By.ID, "operation")
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Модуль")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button").click()
    txt = driver.find_element(By.ID, "result").text
    time.sleep(2)
    return txt == f"Результат: {100 % 70}"

def check_pow(driver):
    field = driver.find_element(By.ID, "first")
    field.send_keys("5")
    time.sleep(1)
    field = driver.find_element(By.ID, "second")
    field.send_keys("10")
    time.sleep(1)
    dropdown_element = driver.find_element(By.ID, "operation")
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Степень")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button").click()
    txt = driver.find_element(By.ID, "result").text
    time.sleep(2)
    return txt == f"Результат: {5 ** 10}"
