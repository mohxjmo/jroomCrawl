# -*- coding: utf-8 -*-
import codecs
import re
import scrapy
from scrapy.http import Request
from JRoom.items import JroomItem
import json
import urllib.request


# by huxiajie
class ZiroomSpider(scrapy.Spider):
    name = 'ziroom'
    allowed_domains = ['ziroom.com']
    start_urls = ['http://www.ziroom.com/z/nl/z2-r1-d23008614.html',  #东城
                  'http://www.ziroom.com/z/nl/z2-r2-d23008614.html',
                  'http://www.ziroom.com/z/nl/z2-r3-d23008614.html',
                  'http://www.ziroom.com/z/nl/z2-r4-d23008614.html',
                  'http://www.ziroom.com/z/nl/z2-r5-d23008614.html',
                  'http://www.ziroom.com/z/nl/z2-r6-d23008614.html',
                  'http://www.ziroom.com/z/nl/z2-r1-d23008626.html',  #西城
                  'http://www.ziroom.com/z/nl/z2-r2-d23008626.html',
                  'http://www.ziroom.com/z/nl/z2-r3-d23008626.html',
                  'http://www.ziroom.com/z/nl/z2-r4-d23008626.html',
                  'http://www.ziroom.com/z/nl/z2-r5-d23008626.html',
                  'http://www.ziroom.com/z/nl/z2-r6-d23008626.html',
                  'http://www.ziroom.com/z/nl/z2-r1-d23008613.html',  #朝阳
                  'http://www.ziroom.com/z/nl/z2-r2-d23008613.html',
                  'http://www.ziroom.com/z/nl/z2-r3-d23008613.html',
                  'http://www.ziroom.com/z/nl/z2-r4-d23008613.html',
                  'http://www.ziroom.com/z/nl/z2-r5-d23008613.html',
                  'http://www.ziroom.com/z/nl/z2-r6-d23008613.html',
                  'http://www.ziroom.com/z/nl/z2-r1-d23008618.html',  #海淀
                  'http://www.ziroom.com/z/nl/z2-r2-d23008618.html',
                  'http://www.ziroom.com/z/nl/z2-r3-d23008618.html',
                  'http://www.ziroom.com/z/nl/z2-r4-d23008618.html',
                  'http://www.ziroom.com/z/nl/z2-r5-d23008618.html',
                  'http://www.ziroom.com/z/nl/z2-r6-d23008618.html',
                  'http://www.ziroom.com/z/nl/z2-r1-d23008617.html',  #丰台
                  'http://www.ziroom.com/z/nl/z2-r2-d23008617.html',
                  'http://www.ziroom.com/z/nl/z2-r3-d23008617.html',
                  'http://www.ziroom.com/z/nl/z2-r4-d23008617.html',
                  'http://www.ziroom.com/z/nl/z2-r5-d23008617.html',
                  'http://www.ziroom.com/z/nl/z2-r6-d23008617.html',
                  'http://www.ziroom.com/z/nl/z2-r1-d23008623.html',  #石景山
                  'http://www.ziroom.com/z/nl/z2-r2-d23008623.html',
                  'http://www.ziroom.com/z/nl/z2-r3-d23008623.html',
                  'http://www.ziroom.com/z/nl/z2-r4-d23008623.html',
                  'http://www.ziroom.com/z/nl/z2-r5-d23008623.html',
                  'http://www.ziroom.com/z/nl/z2-r6-d23008623.html',
                  'http://www.ziroom.com/z/nl/z2-r1-d23008625.html',  #通州
                  'http://www.ziroom.com/z/nl/z2-r2-d23008625.html',
                  'http://www.ziroom.com/z/nl/z2-r3-d23008625.html',
                  'http://www.ziroom.com/z/nl/z2-r4-d23008625.html',
                  'http://www.ziroom.com/z/nl/z2-r5-d23008625.html',
                  'http://www.ziroom.com/z/nl/z2-r6-d23008625.html',
                  'http://www.ziroom.com/z/nl/z2-r1-d23008611.html',  #昌平
                  'http://www.ziroom.com/z/nl/z2-r2-d23008611.html',
                  'http://www.ziroom.com/z/nl/z2-r3-d23008611.html',
                  'http://www.ziroom.com/z/nl/z2-r4-d23008611.html',
                  'http://www.ziroom.com/z/nl/z2-r5-d23008611.html',
                  'http://www.ziroom.com/z/nl/z2-r6-d23008611.html',
                  'http://www.ziroom.com/z/nl/z2-r1-d23008615.html',  #大兴
                  'http://www.ziroom.com/z/nl/z2-r2-d23008615.html',
                  'http://www.ziroom.com/z/nl/z2-r3-d23008615.html',
                  'http://www.ziroom.com/z/nl/z2-r4-d23008615.html',
                  'http://www.ziroom.com/z/nl/z2-r5-d23008615.html',
                  'http://www.ziroom.com/z/nl/z2-r6-d23008615.html',
                  'http://www.ziroom.com/z/nl/z2-r1-d23008624.html',  #顺义
                  'http://www.ziroom.com/z/nl/z2-r2-d23008624.html',
                  'http://www.ziroom.com/z/nl/z2-r3-d23008624.html',
                  'http://www.ziroom.com/z/nl/z2-r4-d23008624.html',
                  'http://www.ziroom.com/z/nl/z2-r5-d23008624.html',
                  'http://www.ziroom.com/z/nl/z2-r6-d23008624.html',
                  'http://www.ziroom.com/z/nl/z2-r1-d23008616.html',  #房山
                  'http://www.ziroom.com/z/nl/z2-r2-d23008616.html',
                  'http://www.ziroom.com/z/nl/z2-r3-d23008616.html',
                  'http://www.ziroom.com/z/nl/z2-r4-d23008616.html',
                  'http://www.ziroom.com/z/nl/z2-r5-d23008616.html',
                  'http://www.ziroom.com/z/nl/z2-r6-d23008616.html',
                  'http://www.ziroom.com/z/nl/z2-r1-d23008620.html',  #门头沟
                  'http://www.ziroom.com/z/nl/z2-r2-d23008620.html',
                  'http://www.ziroom.com/z/nl/z2-r3-d23008620.html',
                  'http://www.ziroom.com/z/nl/z2-r4-d23008620.html',
                  'http://www.ziroom.com/z/nl/z2-r5-d23008620.html',
                  'http://www.ziroom.com/z/nl/z2-r6-d23008620.html',
                  'http://www.ziroom.com/z/nl/z2-r1-d23008629.html',  #亦庄开发区
                  'http://www.ziroom.com/z/nl/z2-r2-d23008629.html',
                  'http://www.ziroom.com/z/nl/z2-r3-d23008629.html',
                  'http://www.ziroom.com/z/nl/z2-r4-d23008629.html',
                  'http://www.ziroom.com/z/nl/z2-r5-d23008629.html',
                  'http://www.ziroom.com/z/nl/z2-r6-d23008629.html',
                  'http://www.ziroom.com/z/nl/z1-r1-d23008614.html',  # 东城
                  'http://www.ziroom.com/z/nl/z1-r2-d23008614.html',
                  'http://www.ziroom.com/z/nl/z1-r3-d23008614.html',
                  'http://www.ziroom.com/z/nl/z1-r4-d23008614.html',
                  'http://www.ziroom.com/z/nl/z1-r5-d23008614.html',
                  'http://www.ziroom.com/z/nl/z1-r6-d23008614.html',
                  'http://www.ziroom.com/z/nl/z1-r1-d23008626.html',  # 西城
                  'http://www.ziroom.com/z/nl/z1-r2-d23008626.html',
                  'http://www.ziroom.com/z/nl/z1-r3-d23008626.html',
                  'http://www.ziroom.com/z/nl/z1-r4-d23008626.html',
                  'http://www.ziroom.com/z/nl/z1-r5-d23008626.html',
                  'http://www.ziroom.com/z/nl/z1-r6-d23008626.html',
                  'http://www.ziroom.com/z/nl/z1-r1-d23008613.html',  # 朝阳
                  'http://www.ziroom.com/z/nl/z1-r2-d23008613.html',
                  'http://www.ziroom.com/z/nl/z1-r3-d23008613.html',
                  'http://www.ziroom.com/z/nl/z1-r4-d23008613.html',
                  'http://www.ziroom.com/z/nl/z1-r5-d23008613.html',
                  'http://www.ziroom.com/z/nl/z1-r6-d23008613.html',
                  'http://www.ziroom.com/z/nl/z1-r1-d23008618.html',  # 海淀
                  'http://www.ziroom.com/z/nl/z1-r2-d23008618.html',
                  'http://www.ziroom.com/z/nl/z1-r3-d23008618.html',
                  'http://www.ziroom.com/z/nl/z1-r4-d23008618.html',
                  'http://www.ziroom.com/z/nl/z1-r5-d23008618.html',
                  'http://www.ziroom.com/z/nl/z1-r6-d23008618.html',
                  'http://www.ziroom.com/z/nl/z1-r1-d23008617.html',  # 丰台
                  'http://www.ziroom.com/z/nl/z1-r2-d23008617.html',
                  'http://www.ziroom.com/z/nl/z1-r3-d23008617.html',
                  'http://www.ziroom.com/z/nl/z1-r4-d23008617.html',
                  'http://www.ziroom.com/z/nl/z1-r5-d23008617.html',
                  'http://www.ziroom.com/z/nl/z1-r6-d23008617.html',
                  'http://www.ziroom.com/z/nl/z1-r1-d23008623.html',  # 石景山
                  'http://www.ziroom.com/z/nl/z1-r2-d23008623.html',
                  'http://www.ziroom.com/z/nl/z1-r3-d23008623.html',
                  'http://www.ziroom.com/z/nl/z1-r4-d23008623.html',
                  'http://www.ziroom.com/z/nl/z1-r5-d23008623.html',
                  'http://www.ziroom.com/z/nl/z1-r6-d23008623.html',
                  'http://www.ziroom.com/z/nl/z1-r1-d23008625.html',  # 通州
                  'http://www.ziroom.com/z/nl/z1-r2-d23008625.html',
                  'http://www.ziroom.com/z/nl/z1-r3-d23008625.html',
                  'http://www.ziroom.com/z/nl/z1-r4-d23008625.html',
                  'http://www.ziroom.com/z/nl/z1-r5-d23008625.html',
                  'http://www.ziroom.com/z/nl/z1-r6-d23008625.html',
                  'http://www.ziroom.com/z/nl/z1-r1-d23008611.html',  # 昌平
                  'http://www.ziroom.com/z/nl/z1-r2-d23008611.html',
                  'http://www.ziroom.com/z/nl/z1-r3-d23008611.html',
                  'http://www.ziroom.com/z/nl/z1-r4-d23008611.html',
                  'http://www.ziroom.com/z/nl/z1-r5-d23008611.html',
                  'http://www.ziroom.com/z/nl/z1-r6-d23008611.html',
                  'http://www.ziroom.com/z/nl/z1-r1-d23008615.html',  # 大兴
                  'http://www.ziroom.com/z/nl/z1-r2-d23008615.html',
                  'http://www.ziroom.com/z/nl/z1-r3-d23008615.html',
                  'http://www.ziroom.com/z/nl/z1-r4-d23008615.html',
                  'http://www.ziroom.com/z/nl/z1-r5-d23008615.html',
                  'http://www.ziroom.com/z/nl/z1-r6-d23008615.html',
                  'http://www.ziroom.com/z/nl/z1-r1-d23008624.html',  # 顺义
                  'http://www.ziroom.com/z/nl/z1-r2-d23008624.html',
                  'http://www.ziroom.com/z/nl/z1-r3-d23008624.html',
                  'http://www.ziroom.com/z/nl/z1-r4-d23008624.html',
                  'http://www.ziroom.com/z/nl/z1-r5-d23008624.html',
                  'http://www.ziroom.com/z/nl/z1-r6-d23008624.html',
                  'http://www.ziroom.com/z/nl/z1-r1-d23008616.html',  # 房山
                  'http://www.ziroom.com/z/nl/z1-r2-d23008616.html',
                  'http://www.ziroom.com/z/nl/z1-r3-d23008616.html',
                  'http://www.ziroom.com/z/nl/z1-r4-d23008616.html',
                  'http://www.ziroom.com/z/nl/z1-r5-d23008616.html',
                  'http://www.ziroom.com/z/nl/z1-r6-d23008616.html',
                  'http://www.ziroom.com/z/nl/z1-r1-d23008620.html',  # 门头沟
                  'http://www.ziroom.com/z/nl/z1-r2-d23008620.html',
                  'http://www.ziroom.com/z/nl/z1-r3-d23008620.html',
                  'http://www.ziroom.com/z/nl/z1-r4-d23008620.html',
                  'http://www.ziroom.com/z/nl/z1-r5-d23008620.html',
                  'http://www.ziroom.com/z/nl/z1-r6-d23008620.html',
                  'http://www.ziroom.com/z/nl/z1-r1-d23008629.html',  # 亦庄开发区
                  'http://www.ziroom.com/z/nl/z1-r2-d23008629.html',
                  'http://www.ziroom.com/z/nl/z1-r3-d23008629.html',
                  'http://www.ziroom.com/z/nl/z1-r4-d23008629.html',
                  'http://www.ziroom.com/z/nl/z1-r5-d23008629.html',
                  'http://www.ziroom.com/z/nl/z1-r6-d23008629.html'
                  ]
    paytype = ["天", "月", "季", "半年", "年"]
    total = 0
    invalid = 0

    # 自定义配置
    custom_settings = {
        # item处理管道
        'ITEM_PIPELINES': {
            'JRoom.pipelines.MySqlPipeline': 1,
        },
    }

    # 伪装成浏览器，对start_urls依次爬取
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, self.parse)

    def parse(self, response):
        # 获取房屋链接
        links = response.xpath('//a[@class="t1"]/@href').extract()

        url = response.url
        try:
            nexturl = response.xpath('//a[@class="next"]/@href').extract()[0]
            nexturl = "http:" + nexturl
        except IndexError:
            nexturl = url

        for link in links:
            link = "http:" + link
            yield Request(link, callback=self.house_parse)

        # 若是最后一页，那么nexturl也是最后一页的地址
        if nexturl != url:
            yield Request(nexturl, callback=self.parse)

    # total:9765; 11313; 10777
    # valid:6182; 6814; 7335
    # invalid:3582; 4494; 3434
    def house_parse(self, response):
        print("**********正在访问：" + response.url + "**********")
        self.total += 1
        print('total:' + str(self.total))
        ifconfig = response.xpath('//ul[@class="detail_room"]/li[1]/text()').extract()[0]
        if "约" in ifconfig:
            print("该房源正在配置，不访问:" + response.url)
            self.invalid += 1
            print('invalid:' + str(self.invalid))
            return

        item = JroomItem()
        # table:house
        try:
            item['houseID'] = response.xpath('//input[@id="room_code"]/@value').extract()[0]
        except IndexError:
            item['houseID'] = ""
        try:
            item['housetitle'] = response.xpath('//div[@class="room_name"]/h2/text()').extract()[0].strip()
        except IndexError:
            item['housetitle'] = ""
        item['city'] = "北京"
        try:
            item['district'] = re.findall('\[(.+?)\s', response.xpath('//p[@class="pr"]/span[@class="ellipsis"]/text()').extract()[0])[0]
            item['district'] = item['district'].replace('区', "")
        except IndexError:
            item['district'] = ""
        try:
            item['area'] = re.findall('\s(\S+?)]', response.xpath('//p[@class="pr"]/span[@class="ellipsis"]/text()').extract()[0])[0]
        except IndexError:
            item['area'] = ""
        try:
            item['community'] = re.findall('(.+?)\d居室', item['housetitle'])[0]
        except IndexError:
            item['community'] = ""
        try:
            item['street'] = re.findall('(.+?)\d居室',response.xpath('//input[@id="mapsearchText"]/@data-title').extract()[0])[0]
            item['street'] = item['street'].replace(item['district'], "")
            item['street'] = item['street'].replace(item['community'], "")
            item['street'] = item['street'].replace(item['area'], "")
            item['street'] = item['street'].replace('区', "")
        except IndexError:
            item['street'] = ""
        try:
            item['room'] = re.findall('.+?(\d居室)',response.xpath('//input[@id="mapsearchText"]/@data-title').extract()[0])[0]
        except IndexError:
            item['room'] = ""
        try:
            item['lng'] = response.xpath('//input[@id="mapsearchText"]/@data-lng').extract()[0]
            item['lat'] = response.xpath('//input[@id="mapsearchText"]/@data-lat').extract()[0]
        except IndexError:
            item['lng'] = ""
            item['lat'] = ""
        try:
            item['housearea'] = float(re.findall('面积\S\s*?(\d.+?)\s㎡',
                                                 response.xpath('//ul[@class="detail_room"]/li[1]/text()').extract()[
                                                     0])[0])
        except IndexError:
            item['housearea'] = 0
        try:
            item['housedirect'] = \
                re.findall('朝向\S\s*?(\S+)', response.xpath('//ul[@class="detail_room"]/li[2]/text()').extract()[0])[0]
        except IndexError:
            item['housedirect'] = ""
        try:
            item['housefloor'] = \
                re.findall('楼层\S\s*?(\d.+?)\s*层',
                           response.xpath('//ul[@class="detail_room"]/li[4]/text()').extract()[0])[0]
        except IndexError:
            item['housefloor'] = ""
        try:
            item['househall'] = \
                re.findall('户型\S\s*?(\d\S\d\S)',
                           response.xpath('//ul[@class="detail_room"]/li[3]/text()').extract()[0])[0]
        except IndexError:
            item['househall'] = ""
        try:
            item['balcony'] = response.xpath('//span[@class="balcony"]').extract()[0]
            item['balcony'] = 1
        except IndexError:
            item['balcony'] = 0
        try:
            item['bathroom'] = response.xpath('//span[@class="toilet"]').extract()[0]
            item['bathroom'] = 1
        except IndexError:
            item['bathroom'] = 0
        item['housestatus'] = 1
        try:
            item['housetype'] = response.xpath('//span[@class="icons"]/text()').extract()[0] + "租"
        except IndexError:
            item['housetype'] = ""
        try:
            item['housearound'] = response.xpath('//div[@class="aboutRoom gray-6"]/p/text()').extract()[0]
        except IndexError:
            item['housearound'] = ""
        item['ownertel'] = "00000000000"
        item['mantel'] = "88886688"

        # table:housepic
        item['image_urls'] = response.xpath('//img[@class="loadImgError"]/@src').extract()
        item['housepic'] = item['image_urls'][0]

        # table:payment
        item['payname'] = []
        item['payrent'] = []
        item['paydeposit'] = []
        item['payservice'] = []
        try:
            item['payname'] = response.xpath('//div[@id="payCon"]/table/tr/td[1]/span/text()').extract()
            temp = item['payname'][0]
            for payrent in response.xpath('//div[@id="payCon"]/table/tr/td[2]/text()').extract():
                item['payrent'].append(int(re.findall('(\d+?)\D', payrent)[0]))
            for paydeposit in response.xpath('//div[@id="payCon"]/table/tr/td[3]/text()').extract():
                item['paydeposit'].append(int(re.findall('(\d+)', paydeposit)[0]))
            for payservice in response.xpath('//div[@id="payCon"]/table/tr/td[4]/text()').extract():
                item['payservice'].append(int(re.findall('(\d+?)\D', payservice)[0]))
        except IndexError:
            paytext = response.xpath('//span[@class="price"]/span[2]/text()').extract()[0]
            payprice = re.findall('\D(\d+)', response.xpath('//span[@class="price"]/span[1]/text()').extract()[0])[0]
            flag = True
            for type in self.paytype:
                if type in paytext:
                    item['payname'].append(type + "付")
                    item['payrent'].append(int(payprice))
                    item['paydeposit'].append(int(payprice))
                    item['payservice'].append(2000)
                    flag = False
                    break
            if flag==True:
                item['payname'].append("none")
                item['payrent'].append(0)
                item['paydeposit'].append(0)
                item['payservice'].append(0)
        return item
