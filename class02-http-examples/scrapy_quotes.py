import scrapy

class QuotesSpider(scrapy.Spider):
    name = "MyFirstQuoteSpider"
    start_urls = ["http://quotes.toscrape.com/page/1/"]
   
    """
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = "quotes-%s.html" % page
        with open(filename, "wb") as f:
            f.write(response.body)
    
    """
    def parse(self, response):
        with open('quotes-s.txt', 'a') as f:
            quotes = response.css("div.quote")
            for quote in quotes:
                text = quote.css('span.text::text').extract_first()
                print(text,file=f)
        next_page=response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            #next_page = response.urljoin(next_page)
            #yield scrapy.Request(next_page, callback=self.parse) 
            yield response.follow(next_page, callback=self.parse)       

if __name__=='__main__':
    import scrapy.crawler
    #myspider = QuotesSpider()
    process = scrapy.crawler.CrawlerProcess({
        'USER_AGENT':'Mozilla/5.0'
    })
    process.crawl(QuotesSpider)
    process.start()
    process.stop()
