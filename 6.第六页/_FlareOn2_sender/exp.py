import base64
import pyshark

def Strtoascii(string):
    ascii_encoded = ""
    for i in range(0, len(string), 2):
        hex_str = string[i:i+2]
        integer = int(hex_str, 16)
        ascii_encoded += chr(integer)
    return ascii_encoded

def extract_post_data(pcap_file):
    cap = pyshark.FileCapture(pcap_file, display_filter='http.request.method == "POST"')
    post_data = ""
    
    for pkt in cap:
        try:
            payload = pkt.http.Data
            post_data += Strtoascii(payload)
        except AttributeError:
            pass

    cap.close()
    return post_data

# 提取并拼接POST请求数据
pcap_file = r"D:\CTF_Study\Reverse\BUU\6.第六页\_FlareOn2_sender\challenge.pcap"

post_data = extract_post_data(pcap_file)
print("提取出的数据：",post_data)


str1 = "UDYs1D7bNmdE1o3g5ms1V6RrYCVvODJF1DpxKTxAJ9xuZW=="

string1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/="
string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

a=str1.translate(str.maketrans(string1,string2))#利用密码表还原成正常base64编码后的字符串

byte_980EA8 = [0x66, 0x6C, 0x61, 0x72, 0x65, 0x62, 0x65, 0x61, 0x72, 0x73, 0x74, 0x61, 0x72, 0x65]
flag = ''
byte_string = base64.b64decode(a)
string_array = []

for byte in byte_string:
    int_value = int(byte)
    string_array.append(int_value)

for i in range(len(string_array)):
    flag += chr((string_array[i]-byte_980EA8[i%0xe])&0xff)
print('flag{' + flag + '}')
