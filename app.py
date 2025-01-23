# Import Section
from flask import Flask, render_template, request
import pickle

# Model File Path.
model_path = r'C:\Users\rcjad\Desktop\Desktop Files\NLP\CodeSoft ML Internship\Movie\Models\Movie_Genre_Prediction_Logistic_Regression_Model.pkl'

# TFIDF-vectorizer Model File Path. 
TFIDV_Path = r'C:\Users\rcjad\Desktop\Desktop Files\NLP\CodeSoft ML Internship\Movie\Models\TFIDV.pkl'

# Load Model and TFIDF Vectorizer
model = pickle.load(open(model_path, 'rb'))
tfidv = pickle.load(open(TFIDV_Path, 'rb'))

# Helper Function
def Prediction_Time():
    try:
        Description = request.form['text-area']
        vectorizer = tfidv.transform([Description])  # Transform the input text
        Prediction = str(model.predict(vectorizer)[0])     # Predict the genre
        return Prediction                   # Return prediction as a string
    except Exception as e:
        return f"Error during prediction:  {str(e)}"

# Flask Application
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure index.html exists in the 'templates' folder

@app.route('/pred', methods=['POST'])
def prediction():
    if request.method == 'POST':
        try:
            pred = Prediction_Time()
            print(pred)  # For debugging purposes
            return render_template('index.html', Prediction_Result = pred)
            # return f"Predicted Genre: {pred}"
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "Please submit a valid POST request."

if __name__ == '__main__':
    app.run(port=3000, debug=True)
