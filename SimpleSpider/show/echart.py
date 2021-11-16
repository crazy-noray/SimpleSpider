# coding: utf-8

import xlrd
import os
os.chdir('D:\\scrapy\\wanfang\\')

data = xlrd.open_workbook('key_rate.xls')
table = data.sheet_by_index(0)
rate = table.col_values(0)
key_word = table.col_values(1)

from pyecharts import Bar
bar = Bar()
bar.add('词频', rate, key_word)
bar.show_config()
bar.render()