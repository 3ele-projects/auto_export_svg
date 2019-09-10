#!/usr/bin/env python

""" This is a multiline string, which can also act
as a multiline comment """


import svgwrite
from lxml import etree # Ubuntu Karmic package: python-lxml


import svgutils.transform as sg


VERSION = '0.1dev' # keep in sync with setup.py

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

        logo.attrib['viewBox'] = '0 0 '+str(template_width)+' '+str(template_height)

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
        center_element_y = template_height / 2 - (element_height / 2)

        logo.attrib['x'] = str(center_element_x)
        logo.attrib['y'] = str(center_element_y)
        logo.attrib['width'] = str(element_width)
        logo.attrib['height'] = str(element_height)


        doc = etree.ElementTree(root)
        doc.write(template)





