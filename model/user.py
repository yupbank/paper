#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
user.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2013-02-21
'''
from base import Base
from sqlalchemy import Table, Column, Integer, String

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init(self, name):
        self.name = name
    
    def __repr__(self):
        return '<User: %s >'%self.name

def main():
    pass

if __name__ == '__main__':
    main()
