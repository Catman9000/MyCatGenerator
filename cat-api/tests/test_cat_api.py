from application import app
import application.routes
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    @patch('application.routes.choice', return_value='Mila')
    def test_get_animal_cat(self, mock_func):
        response = self.client.get(url_for('Mila'))
        self.assert200(response)
        self.assertIn(b'Mila', response.data)
    
    @patch('application.routes.choice', return_value='treat')
    def test_get_animal_dog(self, mock_func):
        response = self.client.get(url_for('treat'))
        self.assert200(response)
        self.assertIn(b'treat', response.data)
        