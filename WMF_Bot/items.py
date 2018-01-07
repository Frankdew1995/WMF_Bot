# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WmfBotItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    img = scrapy.Field()
    ean = scrapy.Field()
    Size_sets = scrapy.Field()
    Material = scrapy.Field()
    Product_properties = scrapy.Field()
    Stove_type = scrapy.Field()
    Lid_Type = scrapy.Field()
    Height_cm = scrapy.Field()
    Diameter_cm = scrapy.Field()
    Hotplate_diameter_cm = scrapy.Field()
    Capacity_in_L = scrapy.Field()
    Color = scrapy.Field()
    Care = scrapy.Field()





