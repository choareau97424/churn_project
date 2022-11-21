from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from schemas.customerSchema import CustomerSchema
from services import customer

security = HTTPBasic()

# Router declaration (replace the prefix if needed)
# Metadata for the swagger documentation
router = APIRouter(
    prefix="",
    tags=["CHURN"]
)


auth_obj = {
"william": "churn",
"christophe": "churn",
}


# The analytics route, receive the example input as body
# Then it uses the services to process thedataset

# Route for minimum dataset input
@router.get("/customer/churn", summary="API for returning profile of customer")
async def get_customer_data(customerSchema: CustomerSchema, credentials: HTTPBasicCredentials = Depends(security)):
    customer_data = []
    auth_obj_found = auth_obj.get(credentials.username, None)
    if not auth_obj_found:
        return {"error": True, "message": "user not found"}
    if auth_obj_found != credentials.password:
        return {"error": True, "message": "Password does not matched."}

    return {"error": False, "message": "data found", "data": customer_data}