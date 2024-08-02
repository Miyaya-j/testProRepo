from urllib import request
from urllib import parse

word = input('请输入搜索内容:')
def getfull_url(url1):
    url = url1
    #想要搜索的内容
    params = parse.quote(word)
    full_url = url.format(params)
    return full_url
    print(full_url)

def gethtml(full_url):
    #重构请求头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
    #创建请求对应
    req = request.Request(url=full_url,headers=headers)
    #获取响应对象
    res = request.urlopen(req)
    #获取响应内容
    html = res.read().decode("utf-8")
    return html
    #print(html)

def savefile(html):
    filename = word + '2.html'
    with open(filename,'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    full_url = getfull_url('http://www.baidu.com/s?wd={}')
    html = gethtml(full_url=full_url)
    savefile(html)