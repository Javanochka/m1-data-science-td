import scrapy
import json


class WikipediaSpider(scrapy.Spider):  # Something is missing here. What exactly?
    name = "wikipedia"

    start_urls = ["https://en.wikipedia.org/wiki/List_of_French_artists"]

    def parse(self, response):
        list_els = response.css(
            "div.mw-parser-output > ul > li > a::attr(href)"
        ).getall()
        list_see_also = response.css(
            "div.mw-parser-output > ul:last-of-type > li > a::attr(href)"
        ).getall()
        res_list = list(set(list_els) - set(list_see_also))
        for link in res_list:
            if link.startswith("/wiki/"):
                yield response.follow(link, callback=self.parse_artist)

    def parse_artist(self, response):
        url = response.url
        name = response.css("span.mw-page-title-main::text").get()
        paragraph = response.css("table.infobox + p::text").get()
        if paragraph == None:
            paragraph = response.css("div.thumb + p::text").get()
        yield {"url": url, "name": name, "paragraph": paragraph}


if __name__ == "__main__":
    import scrapy.crawler

    process = scrapy.crawler.CrawlerProcess(
        {
            "USER_AGENT": "Mozilla/5.0",
            "FEEDS": {
                "artists.json": {"format": "json"},
            },
        }
    )
    process.crawl(WikipediaSpider)
    process.start()
    process.stop()
