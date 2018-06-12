#coding:utf-8
#由于scapy没有自动将库目录添加到python系统目录内，所以这里先查看模块目录在哪里，再添加到系统搜索路径下
from scapy.all import *   #导入scapy较慢，如果无法导入，就将py文件放到scapy库，C:\Python27\Scripts\scapy-master文件夹下执行
import struct
print("sucess import")


# 发送数据包
data=struct.pack('ssssss','w','a','n','g','p','e')   #第一个参数的字符串的长度，是后面参数的个数
pkt=IP(src='11.39.94.17',dst='11.39.94.55')/TCP(sport=12345,dport=5555)/data
send(pkt,inter=1,count=5)