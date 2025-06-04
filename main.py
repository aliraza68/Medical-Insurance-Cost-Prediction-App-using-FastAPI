# importing neessary libraries
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pickle
import pandas as pd

from user_input_schema import UserInput

# object of fastapi
app = FastAPI()

# loading the ml model
def load_trained_model():
    try:
        with open("ml_model/model.pkl", 'rb') as f:
            model = pickle.load(f)
            
            return model
    
    except FileNotFoundError as ex:
        print(f"Exception occurred in load_trained_model method: {ex}")
    except Exception as ex:
        print(f"Exception occurred: {ex}")

@app.get("/")
def index():
    return {"data":"Home Page"}

# post request
@app.post("/predict")
def predict_insurance_charges(data: UserInput):

    ml_model = load_trained_model()
    input_data_dict = {
        "age" : data.age,
        "sex": data.sex_int,
        "bmi": data.bmi,
        "children": data.children,
        "smoker": data.smoker_int,
        "region": data.region_int
    }

    input_df = pd.DataFrame([input_data_dict])
    print("The value of input_df:\n", input_df)

    # make inference from model
    prediction = ml_model.predict(input_df)[0]
    print("Model Prediction:", prediction)

    return JSONResponse(status_code = 200, 
                        content = {"Predicted_insurance_charges": prediction})
    

