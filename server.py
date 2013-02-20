#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
server.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2013-02-21
'''
import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web

def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    print "start on port %s..."%options.port
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
