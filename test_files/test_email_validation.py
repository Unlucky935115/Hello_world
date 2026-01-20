def test_valid_email():
    assert is_valid_email("test@example.com") == True

def test_invalid_email():
    assert is_valid_email("invalid-email") == False

def test_empty_email():
    assert is_valid_email("") == False

def is_valid_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None