#! /usr/bin/env python
# encoding:utf8
# vim: set ts=4 et sw=4 sts=4

"""
File: utils.py
Author: "shanzi"
Email: "shanzi@diumoo.net"
Created At: 2013-06-02 00:17
Description: prepare python path for all project
"""
import sys
import os


def env():
    path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.join(path,os.path.pardir))
