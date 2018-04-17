# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:00:17 2018

@author: Administrator
"""

import requests
from lxml import etree
def getNewsUrlList(url):
    x = requests.get(url)
    html = x.content.decode('gbk')
    selector = etree.HTML(html)
    contents = selector.xpath("//div[@id='resultList']/div[@class='el']/span[@class='t3']/text()")
    print(contents)
        
        
if __name__ == '__main__':
    baseurl = 'https://search.51job.com/list/200200,000000,0000,00,9,99,java,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    getNewsUrlList(baseurl)