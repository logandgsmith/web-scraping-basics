#!/usr/bin/env python3

import config
import requests

def scrape_subs(chan_id) -> int:
    """Scrapes the subs from YouTube API"""
    res = requests.get('https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics'
                       + '&id=' + chan_id + '&key=' + config.api_key)
    if res.status_code != 200:
        return -1
    else:
        return int(res.json()['items'][0]['statistics']['subscriberCount'])

def main():
    # Create a group from the HoloEN Members
    holo_myth_members = [
        ('Amelia Watson', 'UCyl1z3jo3XHR1riLFKG5UAg'),
        ('Calliope Mori', 'UCL_qhgtOy0dy1Agp8vkySQg'),
        ('Gura Gawr', 'UCoSrY_IQQVpmIRZ9Xf-y93g'),
        ('Ina\'nis Ninomae', 'UCMwGHR0BTZuLsmjY_NT5Pwg'),
        ('Kiara Takanashi', 'UCHsx4Hqa-1ORjQTh9TYDhww')
    ]

    # Scrape and display the subs of the channels
    print('Hololive Myth Sub Counts')
    for member in holo_myth_members:
        num_subs = scrape_subs(member[1])
        # Format over 1 Million subs
        if num_subs > 1000000: 
            num_subs = f'{num_subs / 1000000}M'
        # Format over 1 Thousand subs
        elif num_subs > 100000:
            num_subs = f'{num_subs // 1000}K'
        # New line for each member
        print(f'{member[0]} has {num_subs} subs.')

if __name__ == '__main__':
    main()
