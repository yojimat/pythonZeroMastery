import unittest
import main as my_main


class TestMain_2(unittest.TestCase):

    def test_get_guess_0(self):
        #test_param = 1
        result = my_main.get_guess()
        self.assertEqual(result, 1)

    def test_get_guess_1(self):
        #test_param = "1"
        result = my_main.get_guess()
        self.assertIsInstance(result, ValueError)

    def test_try_guess_0(self):
        test_param = 1
        answer = 1
       	result = my_main.try_guess(test_param, answer)
        self.assertEqual(result, True)

    def test_try_guess_1(self):
        test_param = 1
        answer = 2
        result = my_main.try_guess(test_param, answer)
        self.assertEqual(result, None)

    def test_try_guess_2(self):
        test_param = 309
        answer = 2
        result = my_main.try_guess(test_param, answer)
        self.assertEqual(result, False)
