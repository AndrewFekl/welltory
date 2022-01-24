VALIDATION_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "user_id": {"type": "integer"},
        "data": {
            "type": "object",
            "properties": {
                "x_data_type": {"type": "string"},
                "y_data_type": {"type": "string"},
                "x": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "date": {"type": "string", "format": "date"},
                            "value": {"type": "number"}
                        }
                    }
                },
                "y": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "date": {"type": "string", "format": "date"},
                            "value": {"type": "number"}
                        }
                    }
                }
            },
            "required": ["x_data_type", "y_data_type", "x", "y"]
        }
    },
    "required": ["user_id", "data"]
}

