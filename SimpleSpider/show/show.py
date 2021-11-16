import xlrd
import os

os.chdir('D:\\scrapy\\wanfang\\')

data = xlrd.open_workbook('key_rate.xls')

table = data.sheet_by_index(0)

rate = table.col_values(0)
key_word = table.col_values(1)

with open('rate_key.txt','w')as f:
    for i in range(1, len(rate)):
        f.write('<a title="%s" class="font_color_%d">%s</a>\n '%(key_word[i],i%10+1,rate[i]))
    
print('生成完成！')

