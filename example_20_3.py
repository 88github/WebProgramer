#coding=utf-8

'''
    20170716
    why
    Learning:
    文件对象提供了三个“读”方法： .read()、.readline() 和 .readlines()。
    每种方法可以接受一个变量以限制每次读取的数据量，但它们通常不使用变量。
    .read() 每次读取整个文件.
    .readline()每次只读取一行.
    .readlines()读取整个文件,自动将文件内容分析成一个行的列表
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
