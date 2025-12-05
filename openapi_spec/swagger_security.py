swagger_security = {
    "securitySchemes": {
        "TokenAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Pass your token as: Token <your_token>"
        }
    }
}
