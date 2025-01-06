import pickle


model_path = r'C:\Users\rcjad\Desktop\Desktop Files\NLP\CodeSoft ML Internship\Movie\Models\Movie_Genre_Prediction_Logistic_Regression_Model.pkl'

TFIDV_Path = r'C:\Users\rcjad\Desktop\Desktop Files\NLP\CodeSoft ML Internship\Movie\Models\TFIDV.pkl'

model = pickle.load(open(model_path,'rb'))
tfidv = pickle.load(open(TFIDV_Path,'rb'))

def Prediction_Time():
    Description = input("Enter the Description of the Movie : ")
    vectorizer = tfidv.transform([Description])
    Prediction = model.predict(vectorizer)
    Prediction = str(Prediction[0])
    return Prediction
print(Prediction_Time())