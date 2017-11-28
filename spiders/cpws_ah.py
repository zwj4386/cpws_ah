# coding:utf-8
import scrapy
from lxml import etree
import time
import random
import sys
import pymysql
reload(sys)
sys.setdefaultencoding = 'utf-8'
from selenium import webdriver

conn = pymysql.connect(host='192.168.3.232', user='zwj', password='123456',db='caiji',charset='utf8')
cursor = conn.cursor()
sql_sel = 'select url from CPWSURL_AH where id=3'
cursor.execute(sql_sel)
rs = cursor.fetchall()
b = webdriver.Chrome()
for i in rs:
    url = 'http://openlaw.cn%s'%i
    print(url)
    c = b.get(url)
    print(c)
    print(type(c))
    seconds = random.randint(2,5)
    time.sleep(seconds)

    yzm = '//input[@name="j_validatecode"]'
    html = b.page_source
    etree = etree.HTML(html)
    name = etree.xpath('//h2[@class="entry-title"]')[0]
    tag = name.tag
    text = name.text
    date = ''.join(etree.xpath('//li[@class="ht-kb-em-date"]/text()'))
    court = ''.join(etree.xpath('//a[@class="url fn n"]/text()'))
    caseno = ''.join(etree.xpath('//li[@class="ht-kb-em-category"]/text()'))
    ptext = ''.join(etree.xpath('//div[@id="Litigants"]'))
    content = ''.join(etree.xpath('//div[@class="part"]')[2::])
    sql = 'insert into CPWS_AH(name,date,court,caseno,ptext,content) values("%s","%s","%s","%s","%s","%s")'%\
          (name, date,court,caseno,ptext,content)
    cursor.execute(sql)
    conn.commit()

b.close()
cursor.close()
conn.close()



