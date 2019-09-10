#!/usr/bin/env python
import sys, getopt
import csv
import logoexportsm as logo2sm
from cairosvg import svg2png


def main(csv_source, logo_name):
    with open(csv_source, newline='') as csvfile:
        template_dic = csv.DictReader(csvfile)
        for template in template_dic:
            export_file = logo2sm.ImMaker()
            template_file = export_file.create_svg_templates(template['width'], template['height'], template['name'])
            logo = export_file.create_svg_image(template_file, logo_name)
            svg2png(url=template['name'] + '.svg', write_to=template['name'] + '.png')


if __name__ == '__main__':
    csv_source = 'sizes.csv'
    logo_name = 'vector.svg'
    try:
        logo_name = sys.argv[1]
        csv_source = sys.argv[2]
        obj_path = sys.argv[3]

        logo_name = obj_path + '/' + logo_name
        csv_sourcee = obj_path + '/' + csv_source
    except:
        print('All parameter?')
    main(csv_source, logo_name)
