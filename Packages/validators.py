import re

def phonenumbervalidator(number):
    pattern="^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$"
    if re.match(pattern,str(number)):
        return True
    else:
        return False
#phonenumbervalidator(8985485)

def emailvalidator(email):
    pattern="^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$"
    if re.match(pattern,email):
        return True
    return False
emailvalidator("_12nihadh@gmail.com")