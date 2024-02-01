import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import testcases

class CalcTestCases(unittest.TestCase):

    def setUp(self) -> None:
        url = 'http://127.0.0.1:5000/calculator'

        op = Options()
        op.add_argument("--no-sandbox")
        op.add_argument("start-maximized")
        op.add_argument("window-size=1900,1080")
        op.add_argument("disable-gpu")
        op.add_argument("--disable-software-rasterizer")
        op.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=op)
        self.driver.get(url)


    def test_case_addition(self):
        assert testcases.check_addition(self.driver)

    def test_case_subtraction(self):
        assert testcases.check_subtraction(self.driver)

    def test_case_multiplication(self):
        assert testcases.check_multiplication(self.driver)

    def test_case_division(self):
        assert testcases.check_division(self.driver)

    def test_case_mod(self):
        assert testcases.check_mod(self.driver)

    def test_case_pow(self):
        assert  testcases.check_pow(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()
