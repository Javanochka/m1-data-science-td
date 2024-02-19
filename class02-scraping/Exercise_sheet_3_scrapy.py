import scrapy
import json

class WikipediaSpider(scrapy.Spider): #Something is missing here. What exactly?
    name = "wikipedia"

    start_urls = ["https://en.wikipedia.org/wiki/List_of_French_artists"]

    def parse(self, response):
        list_els = response.css('#bodyContent li a::attr(href)').getall()#get all links which are in lists on the page
        list_see_also = list_see_also = response.css('#bodyContent ul:nth-child(40) li a::attr(href)').getall() #get the links in see also (they are not about the disctinct authors)
        list_table = response.css('#bodyContent td li a::attr(href)').getall()#get the links in the table
        res_list = list(set(list_els) - set(list_see_also) -set(list_table))
        for link in res_list:
            #check that the link actually exists and is not red
                yield response.follow(link, callback=self.parse_artist)
        
    def parse_artist(self, response):
        url = response.url #get url of the page
        name =response.css('.mw-page-title-main::text').get() # get name of the artist
        paragraph = ''.join(response.css('.mw-content-ltr > p:not(.mw-empty-elt):first-of-type::text').getall())# get the first paragraph
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
