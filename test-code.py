from verification import miller_rabin_test
import unittest

class TestMonModule(unittest.TestCase):
    def test_prime(self):
        lst_not_prime = [6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]
        lst_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
        
        for prime in lst_prime:
            result = miller_rabin_test(prime, 15)
            print(f"Testing prime: {prime}, Result: {result}")  # Debug
            self.assertTrue(result, f"Échec sur {prime}, attendu True mais obtenu {result}")

        for not_prime in lst_not_prime:
            result = miller_rabin_test(not_prime, 15)
            print(f"Testing not prime: {not_prime}, Result: {result}")  # Debug
            self.assertFalse(result, f"Échec sur {not_prime}, attendu False mais obtenu {result}")


if __name__ == '__main__':
    unittest.main()
            
