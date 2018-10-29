def validate_user_object(user_object):
    if "username" in user_object and "email" in user_object:
        return True
    else:
        return False


def validate_put_request_object(user_object):
    if "email" in user_object:
        return True
    else:
        return False
