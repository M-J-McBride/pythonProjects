def check_password(password: str):
    if len(password) == 0:
        return print('Please enter a password with at least 1 character')
    with open('passwords.txt','r') as file:
        common_passwords: list[str] = file.read().splitlines()

    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            return print(f'❌ {password} is common password #{i}')
        continue
    return print(f'Unique enough! ✅')

def main():
    check_password('')

if __name__ == '__main__':
    main()