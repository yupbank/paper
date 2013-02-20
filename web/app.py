#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
app.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2013-02-21
'''
from .index import IndexHandler


handlers = [
        (r'/', IndexHandler),

        ]

def main():
    pass

if __name__ == '__main__':
    main()
