# -*- coding: utf-8 -*-

# Scrapy settings for doubanTop250 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'doubanTop250'

SPIDER_MODULES = ['doubanTop250.spiders']
NEWSPIDER_MODULE = 'doubanTop250.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent

import random

# user agent 列表
MY_USER_AGENT = [
    'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
    'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
    'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
    'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
    'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
    'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
    'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
    'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'
]

PROXIES = [
    "194.186.20.62:21231"
    , "66.153.222.162:54684"
     # "219.234.5.128:3128"
    # , "117.114.149.66:53281"
    # , "117.114.149.66:53281"
           ]
# 随机生成user agent
# USER_AGENT = random.choice(MY_USER_AGENT)


# Obey robots.txt rules
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'DEBUG'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3  # 每次请求间隔时间 秒
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    "Accept-Language": 'zh-CN,zh;q=0.9',
    "Cache-Control": 'max-age=0',
    "Connection": 'keep-alive',
    "Cookie": 'bid=IFBAuOvTPyM; ll="118288"; __yadk_uid=dVfN4bCOe5mDRkH2SUgZhCQVltk9xQfZ; _vwo_uuid_v2=D03805B24722C4F1FA0973E68D7754203|5063bcd155fdd64889548648e2688aec; douban-fav-remind=1; _pk_ses.100001.4cf6=*; ap_v=0,6.0; ps=y; dbcl2="187514772:Ato9/Z8an7w"; ck=VJ5Y; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=3f7c89dacd2a36d4.1542519399.5.1542543636.1542539644.',
    "Host": ' movie.douban.com',
    "Upgrade-Insecure-Requests": ' 1',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'doubanTop250.middlewares.Doubantop250SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'doubanTop250.middlewares.MyUserAgentMiddleware': 300,
    # 'doubanTop250.middlewares.ProxyMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'doubanTop250.pipelines.Doubantop250Pipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# """ 启用限速设置 """
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 0.3  # 初始下载延迟
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
