from urllib import request
from bs4 import BeautifulSoup
import time

def test():
    url = 'http://cip.cc/'
    #这是代理IP
    proxy = {'http':'127.0.0.1:8888'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装OPener
    request.install_opener(opener)
    #使用自己安装好的Opener
    response = request.urlopen(url)
    #读取相应信息并解码
    # soup = BeautifulSoup(response, 'lxml')
    # message = soup.find(class_=)
    html = response.read().decode("utf-8")
    #打印信息
    soup = BeautifulSoup(html, 'lxml')
    message = soup.find(class_='data kq-well').pre.text
    return message

if __name__ == "__main__":
    #访问网址
    for i in range(0, 6):
    	print(f'====================代理IP= {i} ==============')
    	print(test())
    	time.sleep(2)