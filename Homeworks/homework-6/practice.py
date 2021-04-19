from lxml import etree

parser = etree.XMLParser(ns_clean=True)

with open('short-data.xml', 'r', encoding='UTF-8') as file:
    tree = etree.parse(file, parser)
    print(parser.error_log)
    result = tree.xpath('/mediawiki/page/revision')
    print(result)

