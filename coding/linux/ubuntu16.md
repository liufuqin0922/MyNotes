# ubuntu1604

## change source

sudo sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

## docker

### 一键脚本

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common &&
curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/gpg | sudo apt-key add - &&

sudo add-apt-repository \
   "deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu \
   $(lsb_release -cs) \
   stable" &&
sudo apt-get update &&
sudo apt-get install docker-ce &&
sudo echo -e "{\n 
  \"registry-mirrors\": [\"https://docker.mirrors.ustc.edu.cn/\"]
}" >/etc/docker/daemon.json 
sudo systemctl restart docker

### 监听tcp

```bash
# 查看配置文件位于哪里
systemctl show --property=FragmentPath docker 
#编辑配置文件内容，接收所有ip请求
sudo vim /lib/systemd/system/docker.service  
ExecStart=/usr/bin/dockerd -H unix:///var/run/docker.sock -H tcp://0.0.0.0:2376
#重新加载配置文件，重启docker daemon
sudo systemctl daemon-reload
sudo systemctl restart docker
```

## pmm

```bash
# 拉取服务器镜像

docker pull percona/pmm-server:latest

# 创建PMM数据容器

docker create \
   -v /opt/prometheus/data \
   -v /opt/consul-data \
   -v /var/lib/mysql \
   -v /var/lib/grafana \
   --name pmm-data \
   percona/pmm-server:latest /bin/true

# 创建PMM服务器容器, 同时设置登录用户名(SERVER_USER)和密码(SERVER_PASSWORD), 根据需要进行修改. 默认使用80端口, 如果需要可以更改.

docker run -d -p 9001:80 \
  --volumes-from pmm-data \
  --name pmm-server \
  -e SERVER_USER=test \
  -e SERVER_PASSWORD=test \
  --restart always \
  percona/pmm-server:latest
```