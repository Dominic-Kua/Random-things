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
