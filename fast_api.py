import pandas as pd
import alert_email
import uvicorn
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    
    return {"message": ""}

@app.get("/{departure}/{destination}{date}")
async def test_query(departure, destination,date,price):
    
    return {"result": alert_email(departure, destination, date,"563186832@qq.com", "Go buy tickets!", price, server='smtp.example.cn',
              from_email='563186832wayne@example.com')}

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0")

