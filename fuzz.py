## Creation date: 14/3/2023
## Author: Shad0w-ops
## Purpose: Bruteforce Subdomains


# Importing Modules
import requests
import argparse
from termcolor import colored
import os
import time
import sys

# Defining Banner
banner = '''
    _____       __    ________  __                   
   / ___/__  __/ /_  / ____/ / / /_______  ___  _____
   \__ \/ / / / __ \/ /_  / / / /_  /_  / / _ \/ ___/
  ___/ / /_/ / /_/ / __/ / /_/ / / /_/ /_/  __/ /    
 /____/\__,_/_.___/_/    \____/ /___/___/\___/_/     
)---------------------V1------------------------(                                              
 '''

# Defining the main function
def main():
    parser = argparse.ArgumentParser(description='Find valid subdomains for a given domain')
    parser.add_argument('domain', help='Target domain')
    parser.add_argument('wordlist', help='Wordlist file containing subdomains')
    args = parser.parse_args()

    print("  Starting subdomain fuzzing on " + args.domain)
    print(" ")
    time.sleep(3)

    try:
        with open(args.wordlist) as f:
            subdomains = [line.strip() for line in f]

        for subdomain in subdomains:
            url = f'http://{subdomain}.{args.domain}'
            sys.stdout.write(f"\rTrying {subdomain}")
            sys.stdout.flush()
            try:
                response = requests.get(url, timeout=3)
                if response.status_code == 200:
                    sys.stdout.write(f"\r{' ' * len(url)}\r")
                    print(colored(f'[*] Valid subdomain: {url}', 'green'))

                else:
                    sys.stdout.write(f"\r{' ' * len(url)}\r")
            except requests.exceptions.RequestException:
                sys.stdout.write(f"\r{' ' * len(url)}\r")
            sys.stdout.flush()

    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit()

# Script start
if __name__ == '__main__':
    os.system("clear")
    print(colored(banner, 'red'))
    main()
