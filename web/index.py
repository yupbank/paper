#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
index.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2013-02-21
'''
from base import BaseHandler
from setting import settings
from model import User
class IndexHandler(BaseHandler):
    def get(self):
        user = User("hello")
        return self.render('index.html', s=user)



if __name__ == '__main__':
    pass
