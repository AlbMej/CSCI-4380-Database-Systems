from lxml import etree
import sys

parser = etree.XMLParser(ns_clean=True)

with open('course-data.xml', 'r', encoding='UTF-8') as file:
    tree = etree.parse(file, parser)
    print(parser.error_log)
    result = tree.xpath("//course")
    print(result)

