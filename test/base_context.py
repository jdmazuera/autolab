import unittest

from app import create_app, db

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config="app.testing")
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
    
    def tearDown(self):
        with self.app.app_context():
            # Elimina todas las tablas de la base de datos
            db.session.remove()
            db.drop_all()
