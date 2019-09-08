#!/usr/bin/env python

""" This is a multiline string, which can also act
as a multiline comment """

import svg_stack as ss
import csv
import svgutils.transform as st
import sys, re, os
import base64
import svgwrite
import whratio
import lxml
from lxml import etree # Ubuntu Karmic package: python-lxml
from cairosvg import svg2png

import svgutils.transform as sg




def create_svg_templates (width, height, name):
    dwg = svgwrite.Drawing(name+'.svg', profile='tiny', size =(width, height), )
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='rgb(255,255,255)'))
    dwg.save()
    return name+'.svg'


def check_oriantation(width, height):
    if width > height:
        return True
    else:
        return False


def create_svg_image(fname):
    tree = etree.parse(fname)
    root = tree.getroot()
    margin = 10

    logo_name = 'vector.svg'
    logo = etree.parse(logo_name)
    logo = logo.getroot()
    template_width = int(root.attrib['width'])
    template_height = int(root.attrib['height'])
    element_height = int(logo.attrib['height'])
    element_width = int(logo.attrib['width'])





    root.append(logo)



    if check_oriantation(logo.attrib['width'], logo.attrib['height']):
        print('Logo is horizontal')
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

    print('Template width: '+ root.attrib['width'])
    print('Template height: '+ root.attrib['height'])
    print('Logo width: ' +logo.attrib['width'])
    print ('Logo height: '+logo.attrib['height'])

    print('Logo Position horizontal: ' + logo.attrib['x'])
    print ('Logo Position vertical: '+logo.attrib['y'])
    doc = etree.ElementTree(root)
    doc.write(fname)


def main():
    csv_source = 'sizes.csv'



    with open(csv_source, newline='') as csvfile:
        template_dic = csv.DictReader(csvfile)
        for template in template_dic:
            file_name = create_svg_templates(template['width'], template['height'], template['name'] )
            logo = create_svg_image(file_name)
            svg2png(
                url=template['name']+'.svg', write_to=template['name']+'.png')




if __name__ == '__main__':
    main()

