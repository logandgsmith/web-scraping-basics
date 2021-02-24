#!/usr/bin/env python3

import requests
import bs4

def main():
    # Attempt to get a specified page
    res = requests.get('https://drop.com/mechanical-keyboards/home')

    # Check if the response is 200 (OK)
    if res.status_code != 200:
        print(res) # This will print the response code
        return

    # Print the raw text of the response. Uncomment if curious.
    #print(res.text)

    # Setup the Beautiful Soup parser. Uncomment if curious.
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #print(soup.prettify())

    # Print all of the links on a page
    for link in soup.find_all('a'):
        print(link.get('href'))

if __name__ == '__main__':
    main()
