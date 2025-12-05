swagger_paths = {
    "/api/method/erpnext.company-setup.setup.create_company_api": {
        "post": {
            "tags": ["Company Setup"],
            "summary": "Create a company",
            "requestBody": {
                "required": True,
                "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Company"}}}
            },
            "responses": {
                "201": {
                    "description": "Company created successfully",
                    "content": {
                        "application/json": {
                            "example": {
                                "status_code": "201",
                                "status": "success",
                                "message": "Company created successfully",
                                "data": {
                                    "id": "COMP-00123",
                                    "registrationNumber": "1202700022",
                                    "tpin": "999198881234",
                                    "companyName": "ZamTech Industries",
                                    "companyType": "Limited Liability",
                                    "companyStatus": "Active",
                                    "dateOfIncorporation": "2024-03-15",
                                    "industryType": "Manufacturing",
                                    "contactInfo": {
                                        "companyEmail": "company@example.com",
                                        "companyPhone": "+260211111111",
                                        "alternatePhone": "+260977777777",
                                        "contactPerson": "John Doe",
                                        "contactEmail": "contact@example.com",
                                        "website": "https://www.example.com",
                                        "contactPhone": "0978123456"
                                    },
                                    "address": {
                                        "addressLine1": "Plot 5678 Manda Hill Road",
                                        "addressLine2": "Block C, Third Floor",
                                        "city": "Lusaka",
                                        "district": "Lusaka",
                                        "province": "Lusaka Province",
                                        "postalCode": "10102",
                                        "country": "Zambia",
                                        "timeZone": "Africa/Lusaka"
                                    },
                                    "createdAt": "2025-12-05T08:45:12Z",
                                    "updatedAt": "2025-12-05T08:45:12Z"
                                }
                            }
                        }
                    }
                },
                "400": {"description": "Invalid input"}
            },
            "security": [{"TokenAuth": []}]
        }
    },
    "/api/method/erpnext.company-setup.setup.update_company_api": {
        "put": {
            "tags": ["Company Setup"],
            "summary": "Update a company",
            "parameters": [
                {
                    "name": "id",
                    "in": "query",
                    "required": True,
                    "schema": {"type": "string"},
                    "description": "The unique ID of the company"
                }
            ],
            "requestBody": {
                "required": True,
                "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Company"}}}
            },
            "responses": {
                "200": {
                    "description": "Company updated successfully",
                    "content": {
                        "application/json": {
                            "example": {
                                "status_code": "200",
                                "status": "success",
                                "message": "Company updated successfully",
                                "data": {
                                    "id": "COMP-00123",
                                    "registrationNumber": "1202700022",
                                    "tpin": "999198881234",
                                    "companyName": "ZamTech Industries",
                                    "companyType": "Limited Liability",
                                    "companyStatus": "Active",
                                    "dateOfIncorporation": "2024-03-15",
                                    "industryType": "Manufacturing"
                                }
                            }
                        }
                    }
                },
                "400": {"description": "Invalid input"},
                "404": {"description": "Company not found"}
            },
            "security": [{"TokenAuth": []}]
        }
    },
    "/api/method/erpnext.company-setup.setup.delete_company_api": {
        "delete": {
            "tags": ["Company Setup"],
            "summary": "Delete a company",
            "parameters": [
                {"name": "id", "in": "query", "required": True, "schema": {"type": "string"}}
            ],
            "responses": {
                "200": {"description": "Company deleted successfully"},
                "404": {"description": "Company not found"}
            },
            "security": [{"TokenAuth": []}]
        }
    },
    "/api/method/erpnext.company-setup.setup.get_companies_api": {
        "get": {
            "tags": ["Company Setup"],
            "summary": "Get all companies",
            "responses": {
                "200": {
                    "description": "List of companies",
                    "content": {
                        "application/json": {
                            "example": {
                                "status_code": "200",
                                "status": "success",
                                "message": "Companies retrieved successfully",
                                "data": [
                                    {
                                        "id": "COMP-00123",
                                        "registrationNumber": "1202700022",
                                        "taxId": "999198881234",
                                        "companyName": "ZamTech Industries",
                                        "companyType": "Limited Liability",
                                        "companyStatus": "Active",
                                        "dateOfIncorporation": "2024-03-15",
                                        "industryType": "Manufacturing"
                                    }
                                ]
                            }
                        }
                    }
                }
            },
            "security": [{"TokenAuth": []}]
        }
    },
    "/api/method/erpnext.company-setup.setup.get_company_api": {
        "get": {
            "tags": ["Company Setup"],
            "summary": "Get a single company",
            "parameters": [
                {"name": "id", "in": "query", "required": True, "schema": {"type": "string"}}
            ],
            "responses": {
                "200": {
                    "description": "Company found",
                    "content": {
                        "application/json": {
                            "example": {
                                "status_code": "200",
                                "status": "success",
                                "message": "Company created successfully",
                                "data": {
                                    "id": "COMP-00123",
                                    "registrationNumber": "1202700022",
                                    "tpin": "999198881234",
                                    "companyName": "ZamTech Industries",
                                    "companyType": "Limited Liability",
                                    "companyStatus": "Active",
                                    "dateOfIncorporation": "2024-03-15",
                                    "industryType": "Manufacturing",

                                    "contactInfo": {
                                    "companyEmail": "company@example.com",
                                    "companyPhone": "+260211111111",
                                    "alternatePhone": "+260977777777",
                                    "contactPerson": "John Doe",
                                    "contactEmail": "contact@example.com",
                                    "website": "https://www.example.com",
                                    "contactPhone": "0978123456"
                                    },

                                    "address": {
                                    "addressLine1": "Plot 5678 Manda Hill Road",
                                    "addressLine2": "Block C, Third Floor",
                                    "city": "Lusaka",
                                    "district": "Lusaka",
                                    "province": "Lusaka Province",
                                    "postalCode": "10102",
                                    "country": "Zambia",
                                    "timeZone": "Africa/Lusaka"
                                    },

                                    "createdAt": "2025-12-05T08:45:12Z",
                                    "updatedAt": "2025-12-05T08:45:12Z"
                                }
                            }
                        }
                    }
                },
                "404": {"description": "Company not found"}
            },
            "security": [{"TokenAuth": []}]
        }
    }
}
