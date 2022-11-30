import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc=Calculator

    def test_mul_calc_correct(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_mul_calc_ok(self):
        assert self.calc.adding(self,2, 2) == 4

    def test_mul_calc_cort(self):
        assert self.calc.division(self,8, 2) == 4

    def test_mul_calc_corr(self):
        assert self.calc.subtraction(self,6, 2) == 4