import requests, os
from pyquery import PyQuery as pq
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
# 这里我使用了代理  你可以去掉这个代理IP 我是为了后面大规模爬取做准备的
proxies = {
    'https': '218.75.69.50:39590'
}


# 请求网页 获取源码
def start_request(url):
    r = requests.get(url, headers=headers, proxies=proxies)
    # 这个网站页面使用的是GBK编码 这里进行编码转换
    r.encoding = 'GBK'
    html = r.text
    return html


# 解析网页 获取图片
def parse(text, i):
    doc = pq(text)
    # 锁定页面中的img标签
    images = doc('div.list ul li img').items()
    x = 1
    for image in images:
        # 获取每一张图片的链接
        img_url = image.attr('src')
        # 获得每张图片的二进制内容
        img = requests.get(img_url, headers=headers, proxies=proxies).content
        # 定义要存储图片的路劲
        # 创建目录
        dir_path = os.path.dirname(os.path.abspath(__file__)) + "\\image\\"
        imagspath = dir_path + '/imgs' + str(i)
        # 创建目录
        if not os.path.exists(imagspath):
            os.makedirs(imagspath)

        path = imagspath + "\\" + str(x) + ".jpg"
        # 将图片写入指定的目录 写入文件用"wb"
        with open(path, 'wb') as f:
            f.write(img)
            time.sleep(1)
            print("正在下载第{}页{}张图片".format(i, x))
            x += 1
    print("写入完成")


def main():
    url = "http://www.netbian.com"
    text = start_request(url)
    parse(text, 1)
    # 爬取指定范围页面
    for i in range(2, 100):
        urlnum = url + "/index_" + str(i) + ".htm"
        textnum = start_request(urlnum)
        parse(textnum, i)


if __name__ == "__main__":
    main()