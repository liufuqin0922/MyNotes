个人笔记而已，没啥好看的，可以给我提交哦  
Todo:
* 各种后门隐藏与发现 
* webshell
* getshell后如何getflag
* msf 一件传shell 执行
* 各大cms shell
* 提权
* owasp
* 删账户
* 改cd ls..
* 删解释器
* netstat：端口，连接排查
* kill进程
* sql防注入代码
* 上传漏洞防护
* 日志管理
* 文件监控
* umask?
* 网络端口监控
* waf过滤sqlmap  //sql改head
* 后门批量上传，管理
* 目录禁止写入
* 后门开机启动 定时运行
* 自动化程度提高
* 编译所有的py
* php 5.10 poc

# 如何重启php

启动php-fpm:

/usr/local/php/sbin/php-fpm
INT, TERM 立刻终止
QUIT 平滑终止
USR1 重新打开日志文件
USR2 平滑重载所有worker进程并重新载入配置和二进制模块
先查看php-fpm的master进程号
kill -USR2 \<master pid\>
* 审计源代码，分析后门、命令执行、上传、SQL等威胁 * 现成CMS注意DIFF
* 弱口令更改
* 根据漏洞PATCH
* 根据漏洞写出EXP，发动攻击 * 被攻击后完成EXP，PATCH
* 自动化种马，权限维持
* 自动化收割

# 查看已建立的网络连接及进程

netstat ‐antulp | grep EST

# 查看页面访问排名前十的IP

netstat ‐ant|awk |grep |sed ‐e ‐e |sort|uniq ‐c|sort ‐rn 

http://bobao.360.cn/ctf/learning/210.html  
https://bbs.ichunqiu.com/thread-25092-1-1.html?from=aqzx2

## mac terminal
http://www.jianshu.com/p/c36dfdfa6569

#gist
85eed685f7243831c2d93af98d2bbdbe
kk
base64转图片
<img src="data:image/jpg;base64,ZmxhZ3t4Y3Rmezg4MzEyN2QyNzI2MjZjOWFmN2Q3M2Q5M2JlMDBkZTQ3fX0=">
# 666
66667176e9b719899326552b7144c5eb438a743bc01666


数据库备份表，dump，shell测试，！权限维持方法！