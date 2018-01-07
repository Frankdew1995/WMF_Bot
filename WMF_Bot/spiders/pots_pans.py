# -*- coding: utf-8 -*-
import scrapy
from WMF_Bot.items import WmfBotItem

from scrapy_splash import SplashRequest



class CatalogueSpiderSpider(scrapy.Spider):
    name = 'pots_pans'
    allowed_domains = ['www.wmf.com']
    # urls = response.css('a.product-image::attr(href)').extract()

    start_urls = ['http://www.wmf.com/en/pots-pans.html']
    base_url = 'https://www.wmf.com/en/pots-pans.html?p={}'

    def parse(self, response):

        urls = response.css('a.product-image::attr(href)').extract()
        for url in urls:
            yield SplashRequest(url=url, callback=self.parse_details, endpoint='render.html',
                args={'wait': 0.5},)

        for i in range(2,30):
            next_page = self.base_url.format(i)
            yield scrapy.Request(url=next_page, callback=self.parse)



    def parse_details(self,response):
        item = WmfBotItem()
        item['name'] = response.css('h1.product-name::text').extract()
        item['img'] = response.css('a.thumb-link>img::attr(src)')[0].extract()
        item['ean'] = response.css('td.data::text')[1].extract()
        item['Size_sets'] = response.css('td.data::text')[3].extract()
        item['Material'] = response.css('td.data::text')[4].extract()
        item['Product_properties'] = response.css('td.data::text')[5].extract()
        item['Stove_type'] = response.css('td.data::text')[7].extract()
        item['Lid_Type'] = response.css('td.data::text')[9].extract()
        item['Height_cm'] = response.css('td.data::text')[10].extract()
        item['Diameter_cm'] = response.css('td.data::text')[11].extract()
        item['Hotplate_diameter_cm'] = response.css('td.data::text')[12].extract()
        item['Capacity_in_L'] = response.css('td.data::text')[13].extract()
        item['Color'] = response.css('td.data::text')[14].extract()
        item['Care'] = response.css('td.data::text')[15].extract()
        yield item

