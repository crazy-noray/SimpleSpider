# _*_ coding:utf-8
import os
import json
import time


class WanfangPipeline(object):

    #构造函数
    def __init__(self):
        self.sourceFolder = 'output'

        if not os.path.exists(self.sourceFolder):
            os.mkdir(self.sourceFolder)

    def process_item(self, item, spider):
        now = time.strftime('%Y%m%d', time.localtime())
        jsonFileName = 'article_'+now+'.json'

        with open(self.sourceFolder+os.sep+jsonFileName, 'a') as file:
            data = json.dumps(dict(item), ensure_ascii=False) + '\n'
            file.write(data)
        return item 
