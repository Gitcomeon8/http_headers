#!/usr/bin/python

import requests
import json

class x:

    def __init__(self,url,domen):
        with open(domen,'r') as a:
            self.xx = a.readlines()
            for y in self.xx:
                try:
                    self.str = y.strip()
                    self.get = requests.get(url.format(self.str)).text
                    print (f'[*]result from {self.str.upper()}');print(self.get)

                except Exception as er:
                    print(f'[!]{er}')
                    exit()





inp = input('masukan domen.txt: ')
x('https://api.hackertarget.com/dnslookup/?q={}',inp)
