from unittest import TestCase
from main.main_my import func
from main.main_my import square_equation_solver, TypEr
import pytest
from unittest.mock import patch


def test_ok():
    res = func(8, 2)
    assert res == 10

class TestedUnit(TestCase):

    def test_check_qaua(self):
        with self.assertRaises(TypeError):
            square_equation_solver("", 2, 1.5)

    def test_check_typle(self):
        res = square_equation_solver(0, 0, 1)
        self.assertIsInstance(res, tuple)

    def test_result_zero(self):
        res = square_equation_solver(0, 0, 1)
        self.assertEqual(res, (None, None))

    def test_result_ok(self):
        res = square_equation_solver(1, -3, -4)
        self.assertEqual(res, (4, -1))


class TestByPytest(object):


    def test_raises(self):
        with pytest.raises(TypeError) as err:
            square_equation_solver("1", 2, 1.5)
        assert str(err.value) == TypEr

    def test_check_typle(self):
        res = square_equation_solver(0, 0, 1)
        assert isinstance(res, tuple)

    @pytest.mark.parametrize("args , result", [pytest.param((1, -3, -4), (4, -1), id="first"),
                                               pytest.param((0, 0, 1), (None, None), id="second")])
    def test_silved_ok(self, args, result):
        res = square_equation_solver(*args)
        assert res == result
