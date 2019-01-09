# -*- coding: utf-8 -*-
#****************************************************************************
#*                                                                          *
#*  DatumTools WB for FreeCAD                                               *
#*  Copyright (c) 2018                                                      *
#*  Maurice easyw@katamail.com                                              *
#*                                                                          *
#*  DatumTools WB                                                           *
#*                                                                          *

import os, sys

def module_path():
    #return os.path.dirname(unicode(__file__, encoding))
    return os.path.dirname(__file__)
 
def abs_module_path():
    #return os.path.dirname(unicode(__file__, encoding))
    #return os.path.dirname(__file__)
    return os.path.realpath(__file__)
