Aliyun DDNS Tools for raspberry pi
---------
* Install:
```
pip install -r require.txt   
```
* Howto run?     
```
git clone https://github.com/shenjinti/piddns.git   
cd piddns   
ALIYUN_AK_KEY='YOUR_KEY' ALIYUN_AK_SECRET='YOUR_SECRET' python refresh.py pi4.example.com    
```    
And update command  into `/etc/crontab` 
```
* *	* * *	pi ALIYUN_AK_KEY='YOUR_KEY' ALIYUN_AK_SECRET='YOUR_SECRET' python /home/pi/piddns/refresh.py YOUR_DOMAIN
````

