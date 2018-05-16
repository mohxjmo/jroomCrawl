# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# by huxiajie

class JroomItem(scrapy.Item):
    # table house
    houseID = scrapy.Field()
    housetitle = scrapy.Field()
    city = scrapy.Field()
    district = scrapy.Field()
    area = scrapy.Field()
    street = scrapy.Field()
    community = scrapy.Field()
    room = scrapy.Field()
    lng = scrapy.Field()
    lat = scrapy.Field()
    housepic = scrapy.Field()
    housearea = scrapy.Field()
    housedirect = scrapy.Field()
    housefloor = scrapy.Field()
    househall = scrapy.Field()
    balcony = scrapy.Field()
    bathroom = scrapy.Field()
    housestatus = scrapy.Field()
    housetype = scrapy.Field()
    housearound = scrapy.Field()
    ownertel= scrapy.Field()
    mantel = scrapy.Field()

    # table housepic
    # image_urls 组内的URLs将被Scrapy的调度器和下载器安排下载
    image_urls = scrapy.Field()
    image = scrapy.Field()
    image_paths = scrapy.Field()

    # table payment
    payname = scrapy.Field()
    payrent = scrapy.Field()
    paydeposit = scrapy.Field()
    payservice = scrapy.Field()
