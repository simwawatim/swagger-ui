from swagger_info import swagger_info
from swagger_security import swagger_security
from swagger_schemas import swagger_schemas
from swagger_paths import swagger_paths

custom_swagger = {
    **swagger_info,
    "components": {
        "securitySchemes": swagger_security["securitySchemes"],
        "schemas": swagger_schemas
    },
    "security": [{"TokenAuth": []}],
    "paths": swagger_paths
}
