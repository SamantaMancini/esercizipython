import re

def valida_indirizzo_email(email):
    pattern = re.compile(r"""
                         ^
                         [\w\.-]+
                         @
                         ([\w-]+\.)+
                         [a-zA-Z]{2,}
                         $
                         """, re.VERBOSE)

    corrispondenza = pattern.search(email)

    if corrispondenza:
        return True
    else:
        return False
    
email1 = "example@example.com"
email2 = "example@123.456.789"

print(valida_indirizzo_email(email1))
print(valida_indirizzo_email(email2))