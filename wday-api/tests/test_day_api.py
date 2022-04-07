from application import app
from flask_testing import TestCase
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    def test_get_day_mila(self):
        response = self.client.post(url_for('wday'), json={"cat":"mila"})
        self.assert200(response)
        self.assertIn(b'Monday', response.data)
    
    def test_get_day_lilo(self):
        response = self.client.post(url_for('wday'), json={"cat":"lilo"})
        self.assert200(response)
        self.assertIn(b'Sunday', response.data)