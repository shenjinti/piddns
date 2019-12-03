import os
import sys
import requests
import re
import json

from six import print_
from aliyunsdkcore import client
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest

IPSVR = 'https://ip.cn'
RE_IP = re.compile('(\d+.\d+.\d+.\d+)')

KEY = os.getenv('ALIYUN_AK_KEY', 'None')
SECRET = os.getenv('ALIYUN_AK_SECRET', 'None')
REGION = os.getenv('ALIYUN_REGION', 'cn-hangzhou')


def get_outbound_ip():
    headers = {'User-Agent': 'curl/7.43.0'}
    req = requests.get(IPSVR, headers=headers)
    res = RE_IP.search(req.text)
    if res is None:
        raise Exception('Fail lookup outbound ip')
    return res.groups()[0]
    

def update_domain(domain, new_ip, rrs):
    cli = client.AcsClient(KEY, SECRET, REGION)

    req = DescribeDomainRecordsRequest()
    req.set_DomainName(domain)
    req.set_accept_format('json')
    resp = cli.do_action(req)


    records = json.loads(resp)['DomainRecords']['Record']

    for rec in records:
        if rec['Type'] != 'A':
            continue

        if rec['RR'] not in rrs:
            continue
        
        if rec['Value'] == new_ip:
            print_('Not need refresh, same as now.', new_ip, rec['RR'])
            continue

        req = UpdateDomainRecordRequest()
        req.set_RecordId(rec['RecordId'])
        req.set_Value(new_ip)
        req.set_RR(rec['RR'])
        req.set_Type(rec['Type'])

        req.set_accept_format('json')
        
        resp = cli.do_action(req)
        result = json.loads(resp)
        if 'Code' in result:
            raise Exception(result['Message'])
    
if __name__ == '__main__':
    if len(sys.argv) <= 0:
        print_usage()
        sys.exit(0)

    domain = sys.argv[1]

    sub_name = 'www'
    if domain.count('.') >= 2:
        sub_name = domain.split('.', 1)[0]
        domain = '.'.join('svnserve.com'.rsplit('.', 2)[:])
    
    ip = get_outbound_ip()
    print_('trying update ...', domain, ip)
    update_domain(domain, ip, [sub_name])
