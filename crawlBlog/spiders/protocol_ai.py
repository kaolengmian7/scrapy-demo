import scrapy
from crawlBlog.items import CrawlblogItem


class ProtocolAiSpider(scrapy.Spider):
    name = "protocol_ai"
    allowed_domains = ["protocol.ai"]
    start_urls = ["https://protocol.ai/blog/"]

    def parse(self, response):
        for article in response.css('article'):
            item = CrawlblogItem()
            item['title'] = article.css('h1::text').get().strip()
            item['desc'] = article.css('p[itemprop="description"]::text').get().strip()
            item['pub_date'] = article.css('time::attr(datetime)').get()
            yield item
