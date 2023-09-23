## Creation date: 14/3/2023
## Updated on 23/9/2023 (Added multi threading)
## Author: Shad0w-ops
## Purpose: Bruteforce Subdomains with Multithreading

# Importing Modules
import requests
import argparse
from termcolor import colored
import os
import time
import threading

# Defining Banner
banner = '''
     _____       __    ______                         
    / ___/__  __/ /_  / ____/_  __________  ___  _____
    \__ \/ / / / __ \/ /_  / / / /_  /_  / / _ \/ ___/
   ___/ / /_/ / /_/ / __/ / /_/ / / /_/ /_/  __/ /    
  /____/\__,_/_.___/_/    \__,_/ /___/___/\___/_/                                                             
)----------------------V1-------------------------(                                                 
 '''

# Lock to prevent concurrent printing
print_lock = threading.Lock()

# Function to check subdomain validity
def check_subdomain(domain, subdomain):
    url = f'http://{subdomain}.{domain}'
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            with print_lock:
                print(colored(f'[*] Valid subdomain: {url}', 'green'))
    except requests.exceptions.RequestException:
        pass

# Defining the main function
def main():
    parser = argparse.ArgumentParser(description='Find valid subdomains for a given domain')
    parser.add_argument('domain', help='Target domain')
    parser.add_argument('wordlist', help='Wordlist file containing subdomains')
    args = parser.parse_args()

    print("Starting subdomain fuzzing on " + args.domain)
    print(" ")
    time.sleep(3)

    try:
        with open(args.wordlist) as f:
            subdomains = [line.strip() for line in f]

        threads = []
        for subdomain in subdomains:
            t = threading.Thread(target=check_subdomain, args=(args.domain, subdomain))
            threads.append(t)
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()

    except KeyboardInterrupt:
        print("\nGoodbye!")

# Script start
if __name__ == '__main__':
    os.system("cls")
    print(colored(banner, 'red'))
    main()
