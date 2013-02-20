#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
base.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2013-02-21
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///foo.db', echo=True)
Base = declarative_base()
def main():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
