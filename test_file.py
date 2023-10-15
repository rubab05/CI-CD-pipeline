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

    def test_predict_sentiment_positive(self):
        # Input a positive movie review
        positive_review = "I absolutely loved this movie! It was fantastic."

        # Post the positive review to the predict route
        response = self.app.post('/', data={'text': positive_review}, follow_redirects=True)

        # Ensure the response contains 'positive'
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'positive', response.data)

        # Modify this part to check the result in the response
        self.assertIn(b'The sentiment of the review is: positive', response.data)

if __name__ == '__main__':
    unittest.main()
