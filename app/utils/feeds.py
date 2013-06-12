#! /usr/bin/env python
# encoding:utf8
# vim: set ts=4 et sw=4 sts=4

"""
File: feeds.py
Author: "shanzi"
Email: "shanzi@diumoo.net"
Created At: 2013-06-10 00:36
Description: util function for feeds
"""


def retrieve_feed_url(url):
    """retrieve url of rss or atom feeds from general pages
    if the given url is already an url of rss or atom feed source
    this function simply returns the url, else it will tried to 
    fetch the url and parse the content and structure of html
    to find possible feed source url. 

    :url: an url of feed source or general pages
    :returns: the list of possible feed source urls

    """
    # TODO: implement this function
    pass
