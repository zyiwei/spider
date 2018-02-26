# 电子科技大学清水河畔二手帖子爬虫与搜索
学校p2p项目时做的，花了好几个小时才弄懂python3处理网页编码问题。
（注：由于python3处理编码时的便捷，服务端程序使用py3虚拟环境；但由于pythonweb的flask框架兼容问题，web 使用py2虚拟环境）

### 程序运行演示

激活服务端虚拟环境：
$ source venv3/bin/activate

运行爬虫，将网络数据写入数据库：
$ cd spider

$ python test.py

（等待几个小时后。。。）

进入数据库，查看数据：
$ sqlite3 test.db

>select * from posts;
...
...
...

>.quit

退出服务端虚拟环境：
$ deactivate

激活web运行虚拟环境：
$ cd ..

$ source venv/bin/activate

运行客户端服务器：
$ python spider.py

打开浏览器体验，输入地址 http://127.0.0.1:5000/ 体验功能
