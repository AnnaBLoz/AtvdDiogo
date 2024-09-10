import unittest

class BibliotecaFiccaoCientifica:
    
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo):
        self.livros.append(titulo)

    def listar_livros(self):
        return self.livros


class BibliotecaFiccaoCientificaTestes(unittest.TestCase):

    def setUp(self):
        self.biblioteca = BibliotecaFiccaoCientifica()

    def test_adicionar_livro(self):
        self.biblioteca.adicionar_livro("Duna")
        self.assertIn("Duna", self.biblioteca.listar_livros())

    def test_listar_livros(self):
        self.biblioteca.adicionar_livro("Neuromancer")
        self.biblioteca.adicionar_livro("Fahrenheit 451")
        self.assertEqual(self.biblioteca.listar_livros(), ["Neuromancer", "Fahrenheit 451"])

if __name__ == "__main__":
    unittest.main()
