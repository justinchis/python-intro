#Author: Justin C
import random
# email: jsmitch@usc.edu, username: jsmith
def get_username(email):
    return email.split("@")[0]

def get_password(phrase):
    password = ""
    
    char_conversion = {
        "a":"@",
        "b":"8",
        "e":"3",
        "g":"9",
        "i":"!",
        "o":"0",
        "s":"$",
        "t":"7"
    }
    
    for letter in phrase:
        if letter.lower() in char_conversion:
            password += char_conversion[letter.lower()]
        else:
            password += maybe_capitalize(letter)
    return password + str(random.randint(0,100))

def maybe_capitalize(letter):
    if random.randint(0,2) == 0:
        return letter.upper()
    else:
        return letter.lower()
    

print("Password Generator: ")
email = input("Enter email: ")
phrase = input("Enter phrase: ")

username = get_username(email)
password = get_password(phrase)

print("UserName: " + username)
print("Password: " + password)
