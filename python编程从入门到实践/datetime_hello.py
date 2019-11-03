#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
#从datetime模块导入datetime类
now = datetime.now()
print(now)

t = 1429417200.0
print(datetime.fromtimestamp(t))

dt = datetime(2015,3,5,14,1)
print(dt)

#print(dt.timestamp())


