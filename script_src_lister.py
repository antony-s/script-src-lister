#!/usr/bin/env python
import sys
from urlparse import urljoin

from bs4 import BeautifulSoup
import requests


class scriptSrcLister(object):

    def __init__(self, url):
        self.url = url
        self.srcs = []
        self.get_srcs()

    def get_srcs(self):
        if not self.url.startswith('http'):
            self.url = 'http://{}'.format(self.url)

        r = requests.get(self.url)

        soup = BeautifulSoup(r.text, 'html.parser')
        self.srcs = [
            script.get('src') for script in soup.find_all('script', src=True)
        ]

    def display_srcs(self):
        for src in self.srcs:
            if src.startswith('/') or src.startswith('.'):
                src = urljoin(self.url, src)
            print src

if __name__ == '__main__':
    script_src_lister = scriptSrcLister(sys.argv[1])
    script_src_lister.display_srcs()
