import scrapy
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup
from scrapy.http import Request
from urllib import request


class Spider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://y.qq.com/portal/search.html#page=2&searchid=1&remoteplace=txt.yqq.top&t=lyric&w=%E5%91%A8%E6%9D%B0%E4%BC%A6']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        page = '1'
        import random
        lyric_list = []
        for page in [1]:
            page = str(page)
            MusicJsonCallback = 'MusicJsonCallback' + str(random.random()).replace('0.', '') + str(random.randint(0, 9))
            url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&remoteplace=txt.yqq.lyric&searchid=96611612886809799&aggr=0&catZhida=1&lossless=0&sem=1&t=7&p=' + page + '&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&jsonpCallback=' + MusicJsonCallback + '&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
            lyric_list.append(url)
            # lyric_list.append(url)
        albumUrl = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&remoteplace=txt.yqq.album&searchid=85789223018125214&aggr=0&catZhida=1&lossless=0&sem=10&t=8&p=' + page + '&n=30&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&jsonpCallback=' + MusicJsonCallback + '&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
        albumUrl = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&remoteplace=txt.yqq.album&searchid=86509927134253293&aggr=0&catZhida=1&lossless=0&sem=10&t=8&p=' + page + '&n=30&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&jsonpCallback=' + MusicJsonCallback + '&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'

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

        return [scrapy.FormRequest(url=albumUrl,
                                   callback=self.parseAlbum, dont_filter=True
                                   )]
        # yield Request(url=albumUrl, method='GET',  # GET or POST
        #               callback=self.parseAlbum, dont_filter=True)
        for url in lyric_list:
            yield Request(url=url, method='GET',  # GET or POST
                          callback=self.parseLyric, dont_filter=True)

    def parseAlbum(self, response):
        base_img_url = 'https://y.gtimg.cn/music/photo_new/T002R300x300M000'
        album = (response.body.decode('UTF-8'))
        print(album)
        first = album.find('(') + 1
        last = album.rfind(')')
        album = album[first:last]

        import json
        json_album = json.loads(album)
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

    def parseLyric(self, response):
        lyric = (response.body.decode('UTF-8'))
        first = lyric.find('(') + 1
        last = lyric.rfind(')')
        lyric = lyric[first:last]
        import json
        from datetime import datetime
        json_lyric = json.loads(lyric)
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
            with open(filename, 'w') as file_to_w:
                file_to_w.write(content.replace("\\n", '\r\n'))
