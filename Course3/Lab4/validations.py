#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    for i in range(1,len(username)):
        if username[0] == username[i]:
            return False
    return True


print(validate_user("priya",3))
print(validate_user("priya.pri",3))
print(validate_user("lakshmi",3))
print(validate_user("lakshmi.la",3))
print(validate_user("zoho",1))
