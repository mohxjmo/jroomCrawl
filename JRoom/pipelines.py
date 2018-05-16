# -*- coding: utf-8 -*-
import pymysql


# by huxiajie

class MySqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            db="jroom",
            user="root",
            passwd="123456",
            charset='utf8'
        )
        self.cursor = self.conn.cursor()
        if self.conn is None:
            print("***********数据库连接失败***********")
        else:
            print("***********数据库连接成功***********")
        self.count = 0

    def process_item(self, item, spider):
        try:
            # table:house
            self.cursor.execute(
                "insert into house (houseID, housetitle, city, district, area, street, community, room, lng, lat, housearea, housedirect, housefloor, househall, balcony, bathroom, housepic, housearound, housestatus, housetype,ownertel,mantel) values(%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (item['houseID'],
                 item['housetitle'],
                 item['city'],
                 item['district'],
                 item['area'],
                 item['street'],
                 item['community'],
                 item['room'],
                 item['lng'],
                 item['lat'],
                 item['housearea'],
                 item['housedirect'],
                 item['housefloor'],
                 item['househall'],
                 item['balcony'],
                 item['bathroom'],
                 item['housepic'],
                 item['housearound'],
                 item['housestatus'],
                 item['housetype'],
                 item['ownertel'],
                 item['mantel']))
            self.conn.commit()
        except Exception as error:
            print(error)

        try:
            # table:housepic
            for imageurl in item['image_urls']:
                self.cursor.execute("insert into housepic(houseID, pic) values(%s,%s)",
                                    (item['houseID'], imageurl))
                self.conn.commit()
        except Exception as error:
            print(error)

        try:
            # table:payment
            for i in range(len(item['payname'])):
                self.cursor.execute(
                    "insert into payment (houseID,payname,payrent,paydeposit,payservice) values(%s,%s,%s,%s,%s)",
                    (item['houseID'],
                     item['payname'][i],
                     item['payrent'][i],
                     item['paydeposit'][i],
                     item['payservice'][i]
                     ))
                self.conn.commit()
        except Exception as error:
            print(error)
        self.count += 1
        return item


def close_spider(self, spider):
    print(str(self.count))
    self.cursor.close()
    self.conn.close()

# class ImgPipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         for image_url in item['image_urls']:
#             yield Request(image_url)
#
#     # 当一个单独项目中的所有图片请求完成时
#     # item_completed()方法将被调用
#     def item_completed(self, results, item, info):
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem("Item contains no images")
#         item['image_paths'] = image_paths
#         return item
