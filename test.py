#coding:utf-8

import sys

sys.path.append('./ai/')
sys.path.append('./interface/')

import wgobject, wgruler, wgsdata, common
import __wginterface as wginterface
import random,time,sys
sys.path.append('../interface/')

obj_interface = wginterface.AI_InterFace()
dic_metadata = obj_interface.getSimTime()
print(dic_metadata)