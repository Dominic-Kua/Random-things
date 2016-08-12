#! /usr/bin/python3
import link_scanner
from link_scanner import scans
import unittest
from unittest import mock

def requests_mock(*args):
	class Mock_Response:
		def __init__ (self, status_code):
			#self.content = content
			self.status_code = status_code
	if args[0] == 'http://www.bbc.co.uk':
		return Mock_Response(200)
	else:
		return Mock_Response(404)


class link_tests(unittest.TestCase):
	def test_dead_links_returned(self):
		base_url = "http://www.bbc.co.uk"
		dead_links = {"http://www.bbc.co.uk/dihydrogenmonoxide": 404, "http://www.bbc.co.uk/admin": 404}
		self.assertEqual(link_scanner.main(base_url), dead_links)

	@mock.patch('requests.get', side_effect=requests_mock)
	def test_base_url_working(self, requests_mock):
		mock_scans = scans()
		'''
		test to make sure that the base_url is correct.
		If this doesn't return 200, we want to bail.
		'''
		base_url = 'http://www.bbc.co.uk'
		assert scans.base_url_checker(base_url) == True

	def test_base_url_not_working(self):
		'''
		Making certain that I bail early if the url is bad
		'''
		base_url = "http://www.bbc.co.uk/skadjskaj"
		assert scans.base_url_checker(base_url) == False

	def test_base_url_is_valid(self):
		'''
		last test showed me that I can't pass
		an invalid URL to requests, good to know
		'''
		base_url = "gibberish"
		assert scans.base_url_checker(base_url) == False



if __name__ == '__main__':
	unittest.main()
