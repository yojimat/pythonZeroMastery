import unittest
import main as my_main


class TestMain(unittest.TestCase):
    """Exemplo de teste"""

    def setUp(self):
        print("Método executado antes de cada função")

    def test_do_stuff(self):
        ''' Comentário/Descrição do teste'''
        test_param = 10
        result = my_main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff_2(self):
        test_param = 'stdasring'
        result = my_main.do_stuff(test_param)
        self.assertEqual(result, "Please enter a number")

    def test_do_stuff_3(self):
        test_param = None
        result = my_main.do_stuff(test_param)
        self.assertEqual(result, "Please enter a number")

    def test_do_stuff_4(self):
        test_param = ""
        result = my_main.do_stuff(test_param)
        self.assertEqual(result, "Please enter a number")

    def test_do_stuff_5(self):
        test_param = 0
        result = my_main.do_stuff(test_param)
        self.assertEqual(result, 5)

    def tearDown(self):
        print("Método que é executado após cada função")

if __name__ == "__main__":
    unittest.main()

# python -m unittest -v comando para rodar testes
