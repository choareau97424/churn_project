import uvicorn
from fastapi import FastAPI
from routers import customer_router, root_router


# Metadata for the swagger documentation for each endpoint
tags_metadata = [
    {
        "name": "churn",
        "description": "All endpoints related to Customer"
    },
    {
        "name": "Root",
        "description": "Root endpoint"
    }
]


# API description
description = "API for Returning customer profile and where this customer churn"


# FastAPI initialization and metadata for the documentation
app = FastAPI(
    root_path="/",
    title="CHURN",
    description=description,
    version="0.1.0",
    contact={
        "name": "william & Christophe",
        "email": "w.siounandan@gmail.com"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "hhtps://www.apache.org/license/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)


# Include routers
# router to root endpoint
app.include_router(root_router.router) # for root

# router for exams endpoint
app.include_router(customer_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)