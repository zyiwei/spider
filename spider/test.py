#-*- coding=utf8 -*-
import importlib,sys
importlib.reload(sys)
import time
import re
import sqlite3
from selenium import webdriver
from bs4 import BeautifulSoup


conn=sqlite3.connect('test.db')
cur=conn.cursor()


def store(idnum,title,link):
    cur.execute("insert into posts (id,title,link) values (?,?,?)",[idnum,title,link])
    cur.connection.commit()


driver=webdriver.PhantomJS(executable_path="../phantomjs-2.1.1-macosx/bin/phantomjs")
driver.get("http://bbs.uestc.edu.cn/member.php?mod=logging&action=login")

username=driver.find_element_by_name("username")
password=driver.find_element_by_name("password")
username.send_keys('zhangyiwei')
password.send_keys('711944ABcde')
submit=driver.find_element_by_name("loginsubmit")
submit.click()

time.sleep(5)

driver.get("http://bbs.uestc.edu.cn/forum.php?mod=forumdisplay&fid=61")
pageSource=driver.page_source
bsObj=BeautifulSoup(pageSource,"html.parser")

total=int(bsObj.find("a",{"class":"last"}).get_text()[4:])


loopflag=0
idnum=0
while loopflag<total:
    loopflag=loopflag+1
    if loopflag==1146:
        continue

    driver.get("http://bbs.uestc.edu.cn/forum.php?mod=forumdisplay&fid=61&page=%s"%loopflag)
    page=driver.page_source.encode('utf-8')
    bsObj=BeautifulSoup(page,"html.parser")
    tbodys=bsObj.findAll("tbody",{"id":re.compile("^(normalthread_).*$")})
    for tbody in tbodys:
        idnum=idnum+1
        aim=tbody.find("a",{"class":"s xst"})
        title=aim.get_text()
        link=aim.attrs['href']
        store(idnum,title,link)
    print(loopflag)

print(total)

cur.close()
conn.close()


























