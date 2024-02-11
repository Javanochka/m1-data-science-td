import scrapy
import json

class WikipediaSpider(scrapy.Spider): 
    name = "wikipedia"

    start_urls = ["https://en.wikipedia.org/wiki/List_of_French_artists"]

    def parse(self, response):
        list_els = response.css('#mw-content-text div[role="note"] + ul li a::attr(href)').getall()
        list_see_also = response.css('h2:has(\#See_also) + ul li a::attr(href)').getall()
        res_list = list(set(list_els) - set(list_see_also))
        for link in res_list:
            #check that the link actually exists and is not red
            yield response.follow(link, callback=self.parse_artist)
        
    def parse_artist(self, response):
        base_url = 'https://en.wikipedia.org'
        url = response.css('#mw-content-text div[role="note"] + ul li a::attr(href)').getall()
        for link in url:
            link = base_url+link
            print(link)
        name = response.css('#mw-content-text div[role="note"] + ul li a::attr(title)').getall()
        paragraph = # get the first paragraph
        yield {'url': url,
               'name': name,
               'paragraph': paragraph}
        
        
if __name__=='__main__':
    import scrapy.crawler
    
    process = scrapy.crawler.CrawlerProcess({
        'USER_AGENT': 'Safari',
        'FEEDS': {
            "artists.json": {"format": "json"},
        },
    })
    process.crawl(WikipediaSpider)
    process.start()
    process.stop()
