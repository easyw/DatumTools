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
from FreeCAD import Base
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
class Plane:
    "datum tools object"
 
    def GetResources(self):
        return {'Pixmap'  : os.path.join( DatumToolsWB_icons_path , 'RefPlane.svg') , # the name of a svg file available in the resources
                     'MenuText': "PlaneRef" ,
                     'ToolTip' : "Plane Reference\nDatumTools workbench"}
 
    def IsActive(self):
        if FreeCAD.ActiveDocument is not None:
            import os, sys
            return True
 
    def Activated(self):
        # do something here...
        def makePlane(plc):
            import FreeCAD, FreeCADGui
            from FreeCAD import Base
            import Part,PartGui
            FreeCAD.ActiveDocument.addObject("Part::Plane","RefPlane")
            plane = FreeCAD.ActiveDocument.ActiveObject
            plane.Length=10.000
            plane.Width=10.000
            l=float(plane.Length)
            w=float(plane.Width)
            px=float(plc.Base.x)
            py=float(plc.Base.y)
            x=px-l/2.0
            y=py-w/2.0
            plane.Placement=Base.Placement(Base.Vector(x,y,0.000),Base.Rotation(0.000,0.000,0.000,1.000))
            FreeCADGui.ActiveDocument.getObject(plane.Name).Transparency = 60
            FreeCADGui.ActiveDocument.getObject(plane.Name).LineColor = (1.000,0.667,0.498)
            return plane
            
        sel = FreeCADGui.Selection.getSelection()
        from FreeCAD import Base
        if len (sel) == 1:
            if 'App::Part' in sel[0].TypeId or 'PartDesign::Body' in sel[0].TypeId \
                    or 'Part::FeaturePython' in sel[0].TypeId:
                try:
                    plc = FreeCAD.Placement(Base.Vector(0.0,0.0,0.000),Base.Rotation(0.000,0.000,0.000,1.000))
                    plane = makePlane(plc)
                    sel[0].addObject(FreeCAD.ActiveDocument.ActiveObject)
                except:
                    plane.Placement = sel[0].Placement.multiply(plane.Placement)
                    print(plane.Label,'exception')
                #    FreeCAD.ActiveDocument.addObject('PartDesign::Plane','DatumPlane')
            else:
                plc = FreeCAD.Placement(Base.Vector(0.0,0.0,0.000),Base.Rotation(0.000,0.000,0.000,1.000))
                makePlane(plc)
        else:
            from FreeCAD import Base
            plc = FreeCAD.Placement(Base.Vector(0.0,0.0,0.000),Base.Rotation(0.000,0.000,0.000,1.000))
            makePlane(plc)        
        FreeCAD.ActiveDocument.recompute()
        #FreeCAD.Console.PrintWarning( 'Done :)\n' )
        
FreeCADGui.addCommand('Plane',Plane())
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
                    sel[0].newObject('PartDesign::CoordinateSystem','Local_CS')
                except:
                    FreeCAD.ActiveDocument.addObject('PartDesign::CoordinateSystem','Local_CS')
            else:
                FreeCAD.ActiveDocument.addObject('PartDesign::CoordinateSystem','Local_CS')
        else:
            FreeCAD.ActiveDocument.addObject('PartDesign::CoordinateSystem','Local_CS')
        
        FreeCAD.ActiveDocument.recompute()
        #FreeCAD.Console.PrintWarning( 'Done :)\n' )
        
FreeCADGui.addCommand('DatumLCS',DatumLCS())
##


#temp_placement_object = App.ActiveDocument.addObject("App::Placement","temporary_placement")
class AltLCS:
    "datum tools object"
 
    def GetResources(self):
        return {'Pixmap'  : os.path.join( DatumToolsWB_icons_path , 'AlternativeLCS.svg') , # the name of a svg file available in the resources
                     'MenuText': "Alternative Datum LCS" ,
                     'ToolTip' : "Alternative Datum LCS\nDatumTools workbench"}
 
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
                    sel[0].newObject("App::Placement",'Local_CSa')
                except:
                    FreeCAD.ActiveDocument.addObject("App::Placement",'Local_CSa')
            else:
                FreeCAD.ActiveDocument.addObject("App::Placement",'Local_CSa')
        else:
            FreeCAD.ActiveDocument.addObject("App::Placement",'Local_CSa')
        
        FreeCAD.ActiveDocument.recompute()
        #FreeCAD.Console.PrintWarning( 'Done :)\n' )
        
FreeCADGui.addCommand('AltLCS',AltLCS())
##

class AnnoLbl:
    "datum tools object"
 
    def GetResources(self):
        return {'Pixmap'  : os.path.join( DatumToolsWB_icons_path , 'Annotation.svg') , # the name of a svg file available in the resources
                     'MenuText': "Annotation Label" ,
                     'ToolTip' : "Annotation Label\nDatumTools workbench"}
 
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
                    sel[0].newObject("App::AnnotationLabel","AnnoLbl")
                    anno = FreeCAD.ActiveDocument.ActiveObject
                    anno.LabelText = "AnnoLbl"
                except:
                    FreeCAD.ActiveDocument.addObject("App::AnnotationLabel","AnnoLbl")
                    anno = FreeCAD.ActiveDocument.ActiveObject
                    anno.LabelText = "AnnoLbl"
            else:
                FreeCAD.ActiveDocument.addObject("App::AnnotationLabel","AnnoLbl")
                anno = FreeCAD.ActiveDocument.ActiveObject
                anno.LabelText = "AnnoLbl"
        else:
            FreeCAD.ActiveDocument.addObject("App::AnnotationLabel","AnnoLbl")
            anno = FreeCAD.ActiveDocument.ActiveObject
            anno.LabelText = "AnnoLbl"
        
        FreeCAD.ActiveDocument.recompute()
        #FreeCAD.Console.PrintWarning( 'Done :)\n' )
        
FreeCADGui.addCommand('AnnoLbl',AnnoLbl())
##