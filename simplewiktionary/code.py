import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
from typing import Iterator


HOST = 'https://simple.wiktionary.org'
STARTING_POINT = 'https://simple.wiktionary.org/w/index.php?title=Special:AllPages&hideredirects=1'
URL = 'https://simple.wiktionary.org/wiki/{0}'
REQUESTS_MAX_RETRIES = 3


class SimpleWiktionary:

    def __init__(self):
        """

        """
        self.session = requests.Session()

        self.session.mount("http://", requests.adapters.HTTPAdapter(max_retries=REQUESTS_MAX_RETRIES))
        self.session.mount("https://", requests.adapters.HTTPAdapter(max_retries=REQUESTS_MAX_RETRIES))
        self.list_of_words = []

    def get_list_of_defined_words(self, max_items=None)  -> Iterator:
        """

        :param max_items:
        :return:
        """
        return self.scrap_list_of_defined_words(STARTING_POINT, max_items=max_items, parsed_page=0,)

    def scrap_list_of_defined_words(self, url,  max_items=None, parsed_page=0):
        """
        Lisf of words on Simple.Wiktionary: recursive generator
        :param url:
        :return:
        """
        r = self.session.get(url)
        parsed_page += 1

        parser = BeautifulSoup(r.content, 'lxml')
        for a in parser.select('.mw-allpages-chunk  li a'):
            word = unquote(a['href'].replace('/wiki/', ''))

            if word not in self.list_of_words:
                if isinstance(max_items, int) and len(self.list_of_words) == max_items:
                    # raise StopIteration
                    return False

                self.list_of_words.append(word)
                yield word

        ''' Looking for the link to the next page (if there is some) '''
        nav_links = parser.select('.mw-allpages-nav a')
        if len(nav_links) == 2:
            if parsed_page > 1:
                raise StopIteration

            return self.scrap_list_of_defined_words('{0}{1}'.format(
                HOST,
                nav_links[0]['href']
            ), max_items, parsed_page)

        return self.scrap_list_of_defined_words(('{0}{1}'.format(
            HOST,
            nav_links[1]['href']
        ), max_items, parsed_page))

    def get_current_list_of_words(self) -> list:
        """

        :return:
        """
        return self.list_of_words

    def define(self, item) -> list:
        """

        :param item:
        :return:
        """
        answer = []

        r = self.session.get('{0}/wiki/{1}'.format(HOST, item))
        parser = BeautifulSoup(r.text, 'lxml')
        for d in parser.select('div#mw-content-text  ol  li'):
            try:
                d.dl.decompose()
            except AttributeError:
                pass

            definition = re.sub(r'\((.+?)\)', '', d.text)
            answer.append(definition.strip())

        return answer

