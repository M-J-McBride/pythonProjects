import string
import secrets
import pdb

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length: int = len(combination)
    new_password: str = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    if symbols & contains_symbols(new_password) == False:
        new_password[secrets.randbelow(length)] = secrets.choice(string.punctuation)
    if uppercase & contains_upper(new_password) == False:
        new_password[secrets.randbelow(length)] = secrets.choice(string.ascii_uppercase)

    return new_password

if __name__ == "__main__":
    for i in range(1,6):
        pdb.set_trace()
        new_pass: str = generate_password(4, True, True)
        specs: str = f'U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}'
        print(f'{i} -> {new_pass} ({specs})')