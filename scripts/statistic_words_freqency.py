#! /usr/bin/env python
# encoding:utf8
# vim: set ts=4 et sw=4 sts=4

"""
File: statistic_words_freqency.py
Author: "shanzi"
Email: "shanzi@diumoo.net"
Created At: 2013-05-30 22:31
Description: primary statistic of english words freq take place in tech-concerned website
"""

from  utils import env; env()

import re

import pymongo
from pymongo import MongoClient
from Stemmer import Stemmer
from searcher.ignorewords import EN as EN_IGNORE
from clint.textui import progress,colored


EN_WORD_CUT = re.compile(r"[^a-zA-Z]*")
client = MongoClient()
db = client.fetch_data

def run():
    stemmer = Stemmer("english")
    pages = db.en.find()
    print colored.yellow("statistic words") 
    wordstatistic = {}
    for page in progress.bar(pages,size=db.en.count()):
        data = page.get("data")
        if not data:continue
        content = data.get("content")
        if not content:
            db.en.remove({"_id":page["_id"]})
            continue
        words = EN_WORD_CUT.split(content)
        for word in words:
            w=stemmer.stemWord(word.strip()).lower()
            if w and len(w)<20 and not w in EN_IGNORE:
                if wordstatistic.get(w):
                    wordstatistic[w]+=1
                else:
                    wordstatistic[w]=1

    
    print colored.yellow("save to en_words_freq")
    savequene = []
    for k,v in progress.bar(wordstatistic.iteritems(),size=len(wordstatistic)):
        savequene.append({"_id":k,"freq":v})
        if len(savequene) >=1000:
            db.en_words_freq.insert(savequene)
            savequene=[]
        
    if savequene:db.en_words_freq.insert(savequene)
    print colored.cyan(
            "count of en_words_freq: %d" % db.en_words_freq.count())

if __name__=="__main__":
    run()

