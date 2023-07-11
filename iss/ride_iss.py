#!/usr/bin/python3
"""Alta3 research - astros on ISSLAB 75"""

import urllib.request
import json

MAJORTOM = "http://api.open-notifu.org/astros.json"

def main():
    """reading json from api"""
    #call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)


    #strip off the attachment (JSON) and read it
    #the problem here, is that it will read out as a string
    helmet = groundctrl.read() 

    # show that at this point, our data is str 
    #we want to convert this to list / dict 
    print(helmet) 

    helmetson = json.loads(helmet.decode("utf-8"))
    # this should say bytes 
    print(type(helmet))



