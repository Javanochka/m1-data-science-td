from pathlib import Path
import scrapy
import json

class WikipediaSpider(scrapy.Spider): #Something is missing here. What exactly?
    name = "wikipedia"

    start_urls = ["https://en.wikipedia.org/wiki/List_of_French_artists"]

    def parse(self, response):
        #get all links which are in lists on the page
        list_els = response.xpath('//div[@class="mw-parser-output"]/ul/li/a[1]/@href').getall()
        #get the links in see also (they are not about the disctinct authors)
        list_see_also = response.xpath('//h2[span/@id="See_also"]/following-sibling::ul/li/a/@href').getall()
        res_list = list(set(list_els) - set(list_see_also))
        for link in res_list:
            #check that the link actually exists and is not red
            if not link.endswith('&redlink=1'):
                yield response.follow(link, callback=self.parse_artist)
        
    def parse_artist(self, response):
        url = response.url #get url of the page
        name = response.xpath('//h1/span/text()').get().split('(')[0].strip() # get name of the artist
        # [@class != "mw-empty-elt"]
        paragraph = (''.join(response.xpath('//div[@class="mw-parser-output"]/p[not(@class)][1]//text()').getall())).strip() # get the first paragraph
        yield {'url': url,
               'name': name,
               'paragraph': paragraph}
        
        
if __name__=='__main__':
    import scrapy.crawler

    if Path('artists.json').is_file():
        Path('artists.json').unlink()
    
    process = scrapy.crawler.CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0',
        'FEEDS': {
            "artists.json": {"format": "json"},
        },
    })
    process.crawl(WikipediaSpider)
    process.start()
    process.stop()
