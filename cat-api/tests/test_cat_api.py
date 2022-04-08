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
    def test_get_animal_mila(self, mock_func):
        response = self.client.get(url_for('get_cat'))
        self.assert200(response)
        self.assertIn(b'Mila', response.data)
    
    @patch('application.routes.choice', return_value='Phoenix')
    def test_get_animal_phoenix(self, mock_func):
        response = self.client.get(url_for('get_cat'))
        self.assert200(response)
        self.assertIn(b'Phoenix', response.data)
        