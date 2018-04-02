+import urllib
from urllib.parse import *
from bs4 import BeautifulSoup
import string
import random
import pandas as pd
import os
import time
import socket


headers = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; rv:27.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:27.0) Gecko/20100101 Firfox/27.0"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:10.0) Gecko/20100101 Firfox/10.0"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/21.0.1180.110 Safari/537.36"
    "Mozilla/5.0 (X11; Ubuntu; Linux i686 rv:10.0) Gecko/20100101 Firfox/27.0"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/34.0.1838.2 Safari/537.36"
    "Mozilla/5.0 (X11; Ubuntu; Linux i686 rv:27.0) Gecko/20100101 Firfox/27.0"
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    ]
random_header = random.choice(headers)


#ip_list = ['118.114.77.47:8080', '140.143.96.216:80', '222.185.184.183:6666', '171.13.37.199:34493']  # 代理IP列表

#proxy_support = urllib.request.ProxyHandler({'http': random.choice(ip_list)})  #
#opener = urllib.request.build_opener(proxy_support)
#opener.addheaders = [('User-Agent', random_header)]
#urllib.request.install_opener(opener)  #


def get_content(url, headers):
    random_header = random.choice(headers)

    req = urllib.request.Request(url)
    req.add_header("User-Agent", random_header)
    req.add_header("Get", url)
    req.add_header("Host", "sou.zhaopin.com")
    req.add_header("refer", "http://sou.zhaopin.com/")
    html = urllib.request.urlopen(req)
    contents = html.read().decode('utf-8')
    return (contents)


def get_content1(url, headers):
    '''''
    @url：需要登录的网址
    @headers：模拟的登陆的终端
    *********************模拟登陆获取网址********************
    '''

    headers1={
        "User-Agent": random_header,
        "Get":url,
#        "Host":"jobs.zhaopin.com",
        "refer": "http://sou.zhaopin.com/jobs/searchresult.ashx"
    }

    req = urllib.request.Request(url,headers=headers1)
#    try:
    html = urllib.request.urlopen(req)#, timeout=30)
#    except urllib.error.URLError as e:
#        print (type(e))  # not catch
#        if e.message=='time out':
#            continue
#    except socket.timeout as e:
#        print (type(e))

#    print(html.read().decode('utf-8'))
    contents = html.read().decode('utf-8')
    html.close()#关闭网页
    time.sleep(3)#设置三秒间隔，以防封IP
    return (contents)


def get_links_from(job, city, page):
    #模拟登陆获取待爬取网页，[1，page）
    urls = []

    for i in range(1,page):
        url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl={}&kw={}&p={}".format(str(city), str(job), i)
        url = quote(url, safe=string.printable)
        info = get_content(url, headers)
        soup = BeautifulSoup(info, "lxml")  # 设置解析器为“lxml”
        link_urls = soup.select('td.zwmc a')
        for url in link_urls:
            urls.append(url.get('href'))
        print(i)#打印已获取网页链接页数
    true_url=[]
    for i in range(len(urls)):
        if urls[i]!='http://e.zhaopin.com/products/1/detail.do':
            true_url.append(urls[i])
    print(true_url)#打印待爬取网页网址
    return (true_url)


def get_link_info(url):
    #获取数据并存储到data字典中
    info = get_content1(url, headers)
    soup = BeautifulSoup(info, "lxml")  # 设置解析器为“lxml”
#    print(soup)
    occ_name = soup.select('div.fixed-inner-box h1')[0]
    print(occ_name.text)
    com_name = soup.select('div.fixed-inner-box h2')[0]
#    print(com_name.text.strip())
    com_url = soup.select('div.inner-left.fl h2 a')[0]
#    print(com_url.get('href'))
    welfare = soup.select('div.welfare-tab-box')[0]
#    print(welfare.text.strip())
    wages = soup.select('div.terminalpage-left strong')[0]
#    print(wages.text.strip())
    date = soup.select('div.terminalpage-left strong')[2]
#    print(date.text.strip())
    exper = soup.select('div.terminalpage-left strong')[4]
#    print(exper.text.strip())
    num = soup.select('div.terminalpage-left strong')[6]
#    print(num.text.strip())
    area = soup.select('div.terminalpage-left strong')[1]
#    print(area.text.strip())
    nature = soup.select('div.terminalpage-left strong')[3]
#    print(nature.text.strip())
    Edu = soup.select('div.terminalpage-left strong')[5]
#    print(Edu.text.strip())
    cate = soup.select('div.terminalpage-left strong')[7]
#    print(cate.text.strip())
    com_scale = soup.select('ul.terminal-ul.clearfix li strong')[8]
#    print(com_scale.text.strip())
    com_nature = soup.select('ul.terminal-ul.clearfix li strong')[9]
#    print(com_nature.text.strip())
    com_cate = soup.select('ul.terminal-ul.clearfix li strong')[10]
#    print(com_cate.text.strip())
    com_address = soup.select('ul.terminal-ul.clearfix li strong')[11]
#    print(com_address.text.strip())
    job_duties =soup.select('div.tab-inner-cont')[0]
#    print(job_duties.text.strip())

    data = {
        "网址": url,
        "工作名称": occ_name.text.strip(),
        "公司名称": com_name.text,
        "公司网址": com_url.get('href'),
        "福利": welfare.text.strip(),
        "月工资": wages.text.strip(),
        "发布日期": date.text.strip(),
        "经验": exper.text.strip(),
        "人数": num.text.strip(),
        "工作地点": area.text.strip(),
        "工作性质": nature.text.strip(),
        "最低学历": Edu.text.strip(),
        "职位类别": cate.text.strip(),
        "公司规模": com_scale.text.strip(),
        "公司性质": com_nature.text.strip(),
        "公司行业": com_cate.text.strip(),
        "公司地址": com_address.text.strip(),
        '工作职责':job_duties.text.strip()
    }
    return (data)


def get_links_all_info(job, city, page):
    #将数据存储到dataframe中
    urls = get_links_from(job, city, page)
#    print(urls)
    df = pd.DataFrame({
        "网址": [],
        "工作名称": [],
        "公司名称": [],
        "公司网址": [],
        "福利": [],
        "月工资": [],
        "发布日期": [],
        "经验": [],
        "人数": [],
        "工作地点": [],
        "工作性质": [],
        "最低学历": [],
        "职位类别": [],
        "公司规模": [],
        "公司性质": [],
        "公司行业": [],
        "公司地址": []
    })
    links = []
    for url in urls:
        if "xiaoyuan" in url:
            links.append(url)
#            columns = ['校园招聘地址']
#            labeled_df = pd.DataFrame(columns=columns, data=links)
#            labeled_df.to_csv('{}\{}校园招聘{}地址.csv'.format(str(city)+str(job),str(city),str(job)))
        elif 'http://jobs.zhaopin.com/136410592' in url:
            links.append(url)
        elif url=='http://jobs.zhaopin.com/481439182250017.htm':
            links.append(url)
        elif url=='http://jobs.zhaopin.com/135109588255621.htm':
            links.append(url)#存在定制招聘网站导致以上数据解析方法不适用，加入links列表
        else:
            print(url)
            data = get_link_info(url)
#           print (data)
            df = df.append(data, ignore_index=True)
#    print(links)
    return df


def remove_useless_info(df):
#    '''''
#    #删除除"公司规模": "20人以下", "20-99人"; "最低学历": "博士","大专"; "经验": "3-5年","5-10年", "10年以上"的情况

#    @Dataframe筛选数据 http://jingyan.baidu.com/article/0eb457e508b6d303f0a90572.html
#    @df: 以矩阵形式存储爬取到的数据
#   定义一个列表，存储指定列类型，
#    删除需要删除的类型，
#    利用isin()函数保留剩下的数据
#    '''
#    '''''
#    **************公司规模问题**************

#    **************最低学历问题**************

#    **************经验问题**************
#    '''
    df = df[(df.经验 != '3-5年') & (df.经验 != '5-10年') & (df.经验 != '10年以上') & (df.最低学历 != '博士') & (df.最低学历 != '大专') & (df.公司规模 != '20人以下')]
    return df


def get_recuite_info(job, city, page):
    '''''
    获取招聘信息
    '''
    df = get_links_all_info(job, city, page)
#    df = remove_useless_info(df) #数据预处理，清洗。
    df.to_csv(('shanghai{}.csv').format(str(page)))



''''' 
*********************获取招聘信息*************************** 
'''

get_recuite_info('人工智能','上海',15 )
#    for page in range(1,9):
#        print('第{}页下载完毕。'.format(str(page)))
#        time.sleep(5)
#    get_recuite_info('人工智能', '广东', 1)
