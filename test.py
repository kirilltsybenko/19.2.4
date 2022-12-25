import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self, 4, 3) == 7

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 11, 10) == 1

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.division(self, 1, 0)

    def test_multiply_success(self):
        assert self.calculator.multiply(self, 20, 2) == 40

    def test_division_success(self):
        assert self.calculator.division(self, 100, 2) == 50

    def teardown(self):
        print('Выполнение метода Teardown')
