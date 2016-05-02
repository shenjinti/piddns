Aliyun DDNS Tools for raspberry pi
---------
* Required:    
python >= 2.7
requests >= 2.4.3
six >= 1.8.0
(aliyundns sdk)[https://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/cn/dns/0.2.17/assets/download/sdk/aliyun-python-sdk-alidns.zip?spm=5176.docdns/sdk/sdk.2.2.LzuuTd&Expires=1462334790&OSSAccessKeyId=80kJOHQaA4syuazx&Signature=qFEQSDrJo0sxcon4HucVbm4RD1A%3D]

* Howto run?
```
ALIYUN_AK_KEY='YOUR_KEY' ALIYUN_AK_SECRET='YOUR_SECRET' python refresh.py example.com
```
And update this into /etc/crontab

