#! /usr/bin/python3
import link_scanner
import unittest

class link_tests(unittest.TestCase):
	def test_url_checked(self):
		'''
		ensures that if a URL has already been checked, it isn't
		checked again
		'''
		url_list = ['www.bbc.co.uk']
		url = 'www.bbc.co.uk'
		self.assertEqual(link_scanner.url_checked(url, url_list),
						 (url_list, False))

	def test_url_not_checked(self):
		'''
		If it's not been checked then we need to add it to the
		list and get the "True" flag to check it.
		'''
		url_list = ['www.bbc.co.uk']
		url = 'www.cnn.com'
		self.assertEqual(link_scanner.url_checked(url, url_list),
						 (['www.bbc.co.uk', 'www.cnn.com'], True))

	def test_url_check_in_tld(self):
		'''
		This wouldn't help if it couldn't scan multiple pages within a site.
		So this checks that it doesn't.
		'''
		url_list = ['www.bbc.co.uk/sport']
		url = 'www.bbc.co.uk/news'
		self.assertEqual(link_scanner.url_checked(url, url_list),
						 (['www.bbc.co.uk/sport', 'www.bbc.co.uk/news'], True))






if __name__ == '__main__':
	unittest.main()
