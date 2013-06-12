#! /usr/bin/env python
# encoding:utf8
# vim: set ts=4 et sw=4 sts=4

"""
File: run.py
Author: "shanzi"
Email: "shanzi@diumoo.net"
Created At: 2013-06-12 23:25
Description: read config and start process
"""

from app import mainapp
import config

def main():
    mainapp.read_config(config)
    mainapp.start()

if __name__=="__main__":
    main()

