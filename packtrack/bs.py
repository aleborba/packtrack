import functools

try:
    from bs4 import BeautifulSoup
    BeautifulSoup = functools.partial(BeautifulSoup, features="lxml")
except ImportError:
    from BeautifulSoup import BeautifulSoup

BeautifulSoup = BeautifulSoup
