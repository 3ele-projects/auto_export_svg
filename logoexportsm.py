#!/usr/bin/env python

""" This is a multiline string, which can also act
as a multiline comment """


import svgwrite
from lxml import etree # Ubuntu Karmic package: python-lxml

VERSION = '0.1.01'  # keep in sync with setup.py

UNITS = ['pt','px','in','mm','cm']
PT2IN = 1.0/72.0
IN2PT = 72.0
MM2PT = 72.0/25.4
CM2PT = 72.0/2.54
PT2PX = 1.25
PX2PT = 1.0/1.25



def get_unit_attr(value):
    # coordinate handling from http://www.w3.org/TR/SVG11/coords.html#Units
    units = None # default (user)
    for unit_name in UNITS:
        if value.endswith(unit_name):
            units = unit_name
            value = value[:-len(unit_name)]
            break
    val_float = float(value) # this will fail if units str not parsed
    return val_float, units

def convert_to_pixels( val, units):
    if units == 'px' or units is None:
        val_px = val
    elif units == 'pt':
        val_px = val*PT2PX
    elif units == 'in':
        val_px = val*IN2PT*PT2PX
    elif units == 'mm':
        val_px = val*MM2PT*PT2PX
    elif units == 'cm':
        val_px = val*CM2PT*PT2PX
    else:
        raise ValueError('unsupport unit conversion to pixels: %s'%units)
    return val_px

class ImMaker:
    def create_svg_templates (self,width, height, name):
        dwg = svgwrite.Drawing(name+'.svg', profile='tiny', size =(width, height), )
        dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='rgb(255,255,255)'))
        dwg.save()
        return name+'.svg'




    def create_svg_image(self,template, logo_name):
        tree = etree.parse(template)
        root = tree.getroot()
        margin = 10
        logo = etree.parse(logo_name)
        logo = logo.getroot()
        root.append(logo)


        template_width = float(root.attrib['width'])
        template_height = float(root.attrib['height'])

        element_height = float(logo.attrib['height'])
        element_width = float(logo.attrib['width'])

        #logo.attrib['viewBox'] = '0 0 '+str(template_width)+' '+str(template_height)
        logo.attrib['preserveAspectRatio'] = "xMidYMid"
        element_width = template_width- margin
        logo.attrib['width'] = str(element_width)
        element_height = template_height- margin
        logo.attrib['height'] = str(element_height)

        if element_width > template_width:
            element_width = template_width - margin
            logo.attrib['x'] = str(margin)
            logo.attrib['width'] =str (element_width)



        if element_height > template_height:
            element_height = template_height - margin
            logo.attrib['y'] = str(margin)
            logo.attrib['height'] = str(element_height)

        center_element_x = template_width / 2 - (element_width / 2)
        center_element_y = template_height / 2 + (element_height / 2)

       # logo.attrib['x'] = str(center_element_x)
       # logo.attrib['y'] = str(center_element_y)
        print ('center_element_x')
        logo.attrib['width'] = str(element_width)
        logo.attrib['height'] = str(element_height)


        doc = etree.ElementTree(root)
        doc.write(template)





