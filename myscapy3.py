#coding:utf-8
#由于scapy没有自动将库目录添加到python系统目录内，所以这里先查看模块目录在哪里，再添加到系统搜索路径下
from scapy.all import *   #导入scapy较慢，如果无法导入，就将py文件放到scapy库，C:\Python27\Scripts\scapy-master文件夹下执行
print("sucess import")
def pack_callback(packet):
#     print packet.show()  #可以查看包的结构属性等
    if packet["TCP"].payload:  #检测tcp负载是否有数据，有Ethernet、IP、TCP几个阶段
        appstr=str(packet["TCP"].payload)  #将tcp负载字节数组转化为字符串
        #匹配自定义正则表达式
        pat = 'Content-Type:(.*)[;\r\n]'   #创建一个正则表达式，在字符串中匹配这个正则表达式，这里以Content-Type:开头，以;或\r结尾的
        pat = re.compile(pat);   #使用正则表达式，创建正则对象
        m = re.search(pat,appstr)  #查询是否存在匹配的子字符串
        if m:
            print(m.groups())  #打印需要()输出的内容
        #检测邮件
#         if "user" in appstr.lower() or "pass" in appstr.lower():
#             print "server:%s"%packet[IP].dst
#             print "%s"%packet[TCP].payload
# 嗅探数据包，参数：过滤器，回调函数，网卡，个数
ifacestr="HUAWEI Mobile Connect - Network Card"  #网口名称，这里要换成自己的网卡名称
filterstr="tcp port 110 or tcp port 8080 or tcp port 80"  #过滤条件，为空表示不限制
sniff(filter=filterstr,prn=pack_callback,iface=ifacestr,count=0)  #count等0表示一直监听，要想监听数据包，需要首先安装winpcap




# 发送数据包
# data=struct.pack('sssss','w','a','n','g','p','e')
# pkt=IP(src='11.39.94.17',dst='11.39.94.55')/TCP(sport=12345,dport=5555)/data
# send(pkt,inter=1,count=5)