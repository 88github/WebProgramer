#coding=utf-8

'''
    20170716
    why
'''

from urllib import urlopen

def firstNoneBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():    #strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
            continue
        else:
            return eachLine

def firstLast(webpage):
    print firstNoneBlank(webpage)
    webpage.reverse() #reverse() 函数用于反向列表中元素。
    print firstNoneBlank(webpage)

def download(url="http://www.baidu.com", process = firstLast):
    try:
        retval = urlopen("http://www.baidu.com").readlines()
    except IOError:
        retval = None
    if retval:
        process(retval)

if __name__ == '__main__':
    download()

'''
    11.4
def firstNoneBlank(lines):
for eachLine in lines:
    if not eachLine.strip():    #strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
        continue
    else:
        return eachLine

def firstLast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print firstNoneBlank(lines)
    lines.reverse() #reverse() 函数用于反向列表中元素。
    print firstNoneBlank(lines)

def download(url='http://www.baidu.com', process = firstLast):
    try:
        retval = urlretrieve(url)[0]
        print 'retval:' + retval
    except IOError:
        retval = None
    if retval:
        process(retval)

if __name__ == '__main__':
    download()
'''
