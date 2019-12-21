# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os
import csv
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
from datetime import datetime
class Imagescrap2Pipeline(ImagesPipeline):
    def file_path(self, request, response=None  , info=None ):
        
        # print (response)
        # print("Printing Request Url ")
        # print(request.url)
        image_guid = request.url.split('/')[-1]
        
        return request.meta.get('filename','')

    def get_media_requests(self, item, info):
        now = datetime.now()
        meta = {'filename': "/full/"+str(item['count'])+"_"+item['s'].replace(' ','_').replace(':','_')+".jpg"}
        yield Request(url=item['src_link'],meta=meta)

    # def item_completed(self, results, item, info):
      
        
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     print("------------------------")
    #     print(image_paths)
    #     if not image_paths:
    #         raise DropItem("Item contains no images")
    #     return item
   
