import scrapy
import json

class WikipediaSpider(scrapy.Spider): #Something is missing here. What exactly?
    name = "wikipedia"

    start_urls = ["https://en.wikipedia.org/wiki/List_of_French_artists"]

    def parse(self, response):
        list_els = response.css("li [href]")
        list_see_also = response.css("#See_also ~ li [href]")
        res_list = list(set(list_els) - set(list_see_also))
        for link in res_list:
            #check that the link actually exists and is not red
            if link.css("[title*='(page does not exist)']").extract_first() is None:
                yield response.follow(link, callback=self.parse_artist)

        
    def parse_artist(self, response):
        url = response.request.url
        name = response.css(".mw-page-title-main::text").extract_first()
        paragraph = ' '.join(t.strip() for t in response.css("#mw-content-text p::text").extract()).strip()
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
