import scrapy
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup
from scrapy.http import Request
from urllib import request


class Spider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['jianshu.com']
    start_urls = [
        'https://y.qq.com/portal/search.html#page=2&searchid=1&remoteplace=txt.yqq.top&t=lyric&w=%E5%91%A8%E6%9D%B0%E4%BC%A6']

    # 'https://www.jianshu.com/search?q=%E8%85%BE%E8%AE%AF%E9%9D%A2%E8%AF%95&page=1&type=note']
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # soup = BeautifulSoup(response.body, "html5lib")
        # print('===================================')
        # print(soup)
        # print('===================================')
        # self.logger.info("======================= 数据 =============================")
        # self.logger.info(soup.find_all(name='a', attrs={"class": "mod_tab__item js_tab", "data-tab": "song"})[0].text)
        # self.logger.info("======================= 数据 =============================")
        # self.logger.info(response.xpath('/html/body/div[1]/div/ul[1]/li[1]/a/text()').extract_first())
        # self.logger.info("======================= 数据 =============================")
        # self.logger.info(response.xpath('/html/body/div[3]/div/div/div[3]/a[1]/text()').extract_first())
        # self.logger.info("======================= 数据 =============================")
        page = '1'
        import random
        lyric_list = []
        album_list = []

        for page in range(1, 39):
            page = str(page)
            MusicJsonCallback = 'MusicJsonCallback' + str(random.random()).replace('0.', '') + str(random.randint(0, 9))
            url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&remoteplace=txt.yqq.lyric&searchid=96611612886809799&aggr=0&catZhida=1&lossless=0&sem=1&t=7&p=' + page + '&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&jsonpCallback=' + MusicJsonCallback + '&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
            lyric_list.append(url)
            # lyric_list.append(url)
        for page in [1, 2]:
            page = str(page)
            MusicJsonCallback = 'MusicJsonCallback' + str(random.random()).replace('0.', '') + str(random.randint(0, 9))
            albumUrl = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&remoteplace=txt.yqq.album&searchid=85789223018125214&aggr=0&catZhida=1&lossless=0&sem=10&t=8&p=' + page + '&n=30&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&jsonpCallback=' + MusicJsonCallback + '&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
            album_list.append(url)
        # url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

        # ct = 24
        # qqmusic_ver = 1298
        # remoteplace = txt.yqq.lyric
        # searchid = 96611612886809799
        # aggr = 0
        # catZhida = 1
        # lossless = 0
        # sem = 1
        # t = 7
        # p = 1
        # n = 10
        # w = % E5 % 91 % A8 % E6 % 9
        # D % B0 % E4 % BC % A6
        # g_tk = 5381
        # jsonpCallback = MusicJsonCallback5790888689515912
        # loginUin = 0
        # hostUin = 0
        # format = jsonp
        # inCharset = utf8
        # outCharset = utf - 8
        # notice = 0
        # platform = yqq
        # needNewCode = 0
        '============================================================='

        '==========================================================='
        # ct=24
        # qqmusic_ver=1298
        # remoteplace=sizer.yqq.lyric_next
        # searchid=107388218416869438
        # aggr=0
        # catZhida=1
        # lossless=0
        # sem=1
        # t=7
        # p=3
        # n=10
        # w=%E5%91%A8%E6%9D%B0%E4%BC%A6
        # g_tk=5381
        # jsonpCallback=MusicJsonCallback6599093897242113
        # loginUin=0
        # hostUin=0
        # format=jsonp
        # inCharset=utf8
        # outCharset=utf-8
        # notice=0
        # platform=yqq
        # needNewCode=0'
        '=================================== album =============================================='
        # ct=24
        # qqmusic_ver=1298
        # remoteplace=txt.yqq.album
        # searchid=85789223018125214
        # aggr=0
        # catZhida=1
        # lossless=0
        # sem=10
        # t=8
        # p=1
        # n=30
        # w=%E5%91%A8%E6%9D%B0%E4%BC%A6
        # g_tk=5381
        # jsonpCallback=MusicJsonCallback6276278540441055
        # loginUin=0
        # hostUin=0
        # format=jsonp
        # inCharset=utf8
        # outCharset=utf-8
        # notice=0
        # platform=yqq
        # needNewCode=0
        #

        # song
        # https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6
        #
        # lyric
        # https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=lyric&w=%E5%91%A8%E6%9D%B0%E4%BC%A6
        #
        # album
        # https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=album&w=%E5%91%A8%E6%9D%B0%E4%BC%A6
        #
        # mv
        # https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=mv&w=%E5%91%A8%E6%9D%B0%E4%BC%A6


        # return [scrapy.FormRequest(url=albumUrl,
        #                            callback=self.parseAlbum, dont_filter=True
        #                            )]

        for url in album_list:
            yield Request(url=url, method='GET',  # GET or POST
                          callback=self.parseAlbum, dont_filter=True)

        # for url in lyric_list:
        #     yield Request(url=url, method='GET',  # GET or POST
        #                   callback=self.parseLyric, dont_filter=True)

    def parseAlbum(self, response):
        base_img_url = 'https://y.gtimg.cn/music/photo_new/T002R300x300M000'

        print('===================================')
        print('===================================')
        album = (response.body.decode('UTF-8'))
        print(album)
        first = album.find('(') + 1
        last = album.rfind(')')
        album = album[first:last]

        import json
        from datetime import datetime
        json_album = json.loads(album)
        # print(json_album['data'])
        print(json_album['data']['zhida'])
        print(json_album['data']['keyword'])
        for album in json_album['data']['album']['list']:
            singers = ''
            for singer in album['singer_list']:
                singers += singer['name']

            print('歌手：' + singers)
            publicTime = album['publicTime']
            print('发行时间：' + publicTime)
            albumName = album['albumName']
            print('专辑名称：' + albumName)
            singerName = album['singerName']
            print('singerName：' + singerName)
            albumMID = album['albumMID']
            print('albumMID：' + albumMID)
            albumImg = albumName + '.jpg'
            jpg_link = base_img_url + albumMID + '.jpg'
            print(albumImg)
            print(jpg_link)
            request.urlretrieve(jpg_link, './img/' + albumImg)
            print('=====================================')
            # print(album)
        print('=====================================')

    def parseLyric(self, response):
        print('===================================')
        print('===================================')
        lyric = (response.body.decode('UTF-8'))
        first = lyric.find('(') + 1
        last = lyric.rfind(')')
        lyric = lyric[first:last]
        import json
        from datetime import datetime
        json_lyric = json.loads(lyric)
        # print(json_lyric)
        print('=====================================')
        print()
        for song in json_lyric['data']['lyric']['list']:
            print('专辑名称：' + song['albumname'])
            ts = int(song['pubtime'])
            pubtime = datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            print('发行时间：' + pubtime)

            print('歌名：' + song['songname'])
            singers = ''
            for singer in song['singer']:
                singers += singer['name']
            print('歌手：' + singers)
            print(song['lyric'].replace('<em>', '').replace('</em>', ''))
            content = song['content'].replace('<em>', '').replace('</em>', '')
            print(content)
            print('================================================')
            filename = 'lyric/' + song['songname'] + "-" + pubtime + '.txt'
            # self.mkdir(filename)

            with open(filename, 'w') as file_to_w:
                file_to_w.write(content.replace("\\n", '\r\n'))

    def mkdir(self, path):
        # 引入模块
        import os
        os.mknod()
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")

        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)

        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.mknod(path)
            print(path + ' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(path + ' 目录已存在')
            return False
