# 数据库链接
 db_connect msf:hack-money@127.0.0.1/msf2
# 资料

https://zhuanlan.zhihu.com/p/25857679
http://www.kali.org.cn/thread-20133-1-1.html
http://blog.csdn.net/lijia111111/article/details/64124693
https://github.com/Veil-Framework/Veil-Evasion
http://www.360zhijia.com/360anquanke/188372.html
http://blog.sina.com.cn/s/blog_4c86552f0102wjr9.html
http://blog.csdn.net/lzhd24/article/details/50664342
http://www.freebuf.com/sectool/72135.html
http://blog.csdn.net/ski_12/article/details/57400687
1.msf>show exploit

显示metasploit框架中所有可用的渗透攻击模块。

 

2.msf>show auxiliary

显示所有的辅助模块以及他们的用途，在metasploit中，辅助模块的用途非常广泛，他们可以是扫描器/拒绝服务攻击工具/fuzz测试器，以及其他类型的工具。

 

3.msf>show options

参数options是保证metasploit框架中各个模块正常运行所需的各种设置，当你选择一个模块，并输入msf>show options后，会列出这个模块所需的各种参数。如果没有选择任何模块，输入这个命令会显示所有的全局参数。

 

4.msf>show payloads

攻击载荷是针对特定平台的一段攻击代码，它通过网络传送到攻击目标进行执行。和show options命令一样，当你在当前模块的命令提示符下输入show payloads，metasploit会将当前模块兼容的攻击载荷显示出来。

msf>show payload  (显示合适的payload反弹shell。reverse_tcp（反弹时tcp）

在msf>下则会显示所有的payload，use进入摸个模块之后show paylad，显示这个模块适合的payload）

 

5.msf>show targets

（列出渗透攻击模块收到漏洞影响的目标系统的类型，例如MS08-067漏洞的攻击只适用于特定的补丁级别/语言版本以及安全机制的实现，攻击是否成功取决于目标windows系统的版本，show targets中的Auto Targeting（自动选择目标）是攻击目标列表中的一个选项。通常，攻击模块会通过目标操作系统的指纹信息，自动选择操作系统版本进行攻击。不过最好还是通过人工更加准确地识别出目标操作系统的相关信息，这样才能避免触发错误的/破坏性的攻击）

 

6.info

若觉得show和search命令所提供的信息过于简短，可以使用info命令加上模块名字来显示此模块的详细信息/参数说明以及所有可用的目标操作系统（如果已选择了某个模块，直接在模块的提示符下输入info即可。

 

 

8.setg和unsetg

setg命令和unsetg命令能够全局参数进行设置或清楚。使用这组命令你不必每次遇到某个参数都要重新设置，特别是那些经常用到又很少会变的参数。

 

9.save

在使用setg命令对全局参数进行设置后，可以使用save命令将当前的设置值保存下来，这样在下次启动MSF终端时还可以使用这些设置值。

（保存在/root/.msf3/config）