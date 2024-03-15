import pyshark

# 打开并解析捕获的网络数据包文件
pcap = pyshark.FileCapture(r'D:\CTF_Study\Reverse\BUU\5.第五页\[FlareOn6]DnsChess\capture.pcap')

# 创建一个空列表用于存储提取的 IP 地址和 DNS 查询名称的元组
lst = []

# 遍历每个数据包
for package in pcap:
    # 检查 DNS 响应中是否只有一个回答
    if package.dns.count_answers == '1':
        # 提取 DNS 响应的 IP 地址
        ip_addr = package.dns.a
        # 将 IP 地址和 DNS 查询名称作为元组添加到列表中
        lst.append((ip_addr, package.dns.qry_name))

# 打印存储了 IP 地址和 DNS 查询名称的列表
sortedList = sorted(lst, key=lambda tup: int(tup[0].split('.')[2]) % 16)
# print(len(sortedList))
for i in sortedList:
    print(i)

ida_chars = [
  0x79, 0x5A, 0xB8, 0xBC, 0xEC, 0xD3, 0xDF, 0xDD, 0x99, 0xA5,
  0xB6, 0xAC, 0x15, 0x36, 0x85, 0x8D, 0x09, 0x08, 0x77, 0x52,
  0x4D, 0x71, 0x54, 0x7D, 0xA7, 0xA7, 0x08, 0x16, 0xFD, 0xD7
]
flag = [i for i in range(len(ida_chars))]
i = 0
for ip_addr, hostname in lst:
    ip_addr_list = [int(i) for i in ip_addr.split('.')]
    if ip_addr_list[0] == 0x7f and not (ip_addr_list[3] & 0x1):
        i = ip_addr_list[2] & 0xF
        flag[2 * i] = chr(ida_chars[2 * i] ^ ip_addr_list[1])
        flag[2 * i + 1] = chr(ida_chars[2 * i + 1] ^ ip_addr_list[1])
    else:
        i = 0
print(''.join(flag))
pcap.close()
#flag{LooksLikeYouLockedUpTheLookupZ@flare-on.com}