# scrapy
关于 scrapy 的各种初体验，本项目会持续更新，直到 scrapy 系列推文结束更新。

## 关注公众号【zone7】，获取最新推文。
![zone7](https://github.com/zonezoen/blog/blob/master/img/zone_qrcode.jpg)


## doubanTop250 | 豆瓣爬虫
此项目为 scrapy 初体验源码，关于豆瓣电影 Top 250 的爬虫文章，
相应的文章地址为：
- [爬虫利器初体验(1)](https://mp.weixin.qq.com/s/PIm98MmK2NUDip_WBhcv5Q)
- [听说你的爬虫又被封了(2)](https://mp.weixin.qq.com/s/8y4LWFYDTULYcFNlxKzAxA)
- [爬取数据不保存，就是耍流氓(3)](https://mp.weixin.qq.com/s/9hHteZdZDFFmH16kM_nHhQ)

## rentHouseScrapy | 租房爬虫
此项目为 scrapy 实战文章。
### 如何启动项目？
此项目为 scrapy 实战文章，关于房天下广州租房数据的爬取与分析
相应的文章地址为：
- [爬取两万多租房数据，告诉你广州房租现状(4)](https://mp.weixin.qq.com/s/PhMocfb54ZHCFAwdyUe99Q)

开始抓取：

clone 当前项目到你的电脑，安装好相应的依赖包，配置好数据库 ip 地址、账号、密码。
进入到 rentHouseScrapy 目录，运行目录：
```
scrapy crawl ftx
```
分析数据：

数据抓取完毕之后，进入到 analysis 目录下，直接运行文件，即可开始数据分析。

### 如何修改成自己所在城市的爬虫？`
修改 baseUrl = "http://gz.zu.fang.com/" 成你对应城市的地址就行。

## girlScrapy | 妹子图
关于 scrapy 爬取图片的教程。此项目爬取了妹子图网站。
- [scrapy 也能爬取妹子图？(5)](https://mp.weixin.qq.com/s/427RSw9wBTzRVJi6w_PbGw)


## splashScrapy | 爬取QQ音乐周杰伦歌词与专辑
入口：直接运行 main.py 即可

相应的文章地址为：
- [scrapy遇上ajax，爬取QQ音乐周杰伦歌词与专辑(6)](https://mp.weixin.qq.com/s/BT7Chf2hN_53hG40m2SAWw)

## doubanScrapyRedis | 分布式爬虫
入口：直接运行 main.py 即可(请配置好你本地的 redis 数据库)
