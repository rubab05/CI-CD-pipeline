import unittest
from app import app, predict_sentiment

class TestSentimentAnalysisApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index_page_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_predict_sentiment_positive(self):
        text = "I loved the movie. It was fantastic!"
        sentiment = predict_sentiment(text)
        self.assertEqual(sentiment, 'positive')

    def test_predict_sentiment_negative(self):
        text = "The movie was terrible, I hated it."
        sentiment = predict_sentiment(text)
        self.assertEqual(sentiment, 'negative')

    def test_post_request_with_positive_review(self):
        response = self.app.post('/', data={'text': 'This is a great movie!'})
        self.assertIn(b'Predicted Sentiment: positive', response.data)

    def test_post_request_with_negative_review(self):
        response = self.app.post('/', data={'text': 'I did not like this movie at all.'})
        self.assertIn(b'Predicted Sentiment: negative', response.data)

if __name__ == '__main__':
    unittest.main()
