# 使用Let's Encrypt 进行泛解析。
## acme.sh的方式
获取acme脚本如下，注意报错，安装依赖
- `curl https://get.acme.sh | sh` 
无法执行acme.sh:
    source ~/.bashrc
## 获取证书
下面是cugapp.com的脚本。
```zsh
    export DP_Id="11111"  &&
    export DP_Key="xxxxxx"  &&
    acme.sh --issue --dns dns_dp -d *.cugapp.com -d cugapp.com &&

    sed -i '4,5c ssl_certificate /usr/local/nginx/conf/ssl/cugapp.com.cer;\
    ssl_certificate_key /usr/local/nginx/conf/ssl/cugapp.com.key;' ./*.cugapp* &&

    acme.sh  --installcert  -d  *.cugapp.com   \
            --key-file   /usr/local/nginx/conf/ssl/cugapp.com.key \
            --fullchain-file /usr/local/nginx/conf/ssl/cugapp.com.cer \
            --reloadcmd  "nginx -s reload" &&
```
