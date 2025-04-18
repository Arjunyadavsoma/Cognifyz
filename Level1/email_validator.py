import re

def valid_mail(email):
    local_allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'*+/=?^_`{|}~.-"
    domain_allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-."
    
    if email.count('@') != 1:
        print(f"{email} is not a valid email")
        return False
    
    username, domain = email.split('@')
    
    if not username or not domain:
        print(f"{email} is not a valid email")
        return False
    
    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        print(f"{email} is not a valid email")
        return False
    
    if '..' in domain or '..' in username:
        print(f"{email} is not a valid email")
        return False
    
    if '_' in domain or '+' in domain:
        print(f"{email} is not a valid email")
        return False


    for part in domain.split('.'):
        if not part or part.startswith('-') or part.endswith('-'):
            print(f"{email} is not a valid email")
            return False
        for ch in part:
            if ch not in domain_allowed:
                print(f"{email} is not a valid email")
                return False

    for ch in username:
        if ch not in local_allowed:
            print(f"{email} is not a valid email")
            return False

    print(f"{email} is a valid email")
    return True

email=input("Enter a email to chech : ")
valid_mail(email)