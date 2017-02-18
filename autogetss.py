import json
import requests 
from bs4 import BeautifulSoup
import hashlib
import random
import base64

configs=[]
guiconfig=[]

def getHtmltext(url):
    """从URL中获取纯文本信息"""
    print('正在从 '+url+' 获取信息……')
    htmltempdata = requests.get(url).text
    print('获取信息完毕！')
    return htmltempdata
    
def getRandomMd5():
    """生成随机MD5作为ID"""
    hash = hashlib.md5()
    hash.update(str(random.random()).encode('utf-8'))
    return hash.hexdigest().upper()
    
def getBase64(src):
    '''返回字符串的base64编码'''
    return base64.b64encode(src.encode(encoding="utf-8")).decode()
    
def getConfig(htmldata):
    '''解析数据提取信息'''
    print('正在解析数据……')
    soup = BeautifulSoup(htmldata,'html.parser')
    #soup.findAll('span',style="color: #ff6464;")[2].find('strong').text.split("\n")[0]
    updatetime=soup.findAll('span',style="color: #ff6464;")[2].find('strong').text.split("\n")[0]
    print('更新日期：'+str(updatetime))
    tabledata = soup.find('table',width="100%")
    trs = tabledata.findAll('tr')[1:] #去掉首行
    for tr in trs:
        config={}
        tds=tr.findAll('td')
        if 'del' in str(tds[1]):
            continue
        if 'ssr://' in str(tds[6]):#去除ssR链接
            continue
        config['remarks']=tds[0].getText()
        config['id']=getRandomMd5()
        config['server']=tds[1].getText()
        config['server_port']=tds[2].getText()
        config['server_udp_port']=0
        config['password']=tds[3].getText()
        config['method']=tds[4].getText()
        config['protocol']='origin'
        config['protocolparam']=''
        config['obfs']='plain'
        config['obfsparam']=''
        config['remarks_base64']=getBase64(config['remarks'])
        config['group']='doub.io'
        config['enable']=True
        config['udp_over_tcp']=False
        #config['provider']=tds[5].getText()
        #config['ssurl']=tds[6].find("a",class_='dl1')['href'].split('url=')[-1]
        configs.append(config)
    print('此次更新了'+str(len(configs))+'条数据')
    print('更新完成！')
    return configs

def loadConfig(filename):
    try:
        with open(filename,'r',encoding='utf-8') as f_obj:
            guiconfig = json.load(f_obj)
    except FileNotFoundError:
        msg = "文件 " + filename + " 并不存在，请确认程序运行在ShadowsocksR目录中！"
        print(msg)
    return guiconfig
    
def saveConfig(filename,data):
    print('正在写入文件……')
    try:
        with open(filename,'w',encoding='utf-8') as f_obj:
            f_obj.write(json.dumps(data,ensure_ascii=False,indent=2))
    except FileNotFoundError:
        msg = "文件 " + filename + " 并不存在，请确认程序运行在ShadowsocksR目录中！"
        print(msg)
    print('写入文件完成！')
    return 0 

url='https://doub.io/sszhfx/'
filename='gui-config.json'
htmldata=getHtmltext(url)
guiconfig=loadConfig(filename)
configs=getConfig(htmldata)
#print(json.dumps(getConfig(htmldata),ensure_ascii=False,indent=2))
#print(guiconfig['configs'])
guiconfig['configs']=configs
saveConfig(filename,guiconfig)
#print(loadConfig(filename)['configs'])
#print(getRandomMd5())
quit = input("请按 回车／Enter 退出……");
