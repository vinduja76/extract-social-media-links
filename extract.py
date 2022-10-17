# -*- coding: utf-8 -*-

"""
title           :extract social media handles
author          :Vinduja K B
date            :Mon Oct 17,2022
version         :1.0
usage           :extract social media handles given input as url
python_version  :3.6
encoding        :UTF-8
"""

import requests
from html_to_etree import parse_html_bytes
from extract_social_media import find_links_tree

#Global Variable. This list contains the social media handle links to be extracted
SOCIAL_MEDIA = ['facebook', 'linkedin', 'twitter']


def extract(url):   
    """
    Description: Function to social media links 
    Input      : Url
    Return     : Dict containing social media as key and value as the links
    """
    try:
        res = requests.get(url)
        tree = parse_html_bytes(res.content, res.headers.get('content-type'))
        result = {}
        for link in set(find_links_tree(tree)):
            key = [value for value in SOCIAL_MEDIA if value in link]
            if len(key) == 0: continue
            result[key[0]] = link
        return result
    except Exception as error:
        #print(f'Exception occurred in extract: {error}')
        return None

if __name__ == '__main__':
    # testcases = ['https://techcrunch.com/contact/', \
    #              'https://give.do/',]
    # for url in testcases:
    #     result = extract(url)
    url = 'https://give.do/'
    print(extract(url))
