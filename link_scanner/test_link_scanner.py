#! /usr/bin/python3
import link_scanner
import unittest

class link_tests(unittest.TestCase):
	def test_url_checked(self):
		url_list = ['www.bbc.co.uk']
		url_response = 'www.bbc.co.uk'
		self.assertEqual(link_scanner.url_checked(url_response, url_list), (url_list, False))

	def test_url_not_checked(self):
		url_list = ['www.bbc.co.uk']
		url_response = 'www.cnn.com'
		self.assertEqual(link_scanner.url_checked(url_response, url_list), (['www.bbc.co.uk', 'www.cnn.com'], True))

	def test_url_check_in_tld(self):
		url_list = ['www.bbc.co.uk/sport']
		url_response = 'www.bbc.co.uk/news'
		self.assertEqual(link_scanner.url_checked(url_response, url_list), (['www.bbc.co.uk/sport', 'www.bbc.co.uk/news'], True))



if __name__ == '__main__':
	unittest.main()