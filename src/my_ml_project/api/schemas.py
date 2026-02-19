from pydantic import BaseModel

class LoanRequest(BaseModel):
    age: int
    job: str
    education: str
    housing: str
    loan: str
    marital: str
    contact: str
    previous: int
    poutcome: str
from pydantic import BaseModel

class LoanResponse(BaseModel):
    prediction: int
    probability: float

