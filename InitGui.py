# -*- coding: utf-8 -*-
#****************************************************************************
#*                                                                          *
#*  DatumTools WB for FreeCAD                                               *
#*  Copyright (c) 2018                                                      *
#*  Maurice easyw@katamail.com                                              *
#*                                                                          *
#*  DatumTools WB                                                           *
#*                                                                          *
#****************************************************************************

DT_wb_version='v 1.0.0'

import FreeCAD, FreeCADGui, Part, os, sys
import re, time

if (sys.version_info > (3, 0)):  #py3
    import urllib
    from urllib import request, error #URLError, HTTPError
else:  #py2
    import urllib2
    from urllib2 import Request, urlopen, URLError, HTTPError
    
import dt_locator
from DatumToolsCMD import *

DatumToolsWBpath = os.path.dirname(dt_locator.__file__)
DatumToolsWB_icons_path =  os.path.join(DatumToolsWBpath, 'Resources', 'icons')

global main_DWB_Icon
main_DTWB_Icon = os.path.join(DatumToolsWB_icons_path , 'DatumTools-icon.svg')


#try:
#    from FreeCADGui import Workbench
#except ImportError as e:
#    FreeCAD.Console.PrintWarning("error")
    
class DatumToolsWB ( Workbench ):
    global main_DTWB_Icon, DT_wb_version
    
    "DatumTools WB object"
    Icon = main_DTWB_Icon
    #Icon = ":Resources/icons/kicad-StepUp-tools-WB.svg"
    MenuText = "DatumTools WB"
    ToolTip = "DatumTools workbench"
 
    def GetClassName(self):
        return "Gui::PythonWorkbench"
    
    def Initialize(self):
        
        self.appendToolbar("Datum Tools", ["DatumPoint","DatumLine","DatumPlane","DatumLCS","AltLCS","Plane","AnnoLbl"])  #"Point","Line",
        
        #self.appendMenu("ksu Tools", ["ksuTools","ksuToolsEdit"])
        self.appendMenu("Datum Tools", ["DatumPoint","DatumLine","DatumPlane","DatumLCS","AltLCS","Plane","AnnoLbl"])
        
        Log ("Loading DatumTools Module... done\n")
 
    def Activated(self):
                # do something here if needed...
        Msg ("DatumTools WB Activated("+DT_wb_version+")\n")
        from PySide import QtGui
        import time
        

    def Deactivated(self):
                # do something here if needed...
        Msg ("DatumTools WB Deactivated()\n")
    
###

FreeCADGui.addWorkbench(DatumToolsWB)
