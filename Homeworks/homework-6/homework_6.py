from lxml import etree

# Practice Example
# parser = etree.XMLParser(ns_clean=True)
# with open('short-data.xml', 'r', encoding='UTF-8') as file:
#     tree = etree.parse(file, parser)
#     print(parser.error_log)
#     result = tree.xpath('/mediawiki/page/revision')
#     print(result)

class ComposerPageQueryTool:
    def __init__(self, tree):
        self.tree = tree
        self.r = "/mediawiki/page/revision"

    def run_query(self, query):
        return self.tree.xpath(query)

    def count_comments(self):
        """
        Returns the number of pages with comments
        """
        return self.run_query(f"count({self.r}/comment)")

    def count_revisions_by_user(self):
        """
        Returns the number of pages for user id 5558
        """
        return self.run_query(f"count({self.r}/contributor[id = 5558])")

    def contribution_timestamp(self):
        """
        Returns the timestamp for the 12th page revised by user 5558
        """
        return self.run_query(f"({self.r}/contributor[id = 5558]/ancestor::page)[12]/revision/timestamp/text()")

    def count_larger_pages(self):
        """
        Returns the number of pages with more than 1kb of content
        """
        return self.run_query(f'count({self.r}/text[@bytes > 1000])')

    def page_reviser(self):
        """
        Returns the username for the contributor who edited page 150096
        """
        return self.run_query("/mediawiki/page[id=150096]/revision/contributor/username/text()")

    def title_timestamp(self):
        """
        Returns the title of the composition that was revised at 2015-02-07T22:58:31Z
        """
        return self.run_query(f"{self.r}[timestamp = '2015-02-07T22:58:31Z']/../title/text()")

    def count_sonata(self):
        """
        Returns the number of pages where the composition title starts with "Sonata"
        """
        return self.run_query("count( /mediawiki/page[starts-with (title, 'Sonata') ] )")

    def sibling_tag(self):
        """
        Returns the tag name for the third sibling of the text element containing the file: 
        PMLP137192-ariaperquestabel00moza.pdf
        """
        return self.run_query(f"name(({self.r}[contains(text, 'PMLP137192-ariaperquestabel00moza.pdf')]/*)[3])")
