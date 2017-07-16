#coding=utf-8

'''
    20170716
    why
    python example_20_2.py http://www.baidu.com
'''

from sys import argv
from urllib import urlretrieve

local = 'D://it/Python/HTTP_Client/cgi-bin/'

def cbk(a, b, c):
    '''回调函数
    @a: 已经下载的数据块
    @b: 数据块的大小
    @c: 远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per

def getPage(url):
    localNew = local + url[7:] + '.html'
    print localNew
    try:
        retval = urlretrieve(url, localNew, cbk)  # 直接将远程数据下载到本地。
    except IOError:
        retval = ('*** Error: invaild URL')
    return retval  # 修改错误处

def main():
    if len(argv) > 1:
        url = argv[1]
    else:
        try:
            url = raw_input("Please a url:")
        except(KeyboardInterrupt):
            url = ''
    if not url:
        return
    getPage(url)

if __name__ == '__main__':
    main()