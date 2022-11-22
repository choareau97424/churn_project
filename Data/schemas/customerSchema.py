from pydantic import BaseModel

class CustomerSchema(BaseModel):
    gender: str=None
    seniorcitizen: int = None
    partner: str = None
    dependents: str = None
    tenure: int = None
    phoneservice: str = None
    multiplelines: str = None
    internetservice: str = None
    onlinesecurity: str = None
    onlinebackup: str = None
    deviceprotection: str = None
    techsupport: str = None
    streamingtv: str = None
    streamingmovies: str = None
    contract:str = None
    paperlessbilling: str = None
    paymentmethod: str = None
    monthlycharges: float = None
    totalcharges: float = None
    Churn: str = None
