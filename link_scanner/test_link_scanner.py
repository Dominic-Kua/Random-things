#! /usr/bin/python3
import link_scanner
import unittest

class link_tests(unittest.TestCase):
	def test_dead_links_returned(self):
		base_url = "www.bbc.co.uk"
		dead_links = {"www.bbc.co.uk/dihydrogenmonoxide": 404, "www.bbc.co.uk/admin": 403}
		self.assertEqual(link_scanner.main(base_url), dead_links)



if __name__ == '__main__':
	unittest.main()
