import scrapy
import json

from scrapy.http import HtmlResponse


class WikipediaSpider(scrapy.Spider): #Something is missing here. What exactly?
    name = "wikipedia"

    start_urls = ["https://en.wikipedia.org/wiki/List_of_French_artists"]

    def parse(self, response):
        list_els = response.css('li a::attr(href)').getall() #get all links which are in lists on the page
        list_see_also = response.xpath('//p[contains(text(), "See also")]/a/@href').getall() #get the links in see also (they are not about the disctinct authors)
        res_list = list(set(list_els) - set(list_see_also))
        for link in res_list:
            #check that the link actually exists and is not red
            if "redlink" not in link:
                yield response.follow(link, callback=self.parse_artist)
        
    def parse_artist(self, response):
        url = response.url #get url of the page
        name = response.css('span.mw-page-title-main::text').get() # get name of the artist
        paragraph = response.xpath('string(//div[@class="mw-parser-output"]/p)').extract_first()# get the first paragraph
        yield {'url': url,
               'name': name,
               'paragraph': paragraph}
        
        
if __name__=='__main__':
    import scrapy.crawler
    
    process = scrapy.crawler.CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0',
        'FEEDS': {
            "artists.json": {"format": "json"},
        },
    })
    process.crawl(WikipediaSpider)
    process.start()
    process.stop()
