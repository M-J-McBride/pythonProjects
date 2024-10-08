import os
import requests

def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png','.jpeg','.jpg', '.gif','.svg']
    for ext in extensions:
        if ext in image_url:
            return ext

def download_image(image_url: str, name: str, folder: str = None):

    # give name and extension to image
    if ext := get_extension(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image extension could not be located......')

    # Check if name already exists
    if os.path.isfile(image_name):
        raise Exception('File name already exists....')

    #Download image
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{image_name}" sucessfully!')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    input_url:str = input('Input a url: ')
    input_name: str = input('Input a name for the image: ')

    print('Downloading...')
    download_image(input_url, input_name, folder = 'images')
    print('Complete')