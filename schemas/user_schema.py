add_user_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "email": {"type": "string"}
    },
    "required": ["username", "email"]
}

update_email_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string"}
    },
    "required": ["email"]
}
