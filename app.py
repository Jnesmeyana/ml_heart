# 1. Library imports
import uvicorn
from fastapi import FastAPI
from person_data import Heart
import numpy as np
import pickle
import pandas as pd

#from fastapi.templating import Jinja2Templates
#templates = Jinja2Templates(directory="app")

# 2. Create the app object
app = FastAPI()
pickle_in = open("best_clf.pkl","rb")
classifier=pickle.load(pickle_in)


# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Проверка на сердечные заболевания'}


# 4. Expose the prediction functionality, make a prediction 
#    JSON data and return the predicted  with the confidence
@app.post('/predict')
def predict(data:Heart):
    data = data.dict()
    age=data['age']
    sex=data['sex']
    cp=data['cp']
    trestbps=data['trestbps']
    chol=data['chol']
    fbs=data['fbs']
    restecg=data['restecg']
    thalach=data['thalach']
    exang=data['exang']
    oldpeak=data['oldpeak']
    slope=data['slope']
    cav=data['cav']
    thal=data['thal']

   #print(classifier.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,cav,thal]]))
    prediction = classifier.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,cav,thal]])
    if(prediction[0]==1):
        pred="Имеется сердечное заболевание"
    else:
        pred="Здоровое сердце"
    return {
        'prediction': pred
    }

# 5. Run the API with uvicorn   
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload 