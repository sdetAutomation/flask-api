invalid_post_error_msg_users = {
    "error": "Invalid request",
    "helpString": "Example: {'username': 'thor', 'email': 'thor@gmail.com'}"
}

invalid_put_error_msg_users = {
    "error": "Invalid request",
    "helpString": "Example: {'email': 'thor@gmail.com'}"
}

invalid_delete_error_msg_users = {
    "error": "User not found, unable to delete."
}

invalid_delete_error_msg_locations = {
    "error": "Location not found, unable to delete."
}


def error_message_helper(msg):
    return '{ "error": "' + msg + '."}'


class ErrorMessages:
    pass
