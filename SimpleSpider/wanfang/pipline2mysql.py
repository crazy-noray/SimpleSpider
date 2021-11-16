#_*_ coding:utf-8
import pymysql


class wanfangPipline(object):
    def process_item(self, item, spider):
        db = pymysql.connect('localhost', 'root', '123456', 'wanfang')

        cur = db.cursor()

        sql = "insert into article(title,link,pubdate,publisher,authors )values('{0}','{1}','{2}','{3}', '{4}')".format(item['title'], item['link'][0],item['pubdate'][0],item['publisher'][0], item['author'][0])

        try:
            cur.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            db.close()
        return item
            