import pickle
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)


# Load the saved sentiment analysis model from the .pkl file
with open('sentiment_model.pkl', 'rb') as model_file:

    
    model = pickle.load(model_file)


# Load the fitted CountVectorizer from the vectorizer.pkl file
with open('vectorizer.pkl', 'rb') as vectorizer_file:

    
    vectorizer = pickle.load(vectorizer_file)
    

# Define a function for sentiment analysis
def predict_sentiment(text):

    
    # Vectorize the text using the loaded CountVectorizer
    text_vectorized = vectorizer.transform([text])
    

    # Make a prediction
    prediction = model.predict(text_vectorized)
    

    # Return the result as 'positive' or 'negative'
    return 'positive' if prediction[0] == 1 else 'negative'
    

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])


def index():
    result = None

    
    if request.method == 'POST':
        text = request.form['text']
        result = predict_sentiment(text)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
