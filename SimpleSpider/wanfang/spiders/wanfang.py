# -*- coding: utf-8 -*-
import scrapy
from wanfang.items import WanfangItem

class WanfangSpider(scrapy.Spider):
    name = 'wanfang'
    allowed_domains = ['www.wanfangdata.com.cn']
    start_urls = ["http://s.wanfangdata.com.cn/Paper.aspx?q=OpenCV&f=top&p=1"]



    def parse(self, response):

        for item in response.xpath("//div[@class='left-record']"):
            article = WanfangItem()
            # 提取title
            article['title'] = item.xpath("div[@class='record-title']/a/text()").extract()
            name = ''
            for i in range(1, len(article['title'])):
                if article == '全文' or article == '目录':
                    article['title'][i] = ' '
                if(i == len(article['title'])-1):
                    name += 'OpenCV'   
                name += article['title'][i]
            article['title'] = name

            # 提取链接
            article['link'] = item.xpath("div[@class='record-title']/a/@href").extract()

            # 提取出版社
            article['publisher'] = item.xpath("div[@class='record-subtitle']/a[1]/text()").extract()

            # 提取出版时间
            article['pubdate'] = item.xpath("div[@class='record-subtitle']/a[2]/text()").extract()

            print(type(article['publisher']))
            
            #提取作者
            article['author'] = item.xpath("div[@class='record-subtitle']/a[@class='creator']/text()").extract()
            print(article['author'])
            

            yield article
        nextPage = response.xpath("//p[@class='pager']/a[@class='page'][5]/@href")
        
        if nextPage:
            url = response.urljoin(nextPage[0].extract())
            yield scrapy.Request(url, self.parse, dont_filter=True)

