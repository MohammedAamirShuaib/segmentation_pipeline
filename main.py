from fastapi import FastAPI, Request, Response
import uvicorn
import pandas as pd
import pickle
from pydantic import BaseModel
from typing import List
import json

class Item(BaseModel):
    Q1: int
    Q2: int
    Q3: int
    Q4: int
    Q5: int
    Q6: int
    Q7: int
    Q8: int
    Q9: int
    Q10: int
    Q11: int
    Q12: int
    Q13: int
    Q14: int
    Q15: int
    Q16: int
    Q17: int
    Q18: int
    Q19: int
    Q20: int
    Q21: int
    Q22: int
    Q23: int
    Q24: int
    Q25: int
    Q26: int
    Q27: int
    Q28: int


app = FastAPI()

@app.post("/prediction/")
async def predict(item: List[Item]):
    data = pd.DataFrame(columns=item[0].__dict__.keys())
    for i in item:
        data.loc[len(data)] = i.__dict__.values()
    model = pickle.load(open('Finalized_model/model.pkl', 'rb'))
    lables = model.predict(data)
    return lables.tolist()

