import os

swagger_info = {
    "openapi": "3.0.0",
    "info": {
        "title": os.getenv("SWAGGER_TITLE", "Company Setup API"),
        "version": os.getenv("SWAGGER_VERSION", "1.0.0"),
        "description": os.getenv("SWAGGER_DESCRIPTION", "CRUD operations for companies and modules")
    },
    "servers": [
        {
            "url": os.getenv("SWAGGER_SERVER_URL", "https://erp.izyanehub.com/"),
            "description": os.getenv("SWAGGER_SERVER_DESC", "Production server")
        }
    ]
}
