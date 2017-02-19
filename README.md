# AutoGetSS
### 介绍 Introduction

免费的ss分享站会频繁修改密码，而人工更新太繁琐，于是有了这个项目。~~根本原因是没钱~~。

### 需求 TODO

- [x] 支持[doub.io](https://doub.io/sszhfx/)
- [x] 调试日志
- [ ] 支持多站点
      - [ ] [ss免费账号-github](https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7)
      - [ ] [ishadowsocks](https://www.ishadowsocks.xyz/)
- [ ] 不和原有配置发生冲突
- [ ] 多系统支持
      - [ ] Linux
      - [x] windows
      - [ ] osx
- [ ] 自动运行

### 安装 Install

#### Windows

1. 你需要安装python3.x，[下载地址](https://www.python.org/downloads/release/python-360/)

2. 需要安装BeautifulSoup和requests模块，在管理员终端运行如下命令

   ```cmd
   pip3 install requests
   pip3 install beautifulsoup4
   ```

3. 将autogetss.py放在ShadowsocksR文件夹内，此代码适用于版本4.1.1-win

4. 定时运行autogetss.py

