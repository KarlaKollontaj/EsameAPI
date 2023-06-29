from fastapi import FastAPI,Depends,HTTPException,status
from pydantic import BaseModel
import joblib
import uvicorn

app = FastAPI(title="API Startup", description="Esame API", version="1.0")

#insert the mean values of rdspend, administration and marketingspend as in the desribe
#of startup.ipnb, without comma
class StartupData(BaseModel):
    rdspend: float = 73721
    administration: float = 121344
    marketingspend: float = 211025

@app.on_event("startup")
def startup_event():
    global model
    model = joblib.load("Startup.pkl")
    print("model loaded")
    return model

@app.get("/")
def home():
    return {" ---->          http://localhost:8000/docs     <----------"}

@app.get("/predict")
async def predictget(data:StartupData=Depends()):
    try:
        X = [[data.rdspend, data.administration, data.marketingspend]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'prediction':res}
    except:
        raise HTTPException(status_code=404, detail="error")
    
@app.post("/predict")
async def predictpost(data:StartupData):
    try:
        X = [[data.rdspend, data.administration, data.marketingspend]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'prediction':res}
    except:
        raise HTTPException(status_code=404, detail="error")
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)