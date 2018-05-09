import os
import platform
import subprocess

import cat_service


def main():
    print_header()
    folder = get_or_create_output_folder()
    # print('Found or created folder: ' + folder)
    download_cats(folder)
    display_cats(folder)

def print_header():
    print('-------------------------')
    print('      CAT FACTORY')
    print('-------------------------')
    print()


def get_or_create_output_folder():
    base_folder = os.path.abspath(os.path.dirname(__file__))
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)
    return full_path


def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count+1):
        name = 'cat_{}'.format(i)
        print('Downloading ' + name)
        cat_service.get_cat(folder, name)


def display_cats(folder):
    print(platform.system())
    print('Displaying cats in OS window')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xpg-open', folder])
    else:
        print('Sorry, we do not support your os: {}'.format(platform.system()))


if __name__ == '__main__':
    main()
