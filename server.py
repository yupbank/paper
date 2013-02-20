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
from tornado.options import define, options
from web.app import handlers
from setting import settings

define("port", default=8000, help="run on the given port", type=int)
define("SINA_APP_KEY", default="3268956170", help="sina_app_key")
define("SINA_APP_SECRET", default="edb869b055dd6c3041999c30f4fbb6ed", help="SINA_APP_SECRET")

logger = logging.getLogger(__file__)

class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(handlers, **settings)

def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    print "start on port %s..."%options.port
    loop=tornado.ioloop.IOLoop.instance()

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
