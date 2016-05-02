Aliyun DDNS Tools for raspberry pi
---------
* Required:    
python >= 2.7    
requests >= 2.4.3    
six >= 1.8.0    
[aliyundnssdk](https://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/cn/dns/0.2.17/assets/download/sdk/aliyun-python-sdk-alidns.zip)

* Howto run?     
```
git clone https://github.com/shenjinti/piddns.git   
cd piddns   
ALIYUN_AK_KEY='YOUR_KEY' ALIYUN_AK_SECRET='YOUR_SECRET' python refresh.py example.com    
```    
And update command  into `/etc/crontab` 
```
* *	* * *	pi ALIYUN_AK_KEY='YOUR_KEY' ALIYUN_AK_SECRET='YOUR_SECRET' python /home/pi/piddns/refresh.py YOUR_DOMAIN
````

