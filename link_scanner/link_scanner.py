#! /usr/bin/python3
'''
This will hopefully evolve into a nice little link scanner
which will pick up things like 403, 400 and hopeful 200s that show
an error message when they should be returning a 404.
'''
#I think these two will be the main libraries I need,
#might add collections if I start to store the URLs in something funky like
#a named tuple.
import requests


def url_fetcher(url):
    '''
    This will take the input URL and scan through the sub-domains
    returning a list of them.
    '''
    pass
