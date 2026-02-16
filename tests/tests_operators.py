import unittest
import sys
sys.path.insert(0, '..')
from operators import add, subtract, multiply, divide


class TestOperations(unittest.TestCase):
    """
    Suite de tests unitaires pour les opérations mathématiques usuelles:
    addition, soustraction, multiplication et division.
    """

    def test_addition(self):
        """Teste l'addition de nombres positifs et de signes opposés."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_addition_with_zero(self):
        """Teste l'addition avec zéro (élément neutre)."""
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(-3, 0), -3)

    def test_addition_commutative(self):
        """Vérifie la commutativité de l'addition."""
        self.assertEqual(add(4, 7), add(7, 4))

    def test_subtract(self):
        """Teste la soustraction avec des entiers positifs et négatifs."""
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(-1, 1), -2)

    def test_subtract_same_values(self):
        """Teste la soustraction d'un nombre par lui-même."""
        self.assertEqual(subtract(5, 5), 0)

    def test_multiply(self):
        """Teste la multiplication de nombres positifs et négatifs."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)

    def test_multiply_by_zero(self):
        """Teste la multiplication par zéro."""
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(-5, 0), 0)

    def test_multiply_by_negative(self):
        """Teste la multiplication de deux nombres négatifs."""
        self.assertEqual(multiply(-2, -3), 6)

    def test_divide(self):
        """Teste la division entière et la division par -1."""
        self.assertEqual(divide(2, 2), 1)
        self.assertEqual(divide(9, -1), -9)

    def test_divide_non_integer_result(self):
        """Teste une division donnant un résultat non entier."""
        self.assertAlmostEqual(divide(5, 2), 2.5)

    def test_divide_by_one(self):
        """Teste la division par 1 (élément neutre)."""
        self.assertEqual(divide(7, 1), 7)
        self.assertEqual(divide(-7, 1), -7)

    def test_divide_zero_numerator(self):
        """Teste la division avec zéro au numérateur."""
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self):
        """Vérifie qu'une division par zéro lève une exception."""
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_division_not_commutative(self):
        """Vérifie que la division n'est pas commutative."""
        self.assertNotEqual(divide(10, 2), divide(2, 10))


if __name__ == '__main__':
    unittest.main()
