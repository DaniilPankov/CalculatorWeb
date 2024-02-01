from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@given("I have a calculator on {url}")
def step(context, url):
    op = Options()
    op.add_argument("--no-sandbox")
    op.add_argument("start-maximized")
    op.add_argument("window-size=1900,1080")
    op.add_argument("disable-gpu")
    op.add_argument("--disable-software-rasterizer")
    op.add_argument("--disable-dev-shm-usage")

    context.browser = webdriver.Chrome(options=op)
    context.browser.get(url)


@given("I have entered {number} in {base} in {entry_field} entry")
def step(context, number, base, entry_field):
    field = context.browser.find_element(By.ID, entry_field)
    field.send_keys(number)
    global dropdown_element
    if entry_field == "first":
        dropdown_element = context.browser.find_element(By.ID, "firstBase")
    elif entry_field == "second":
        dropdown_element = context.browser.find_element(By.ID, "secondBase")
    dropdown = Select(dropdown_element)
    if base == "dec":
        dropdown.select_by_visible_text("Десятичная")
    elif base == "bin":
        dropdown.select_by_visible_text("Двоичная")
    elif base == "oct":
        dropdown.select_by_visible_text("Восьмеричная")
    elif base == "hex":
        dropdown.select_by_visible_text("Шестнадцатеричная")


@given("I have chosen {operation} operation")
def step(context, operation):
    dropdown_element = context.browser.find_element(By.ID, "operation")
    dropdown = Select(dropdown_element)
    if operation == "sum":
        dropdown.select_by_visible_text("Сложение")
    elif operation == "sub":
        dropdown.select_by_visible_text("Вычитание")
    elif operation == "mul":
        dropdown.select_by_visible_text("Умножение")
    elif operation == "div":
        dropdown.select_by_visible_text("Деление")
    elif operation == "mod":
        dropdown.select_by_visible_text("mod")
    elif operation == "pow":
        dropdown.select_by_visible_text("Степень")


@given("I have chosen {type} as type of result")
def step(context, type):
    dropdown_element = context.browser.find_element(By.ID, "resultBase")
    dropdown = Select(dropdown_element)
    if type == "dec":
        dropdown.select_by_visible_text("Десятичная")
    elif type == "bin":
        dropdown.select_by_visible_text("Двоичная")
    elif type == "oct":
        dropdown.select_by_visible_text("Восьмеричная")
    elif type == "hex":
        dropdown.select_by_visible_text("Шестнадцатеричная")


@when("I press button")
def step(context):
    time.sleep(1)
    context.browser.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(1)


@then("The result should be {result} on the screen")
def step(context, result):
    txt = context.browser.find_element(By.ID, "result").text
    assert txt == f"Результат: {result}"

@then("An ZeroDivisionError should be raised")
def step(context):
    txt = context.browser.find_element(By.ID, "error").text
    assert txt == "Ошибка: Второй параметр не должен быть равен 0"

@then("An ValueError should be raised")
def step(context):
    txt = context.browser.find_element(By.ID, "error").text
    assert txt == "Ошибка: Невалидный второй параметр"
