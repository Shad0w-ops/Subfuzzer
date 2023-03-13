import requests
import argparse
from termcolor import colored
import os
import time

banner = '''
   _____       _         _                       _         ______                      
  / ____|     | |       | |                     (_)       |  ____|                     
 | (___  _   _| |__   __| | ___  _ __ ___   __ _ _ _ __   | |__ _   _ ___________ _ __ 
  \___ \| | | | '_ \ / _` |/ _ \| '_ ` _ \ / _` | | '_ \  |  __| | | |_  /_  / _ \ '__|
  ____) | |_| | |_) | (_| | (_) | | | | | | (_| | | | | | | |  | |_| |/ / / /  __/ |   
 |_____/ \__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_| |_|   \__,_/___/___\___|_| 

 --------------------------------------------------------------------------------------
 '''


def main():
    parser = argparse.ArgumentParser(description='Find valid subdomains for a given domain')
    parser.add_argument('domain', help='Target domain')
    parser.add_argument('wordlist', help='Wordlist file containing subdomains')
    args = parser.parse_args()

    print("Starting subdomain fuzzing on " + args.domain)
    print("--------------------------------------------")
    time.sleep(3)

    with open(args.wordlist) as f:
        subdomains = [line.strip() for line in f]

    valid_subdomains = []

    for subdomain in subdomains:
        url = f'http://{subdomain}.{args.domain}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(colored(f'[*] Valid subdomain: {url}', 'green'))
                valid_subdomains.append(url)
            else:
                print(f'{url} is not a valid subdomain')
        except requests.exceptions.RequestException:
            print(colored(f'{url} is not a valid subdomain', 'red'))

    if valid_subdomains:
        os.system("clear")
        print('\nValid subdomains found:')
        print('\n'.join(valid_subdomains))
    else:
        print('No valid subdomains found')

if __name__ == '__main__':
    os.system("clear")
    print(colored(banner, 'green'))
    main()
