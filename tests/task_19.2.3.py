import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    # def test_multiply_calculate_failed(self):
    #     assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    # def test_division_calculate_failed(self):
    #     assert self.calc.division(self, 10, 2) == 4

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 10, 2) == 8

    # def test_subtraction_calculate_failed(self):
    #     assert self.calc.subtraction(self, 10, 2) == 9

    def test_addition_calculate_correctly(self):
        assert self.calc.addition(self, 10, 2) == 12

    # def test_addition_calculate_failed(self):
    #     assert self.calc.addition(self, 10, 2) == 13
