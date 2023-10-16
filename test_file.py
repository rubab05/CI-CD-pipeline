import unittest
from flask import Flask
from flask.testing import FlaskClient

# Import your Flask app and ensure it's in the same directory
from app import app, predict_sentiment

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client for the app
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_predict_sentiment_negative(self):
        # Input a negative movie review
        negative_review = "This movie was terrible. I hated every moment of it."

        # Post the negative review to the predict route
        response = self.app.post('/', data={'text': negative_review}, follow_redirects=True)

        # Ensure the response contains 'negative'
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'negative', response.data)

if __name__ == '__main__':
    unittest.main()
