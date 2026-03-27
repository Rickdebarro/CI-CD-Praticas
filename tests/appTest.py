import unittest
from app.app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_print_health_check(self):
        response = self.app.get('/health-check')
        self.assertEqual(200, response.status_code, "Erro no test_http_code!")
        self.assertEqual("<h1>Hello, I'm Alive!</h1>", response.get_data(as_text=True), "Erro no test_print_health_check!")

    def test_print_hello_error(self):
        response = self.app.get('/hello')
        self.assertEqual(400, response.status_code, "Erro: A rota deveria retornar 400 (Bad Request)!")
        self.assertEqual("Nome não informado", response.get_data(as_text=True), "Erro na mensagem de validação!")

    def test_print_hello_sucess(self):
        # Simulando uma requisição passando "?name=Andre"
        response = self.app.get('/hello?name=Andre')
        self.assertEqual(200, response.status_code, "Erro: A rota deveria retornar 200 (Sucesso)!")
        self.assertEqual("Hello, Andre!", response.get_data(as_text=True), "Erro na mensagem de sucesso!")