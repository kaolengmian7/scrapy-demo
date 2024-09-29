# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlblogItem(scrapy.Item):
    all = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    pub_date = scrapy.Field()
