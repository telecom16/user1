# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:10:15 2018

@author: wbh
"""

if __name__ == '__main__':
    baseurl = "https://search.51job.com/list/200200,000000,0000,00,9,99,java,2,{a}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    for i in range(1,11):
        url = baseurl.format(a=i)
        print(url)