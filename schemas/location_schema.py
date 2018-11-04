add_location_schema = {
    "type": "object",
    "properties": {
        "state": {"type": "string"},
        "capital": {"type": "string"}
    },
    "required": ["state", "capital"]
}

update_capital_schema = {
    "type": "object",
    "properties": {
        "capital": {"type": "string"}
    },
    "required": ["capital"]
}
