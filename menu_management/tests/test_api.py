import unittest
from api.routes import app, db
from flask_testing import TestCase

class APITestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_and_get_meal(self):
        response = self.client.post('/meal/Breakfast/category', json={'name': 'Main Course'})
        self.assertEqual(response.status_code, 201)
        response = self.client.post('/meal/Breakfast/item', json={'category': 'Main Course', 'name': 'Pancakes', 'description': 'Fluffy pancakes'})
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/meal/Breakfast')
        self.assertEqual(response.status_code, 200)
