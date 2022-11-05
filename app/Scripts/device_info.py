#!C:\Users\NASIR KASIM\wassceverse\Scripts\python.exe
#-*- coding: utf-8 -*-
'''
Created on 2013-09-23
@author: happyguannan@gmail.com
@summary: device info
@version: 0.1
'''

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from optparse import OptionParser
import requests

parser = OptionParser("device_info.py [-n --name <typename>][-t --title]")
parser.add_option("-n", "--name", dest="typename",
                  help="args: 'device' or 'host'", metavar="TYPE")
parser.add_option("-t", "--title",
                  action="store_true", default=False)
options, args = parser.parse_args()


def parse():
    """ 
    @summary:接收参数，负责功能调用。
    """
    if options.title:
        print "Mpis_ID 节点名称 节点编号 出口交换机管理IP 核心交换机管理IP 管理服务器IP PDN内网IP TTA服务-ETH0 TTA服务-ETH1 FC服务-ETH0 FC服务-ETH1 测试设备-ETH0 测试>"
        print url_get("device")
    elif options.typename == 'device':
        print url_get('device')
    elif options.typename == 'host':
        print url_get('host')
    else:
        print parser.print_help()
def url_get( order ):
    """
    -- 小写 no"-"
    eg: device_info.py--url http://192.168.137.76:8000/
    """
    url = "http://223.203.188.114:9011/api/" + order + "/"
#    url = "http://127.0.0.1:8080/api/" + order + "/"
    hyper_text = requests.get(url)
    if hyper_text.status_code != 200:
        exit(1)
    return hyper_text.text


if __name__ == "__main__":
    parse()

