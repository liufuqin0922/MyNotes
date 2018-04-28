# ubuntu1604

## change source

sudo sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

## docker

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
}" >/etc/docker/daemon.json &&
sudo systemctl restart docker