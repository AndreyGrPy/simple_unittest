from unittest import TestCase, main
from tests.calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator("2+2"), 4)

    def test_minus(self):
        self.assertEqual(calculator("2-2"), 0)

    def test_divide(self):
        self.assertEqual(calculator("10/5"), 2.0)

    def test_multiply(self):
        self.assertEqual(calculator("2*2"), 4)

    def test_no_sing(self):
        with self.assertRaises(ValueError) as ex:
            calculator("abracadabra")
        self.assertEqual("Expression must contain at least one character(+-/*)", ex.exception.args[0])

    def test_two_character(self):
        with self.assertRaises(ValueError) as ex:
            calculator("2+2+2")
        self.assertEqual("Expression must contain 2 int numbers and 1 sing", ex.exception.args[0])

    def test_mani_sings(self):
        with self.assertRaises(ValueError) as ex:
            calculator("2+22/5*12")
        self.assertEqual("Expression must contain 2 int numbers and 1 sing", ex.exception.args[0])

    def test_no_int(self):
        with self.assertRaises(ValueError) as ex:
            calculator("2.4/5.11")
        self.assertEqual("Expression must contain 2 int numbers and 1 sing", ex.exception.args[0])

    def test_string(self):
        with self.assertRaises(ValueError) as ex:
            calculator("a+b")
        self.assertEqual("Expression must contain 2 int numbers and 1 sing", ex.exception.args[0])


if __name__ == "__main__":
    main()