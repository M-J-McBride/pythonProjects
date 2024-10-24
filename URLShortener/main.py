from typing import Final
import requests

API_KEY: Final[str] = 'sk_2Z7zEnScnpkkNw8C'
base_url: Final[str] = 'https://api.short.io/links"'
domain = 'gls8.short.gy'

def shorten_link(full_link:str):
    payload: dict = {"domain": domain,
                     "originalURL": full_link,
                     "title" : 'NewTitleLink'}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        'Authorization': API_KEY
    }

    response = requests.post(base_url, headers=headers, json=payload)
    print(response.text)


def main():
    user_input: str = input('Enter a url: ')
    shorten_link(user_input)


if __name__ == '__main__':
    main()