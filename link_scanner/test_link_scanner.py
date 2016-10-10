#! /usr/bin/python3
import link_scanner
from link_scanner import scans
import unittest
from unittest import mock

BBC = """
	<HTML>
	<
	"""


def requests_mock(*args):
    '''
	Mocking requests.get and returning status_code
	for each site I call.
	Will need to be expanded for content for later, but that's a different
	test.
	'''

    class Mock_Response:
        def __init__(self, content, status_code):
            self.status_code = status_code
            self.content = content

    if args[0] == 'http://www.bbc.co.uk':
        return Mock_Response('correct', 200)
    elif args[0] == 'http://www.bbc.co.uk/skadjskaj':
        return Mock_Response('', 404)
    elif args[0] == 'http://www.bbc.co.uk/dihydrogenmonoxide':
        return Mock_Response('', 404)
    elif args[0] == 'http://www.bbc.co.uk/admin':
        return Mock_Response('', 403)
    elif args[0] == 'ftp://ftp.kua.org.uk':
        return Mock_Response('', 404)


class link_tests(unittest.TestCase):
    @mock.patch('requests.get', side_effect=requests_mock)
    def test_dead_links_returned(self, requests_mock):
        base_url = 'http://www.bbc.co.uk'
        dead_links = {'http://www.bbc.co.uk/dihydrogenmonoxide': 404, 'http://www.bbc.co.uk/admin': 403}
        self.assertEqual(link_scanner.main(base_url), dead_links)

    @mock.patch('requests.get', side_effect=requests_mock)
    def test_dead_links_correct(self, requests_mock):
        base_url = 'http://www.theregister.co.uk'
        fake_html = """
					<HTML>
					<a href='http://www.bbc.co.uk'>BBC</a>
					<img src='http://theregister.co.uk/header.jpg'>
					<a href='http://edition.cnn.com'>CNN</a>
					<a href='ftp://ftp.kua.org.uk'>this doesn't exist</a>
					</HTML>
					"""
        dead_links = {'ftp://ftp.kua.org.uk': 404}
        self.assertEqual(link_scanner.main(base_url), dead_links)

    @mock.patch('requests.get', side_effect=requests_mock)
    def test_base_url_working(self, requests_mock):
        '''
		test to make sure that the base_url is correct.
		If this doesn't return 200, we want to bail.
		'''
        base_url = 'http://www.bbc.co.uk'
        self.assertEqual(scans.base_url_checker(base_url), ('correct', True))

    @mock.patch('requests.get', side_effect=requests_mock)
    def test_base_url_not_working(self, requests_mock):
        '''
		Making certain that I bail early if the url is bad
		'''
        base_url = 'http://www.bbc.co.uk/skadjskaj'
        self.assertEqual(scans.base_url_checker(base_url), (None, False))

    def test_base_url_is_valid(self):
        '''
		last test showed me that I can't pass
		an invalid URL to requests, good to know
		'''
        base_url = 'gibberish'
        self.assertEqual(scans.base_url_checker(base_url), (None, False))

    def test_urls_gathered_from_html(self):
        '''
		testing that the super simple parser will
		harvest only links and not images or other resources
		It should also not pick up non-link URLs
		'''
        fake_html = '''
					<HTML>
					<a href='http://www.bbc.co.uk/news'>news</a><p>
					This is a new line<p>
					<a href='http://www.bbc.co.uk/sport'>www.bbc.co.uk/sport</a>
					<a href='https://www.google.com'>google</a>
					<img src='http://wwww.bbc.co.uk/fake_image.jpeg'>
					</HTML>
					'''

        url_list = ['http://www.bbc.co.uk/news', 'http://www.bbc.co.uk/sport', 'https://www.google.com']
        base_url = 'http://www.bbc.co.uk'
        self.assertEqual(scans.url_parser(base_url, fake_html), url_list)

    @mock.patch('requests.get', side_effect=requests_mock)
    def test_url_retrieved_on_200(self, requests_mock):
        '''
		ensure that if a url returns 200, we also pull the content
		will extend base_url_checker and the requests_mock for this
		'''
        base_url = 'http://www.bbc.co.uk'
        fake_content = 'correct'
        self.assertEqual(scans.base_url_checker(base_url), (fake_content, True))


if __name__ == '__main__':
    unittest.main()
