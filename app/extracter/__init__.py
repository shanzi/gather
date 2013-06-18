#! /usr/bin/env python
# encoding:utf8
# vim: set ts=4 et sw=4 sts=4

"""
File: __init__.py
Author: "shanzi"
Email: "shanzi@diumoo.net"
Created At: 2013-06-14 00:28
Description: extract content from html dom tree
"""
from extracter import Extracter

def extract(url,html=None):
    """extract content from webpage at specified url,
    if html isnot given, this function will fetch the html
    from the url itself

    :url: the url to extract content
    :html: optional param that give the html content of the url
    :returns: restructured html string contains the main content of url

    """
    # TODO: implement this function
    pass

def main():
    pass

if __name__=="__main__":
    main()

