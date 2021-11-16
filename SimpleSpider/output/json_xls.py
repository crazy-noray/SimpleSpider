# _*_ coding:utf-8

import xlwt
import json

file = xlwt.Workbook(encoding='utf-8')
table = file.add_sheet('data', cell_overwrite_ok=True)
table_name = [
    '序号','标题','链接','出版日期 ','作者','出版社'
]
for i in range(0, len(table_name)):  
    table.write(0, i, table_name[i])
    

with open("D:\\scrapy\\wanfang\\wanfang\\output\\article_20180927.json", "r", encoding='utf-8') as f:
    i = 1
    for line in f.readlines():
        one_art =  json.loads(line)
       
        table.write(i, 0, i)
        table.write(i, 1, one_art['title'])
        table.write(i, 2, one_art['link'])
        table.write(i, 3, one_art['pubdate'])
        table.write(i, 4, one_art['author'])
        table.write(i, 5, one_art['publisher'])
        i += 1
file.save('data.xls')

print('数据已经被保存在D:\\scrapy\\wanfang\\data.xls')       

