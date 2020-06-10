# -*- coding: UTF-8 -*-
import urllib.request
from main import Analyze

class GetImage:
    def __init__(self):
        #print('get image')
        pass

    def getImage(self, url):
        anl = Analyze()
        
        urllib.request.urlretrieve(url, "images/0.jpg")
        return anl.analyze()


#urllib.request.urlretrieve("http://192.168.0.7/images/0.jpg", "images/0.jpg")

#urllib.request.urlretrieve("https://s.pstatic.net/static/newsstand/2020/0526/article_img/new_main/9066/203949_001.jpg", "images/0.jpg")
