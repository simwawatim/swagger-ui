swagger_schemas = {
    "Modules": {
        "type": "object",
        "properties": {
            "accounting": {"type": "boolean"},
            "crm": {"type": "boolean"},
            "hr": {"type": "boolean"},
            "inventory": {"type": "boolean"},
            "procurement": {"type": "boolean"},
            "sales": {"type": "boolean"},
            "supplierManagement": {"type": "boolean"}
        }
    },
    "Company": {
        "type": "object",
        "example": {
            "registrationNumber": "1202700022",
            "tpin": "999198881234",
            "companyName": "ZamTech Industries",
            "companyType": "Limited Liability",
            "companyStatus": "Active",
            "dateOfIncorporation": "2024-03-15",
            "industryType": "Manufacturing",
            "contactInfo": {
                "companyEmail": "info@zamtech.com",
                "companyPhone": "+260211111111",
                "alternatePhone": "+260977777777",
                "contactPerson": "John Doe",
                "contactEmail": "contact@zamtech.com",
                "website": "https://www.zamtech.com",
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
            "bankAccounts": [
                {
                    "accountNo": "1234567890",
                    "accountHolderName": "John Doe",
                    "bankName": "HDFC Bank",
                    "swiftCode": "HDFCINBBXXX",
                    "sortCode": "12-34-56",
                    "branchAddress": "123 MG Road, Mumbai",
                    "currency": "INR",
                    "dateAdded": "2025-12-05",
                    "openingBalance": 0.0
                }
            ],
            "financialConfig": {"baseCurrency": "INR", "financialYearStart": "April"},
            "accountingSetup": {
                "chartOfAccounts": "Standard COA",
                "defaultExpenseGL": "5000-001",
                "fxGainLossAccount": "7500-001",
                "revaluationFrequency": "Monthly",
                "roundOffAccount": "6800-001",
                "roundOffCostCenter": "CC-001",
                "depreciationAccount": "6500-001",
                "appreciationAccount": "4500-001"
            },
            "terms": {},
            "modules": {
                "accounting": True,
                "crm": True,
                "hr": True,
                "inventory": True,
                "procurement": True,
                "sales": True,
                "supplierManagement": False
            },
            "documents": {"companyLogoUrl": "/uploads/logo.png", "authorizedSignatureUrl": "/uploads/signature.png"},
            "templates": {"invoiceTemplate": "template1", "quotationTemplate": "template2", "rfqTemplate": "template3"}
        }
    }
}
