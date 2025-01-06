# Import Section...
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Path Specification...
test_path = r'C:\Users\rcjad\Desktop\Desktop Files\NLP\CodeSoft ML Internship\Movie\Genre Classification Dataset\test_data.txt'
train_path = r'C:\Users\rcjad\Desktop\Desktop Files\NLP\CodeSoft ML Internship\Movie\Genre Classification Dataset\train_data.txt'
test_sol_path = r'C:\Users\rcjad\Desktop\Desktop Files\NLP\CodeSoft ML Internship\Movie\Genre Classification Dataset\test_data_solution.txt'

Train = pd.read_csv(train_path,delimiter=':::',names=['Id','Title','Genre','Description'])
Validation = pd.read_csv(test_sol_path,delimiter=':::', names=['Id', 'Title', 'Genre', 'Description'])
Test = pd.read_csv(test_path,delimiter=":::", names=['Id','Title','Description'])
Genre_Category = Train['Genre'].unique()
print('------------------------------------------------------------------------------------')
print(f'Dataframe : \n\n{Train.tail(4)}') 
print('------------------------------------------------------------------------------------') 
print(f'Dataframe Shape : {Train.shape}') 
print('------------------------------------------------------------------------------------') 
print(f'Genre Unique Category : {len(Genre_Category)}')
print('------------------------------------------------------------------------------------') 

Label_Encoder = LabelEncoder()
Train['Label_Encoder'] = Label_Encoder.fit_transform(Train['Genre'])
Label_Encoder_unique = Train['Label_Encoder'].unique()
print(f'Label Encoder : {len(Label_Encoder_unique)}') 
print('------------------------------------------------------------------------------------') 

TFIDV = TfidfVectorizer(stop_words='english')
TFIDV.fit(Train['Description'])
Description_Vectorize = TFIDV.transform(Train['Description'])
pickle.dump(TFIDV,open('TFIDV.pkl','wb'))
print(f'Vectorization Done.....')

X = Description_Vectorize
y = Train['Genre'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
print('------------------------------------------------------------------------------------') 
print(f'X Train : {X_train.shape}')
print(f'Y Train : {y_train.shape}')
print(f'X Test : {X_test.shape}')
print(f'Y Test : {y_test.shape}')
print('------------------------------------------------------------------------------------') 

# Model Creation...
print('Logistic Regression...')
# Accuracy = 0.5702692733308742
Logistic_Regression = OneVsRestClassifier(LogisticRegression())
Logistic_Regression = Logistic_Regression.fit(X_train,y_train)
Logistic_Regression_Predict = Logistic_Regression.predict(X_test)
Logistic_Regression_Acc = accuracy_score(y_true=y_test, y_pred=Logistic_Regression_Predict)
print(f'Logsitic Regression Accuracy Rate : {Logistic_Regression_Acc}')
LR_Model = pickle.dump(Logistic_Regression, open("Movie_Genre_Prediction_Logistic_Regression_Model.pkl", 'wb'))
print('------------------------------------------------------------------------------------') 

print('KNeighborsClassifier')
# Accuracy = 0.3917373662855035
KNA = KNeighborsClassifier()
KNA = KNA.fit(X_train,y_train)
KNA_Prediction = KNA.predict(X_test)
KNA_Acc = accuracy_score(y_test, KNA_Prediction)
print(f'KNeighborsClassifier Accuracy Rate : {KNA_Acc}')
pickle.dump(KNA,open('Movie_Genre_Prediction_KNeighborsClassifier_Model.pkl','wb'))
print('------------------------------------------------------------------------------------') 
