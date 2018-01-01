#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('中文测试正常')
name=input('please enter your name: ')
print('hello, %s' % name)
age=int(input('please enter your age: '))
if age>=6:
	print('teenager')
elif age>=18:
	print('adult')
else:
	print('kid')
	