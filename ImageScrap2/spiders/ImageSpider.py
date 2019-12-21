import scrapy
from ImageScrap2.items import ImdbItem

class ImageSpider(scrapy.Spider):
    name="ImageSpider"

    def start_requests(self):
        urls = ["https://www.imdb.com/chart/top"]
        for url in urls:
            yield scrapy.Request(url=url , callback=self.parse)

    def parse(self,response):
        links = response.xpath('//tbody[@class="lister-list"]/tr/td[@class="titleColumn"]/a/@href').extract()
        print(len(links))
        i=1
        ocd = list();
        for link in links: 
            
            
            #print(response.xpath('//tbody[@class="lister-list"]/tr['+str(i)+']/td[@class="titleColumn"]/a/text()').extract())
            imgTitle = response.xpath('//tbody[@class="lister-list"]/tr['+str(i)+']/td[@class="titleColumn"]/a/text()').extract()
            
            item = ImdbItem()
            #item["MovieName"] = response.xpath('//tbody[@class="lister-list"]/tr['+str(i)+']/td[@class="titleColumn"]/a/text()').extract()
            # relativeUrl= response.xpath('//tbody[@class="lister-list"]/tr['+str(i)+']/td[@class="posterColumn"]/a/img/@src').extract()
            relativeUrl = response.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr['+str(i)+']/td[1]/a/img/@src').extract()
            print(relativeUrl)
            # item["image_urls"] = self.url_join(relativeUrl, response)
            # item["image_name"]  = imgTitle
            # item["image_paths"]  = imgTitle
            #absUrl = 
            item['host']=self.name
            item['s']=imgTitle[0]
            item['src_link']= self.url_join(relativeUrl, response)[0]
            item['count'] = i
            ocd.append(item);
            
            i=i+1
            
            
        return ocd

    def url_join(self, urls, response):
        joined_urls = []
        for url in urls:
            joined_urls.append(response.urljoin(url))

        return joined_urls