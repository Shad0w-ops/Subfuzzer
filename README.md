# Subfuzz
## Disclaimer: Made for educational purposes only i will not be held responsible for any missuse of this tool.

## Installation:

    git clone https://github.com/Shad0w-ops/Subfuzzer.git
    
    cd Subfuzz  
 
    pip3 install -r requirements.txt
  
## Usage:

    python3 fuzz.py domain /path/to/wordlist.txt
   you can either use the wordlists that are supplied with the tool or use any wordlist you want.
   
## Example:
    
    python3 fuzz.py website.com Wordlists/subdomains-top1mil-20000.txt
    
    
the output will show 2 colors (Green and Red) Green indicating that the subdomain is valid and Red refering otherwise.
after iterating through the entire wordlist, the output of only the valid subdomains will be listed.
