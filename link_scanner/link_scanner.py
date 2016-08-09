#! /usr/bin/python3
'''
This will hopefully evolve into a nice little link scanner
which will pick up things like 403, 400 and hopeful 200s that show
an error message when they should be returning a 404.
'''
#I think this will be the main library I need,
#might add collections if I start to store the URLs in something funky like
#a deque
#if I thread it, and I might, it's going to end up needing asyncio I suspect.

import requests


def url_checked(url, url_list):
	'''
	Very simply, this function really only checks to see if
	a URL has already been requested. If it hasn't it
	adds it to the list and if it has then it doesn't
	Then it returns true or false depending on if it needs
	requesting or not.
	'''
	if url in url_list:
		return url_list , False
	else:
		url_list.append(url)
		return url_list , True
