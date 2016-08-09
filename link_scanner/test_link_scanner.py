#! /usr/bin/python3
import link_scanner
import unittest

class link_tests(unittest.TestCase):
	def test_dead_links_returned(self):
		base_url = "http://www.bbc.co.uk"
		dead_links = {"http://www.bbc.co.uk/dihydrogenmonoxide": 404, "http://www.bbc.co.uk/admin": 404}
		self.assertEqual(link_scanner.main(base_url), dead_links)

	def test_base_url_works(self):
		'''
		test to make sure that the base_url is correct.
		'''
		base_url = "http://www.bbc.co.uk"
		assert link_scanner.base_url_checker(base_url) == True

	def test_base_url_not_working(self):
		'''
		Making certain that I bail early if the url is bad
		'''
		base_url = "http://www.bbc.co.uk/skadjskaj"
		assert link_scanner.base_url_checker(base_url) == False

	def test_base_url_is_valid(self):
		'''
		last test showed me that I can't pass
		an invalid URL to requests, good to know
		'''
		base_url = "gibberish"
		assert link_scanner.base_url_checker(base_url) == False



if __name__ == '__main__':
	unittest.main()
