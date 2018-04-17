# 如何查看Linux系统的带宽流量

- 按网卡查看流量：ifstat、dstat -nf或sar -n DEV 1 2
- 按进程查看流量：nethogs
- 按连接查看流量：iptraf、iftop或tcptrack
- 查看流量最大的进程：sysdig -c topprocs_net
- 查看流量最大的端口：sysdig -c topports_server
- 查看连接最多的服务器端口：sysdig -c fdbytes_by fd.sport