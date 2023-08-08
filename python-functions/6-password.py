def validate_password(password):
    is_long = len(password) >= 8
    has_upper = any(i.isupper() for i in password)
    has_lower = any(i.islower() for i in password)
    has_digit = any(i.isdigit() for i in password)
    no_spaces = ' ' not in password
    if all([is_long, has_upper, has_lower, has_digit, no_spaces]):
        return True
    return False