# -*- coding: utf-8 -*-
#****************************************************************************
#*                                                                          *
#*  Kicad STEPUP (TM) (3D kicad board and models to STEP) for FreeCAD       *
#*  3D exporter for FreeCAD                                                 *
#*  Kicad STEPUP TOOLS (TM) (3D kicad board and models to STEP) for FreeCAD *
#*  Copyright (c) 2015                                                      *
#*  Maurice easyw@katamail.com                                              *
#*                                                                          *
#*  Kicad STEPUP (TM) is a TradeMark and cannot be freely useable           *
#*                                                                          *

import FreeCAD, FreeCADGui, Part, os
import imp, os, sys, tempfile
import FreeCAD, FreeCADGui
from PySide import QtGui, QtCore
import dt_locator


reload_Gui=False#True

def reload_lib(lib):
    if (sys.version_info > (3, 0)):
        import importlib
        importlib.reload(lib)
    else:
        reload (lib)

DatumToolsWBpath = os.path.dirname(dt_locator.__file__)
DatumToolsWB_icons_path =  os.path.join(DatumToolsWBpath, 'Resources', 'icons')

class DatumPlane:
    "datum tools object"
 
    def GetResources(self):
        return {'Pixmap'  : os.path.join( DatumToolsWB_icons_path , 'DatumPlane.svg') , # the name of a svg file available in the resources
                     'MenuText': "Datum Plane" ,
                     'ToolTip' : "Datum Plane\nDatumTools workbench"}
 
    def IsActive(self):
        if FreeCAD.ActiveDocument is not None:
            import os, sys
            return True
 
    def Activated(self):
        # do something here...
        sel = FreeCADGui.Selection.getSelection()
        if len (sel) == 1:
            if 'App::Part' in sel[0].TypeId or 'PartDesign::Body' in sel[0].TypeId \
                    or 'Part::FeaturePython' in sel[0].TypeId:
                try:
                    sel[0].newObject('PartDesign::Plane','DatumPlane')
                except:
                    FreeCAD.ActiveDocument.addObject('PartDesign::Plane','DatumPlane')
            else:
                FreeCAD.ActiveDocument.addObject('PartDesign::Plane','DatumPlane')
        else:
            FreeCAD.ActiveDocument.addObject('PartDesign::Plane','DatumPlane')
        
        FreeCAD.ActiveDocument.recompute()
        #FreeCAD.Console.PrintWarning( 'Done :)\n' )
        
FreeCADGui.addCommand('DatumPlane',DatumPlane())
##
class DatumLine:
    "datum tools object"
 
    def GetResources(self):
        return {'Pixmap'  : os.path.join( DatumToolsWB_icons_path , 'DatumLine.svg') , # the name of a svg file available in the resources
                     'MenuText': "Datum Line" ,
                     'ToolTip' : "Datum Line\nDatumTools workbench"}
 
    def IsActive(self):
        if FreeCAD.ActiveDocument is not None:
            import os, sys
            return True
 
    def Activated(self):
        # do something here...
        sel = FreeCADGui.Selection.getSelection()
        if len (sel) == 1:
            if 'App::Part' in sel[0].TypeId or 'PartDesign::Body' in sel[0].TypeId \
                    or 'Part::FeaturePython' in sel[0].TypeId:
                try:
                    sel[0].newObject('PartDesign::Line','DatumLine')
                except:
                    FreeCAD.ActiveDocument.addObject('PartDesign::Line','DatumLine')
            else:
                FreeCAD.ActiveDocument.addObject('PartDesign::Line','DatumLine')
        else:
            FreeCAD.ActiveDocument.addObject('PartDesign::Line','DatumLine')
        
        FreeCAD.ActiveDocument.recompute()
        #FreeCAD.Console.PrintWarning( 'Done :)\n' )
        
FreeCADGui.addCommand('DatumLine',DatumLine())
##
class DatumPoint:
    "defeaturing tools object"
 
    def GetResources(self):
        return {'Pixmap'  : os.path.join( DatumToolsWB_icons_path , 'DatumPoint.svg') , # the name of a svg file available in the resources
                     'MenuText': "Datum Point" ,
                     'ToolTip' : "Datum Point\nDatumTools workbench"}
 
    def IsActive(self):
        if FreeCAD.ActiveDocument is not None:
            import os, sys
            return True
 
    def Activated(self):
        # do something here...
        sel = FreeCADGui.Selection.getSelection()
        if len (sel) == 1:
            if 'App::Part' in sel[0].TypeId or 'PartDesign::Body' in sel[0].TypeId \
                    or 'Part::FeaturePython' in sel[0].TypeId:
                try:
                    sel[0].newObject('PartDesign::Point','DatumPoint')
                except:
                    FreeCAD.ActiveDocument.addObject('PartDesign::Point','DatumPoint')
            else:
                FreeCAD.ActiveDocument.addObject('PartDesign::Point','DatumPoint')
        else:
            FreeCAD.ActiveDocument.addObject('PartDesign::Point','DatumPoint')
        
        FreeCAD.ActiveDocument.recompute()
        #FreeCAD.Console.PrintWarning( 'Done :)\n' )
        
FreeCADGui.addCommand('DatumPoint',DatumPoint())
##
class DatumLCS:
    "datum tools object"
 
    def GetResources(self):
        return {'Pixmap'  : os.path.join( DatumToolsWB_icons_path , 'DatumLCS.svg') , # the name of a svg file available in the resources
                     'MenuText': "Datum LCS" ,
                     'ToolTip' : "Datum LCS\nDatumTools workbench"}
 
    def IsActive(self):
        if FreeCAD.ActiveDocument is not None:
            import os, sys
            return True
 
    def Activated(self):
        # do something here...
        sel = FreeCADGui.Selection.getSelection()
        if len (sel) == 1:
            if 'App::Part' in sel[0].TypeId or 'PartDesign::Body' in sel[0].TypeId \
                    or 'Part::FeaturePython' in sel[0].TypeId:
                try:
                    sel[0].newObject('PartDesign::CoordinateSystem','LCS')
                except:
                    FreeCAD.ActiveDocument.addObject('PartDesign::CoordinateSystem','LCS')
            else:
                FreeCAD.ActiveDocument.addObject('PartDesign::CoordinateSystem','LCS')
        else:
            FreeCAD.ActiveDocument.addObject('PartDesign::CoordinateSystem','LCS')
        
        FreeCAD.ActiveDocument.recompute()
        #FreeCAD.Console.PrintWarning( 'Done :)\n' )
        
FreeCADGui.addCommand('DatumLCS',DatumLCS())
##
