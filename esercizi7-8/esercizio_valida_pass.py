import re

def valida_password(password):

    pattern = re.compile(r"""
                         ^
                         (?=.*[A-Z])
                         (?=.*[a-z])
                         (?=.*\d)
                         (?=.*[@#$%^&+=])
                         (?=\S+$)
                         .{8,16}
                         $
                         """, re.VERBOSE)
    corrispondenza = pattern.search(password)

    if corrispondenza:
        return True
    
    else:
        return False
    

password1 = "Password1@"
password2 = "abc123"

print(valida_password(password1))
print(valida_password(password2))