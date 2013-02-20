#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
setting.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2013-02-21
'''
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

settings = dict(
    session_storage = 'dir://%s'%(os.path.join(ROOT_PATH, 'session')),
    template_path=os.path.join(os.path.dirname(__file__), "htm"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret = 'ol-ec*i2mk2_)&amp;9t**86b@#r-&amp;ry#ywj2m8k*@$vqiv2e4j-dx',
    xsrf_cookies=True,

)
