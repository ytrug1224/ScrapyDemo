# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
# from scrapy.loader import ItemLoader


class ItspiderItem(scrapy.Item):
    # define the fields for your item here like:
    pass


class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    create_date = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field()
    fav_nums = scrapy.Field()
    comments_nums = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()

