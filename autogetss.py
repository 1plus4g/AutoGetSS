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
    #print(url)
    return requests.get(url).text
    
'''   
def getConfig(htmldata):
    soup = BeautifulSoup(htmldata,'html.parser')
    tabledata = soup.find('table',width="100%")
    trs = tabledata.findAll('tr')[1:] #去掉首行
    for tr in trs:
        config={}
        tds=tr.findAll('td')
        config['remarks']=tds[0].getText()
        config['server']=tds[1].getText()
        config['server_port']=tds[2].getText()
        config['password']=tds[3].getText()
        config['method']=tds[4].getText()
        config['provider']=tds[5].getText()
        config['ssurl']=tds[6].find("a",class_='dl1')['href'].split('url=')[-1]
        configs.append(config)
    return configs
'''

def getRandomMd5():
    hash = hashlib.md5()
    hash.update(str(random.random()).encode('utf-8'))
    return hash.hexdigest().upper()
    
def getBase64(src):
    return base64.b64encode(src.encode(encoding="utf-8")).decode()
    
def getConfig(htmldata):
    soup = BeautifulSoup(htmldata,'html.parser')
    tabledata = soup.find('table',width="100%")
    trs = tabledata.findAll('tr')[1:] #去掉首行
    for tr in trs:
        config={}
        tds=tr.findAll('td')
        if 'del' in str(tds[1]):
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
    return configs

def loadConfig(filename):
    with open(filename,'r',encoding='utf-8') as f_obj:
        guiconfig = json.load(f_obj)
    return guiconfig
    
def saveConfig(filename,data):
    with open(filename,'w',encoding='utf-8') as f_obj:
        f_obj.write(json.dumps(data,ensure_ascii=False,indent=2))
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
