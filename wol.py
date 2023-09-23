# -*- coding: utf-8 -*-
from wakeonlan import send_magic_packet

def main():
    # Mac地址列表
    data = ['8C:35:92:83:8D:26', '8C:35:92:83:8D:27', 'E0:27:6C:EC:C9:77', 'E0:27:6C:EC:C9:78', 'E0:27:6C:EC:C8:72', 'E0:27:6C:EC:C8:71', '8C:35:92:83:8C:4E', '8C:35:92:83:8C:4F', '8C:35:92:83:8D:8E', '8C:35:92:83:8D:8F', 'E0:27:6C:EC:D9:BC', 'E0:27:6C:EC:D9:BE', 'E0:27:6C:EC:C9:6F', 'E0:27:6C:EC:C9:70', '8C:35:92:83:8C:48', '8C:35:92:83:8C:49', '8C:35:92:83:99:77', '8C:35:92:83:99:78', '8C:35:92:83:8D:1C', '8C:35:92:83:8D:1D', 'E0:27:6C:EC:C8:9A', 'E0:27:6C:EC:C8:99', 'E0:27:6C:EC:C7:2F', 'E0:27:6C:EC:C7:30', 'E0:27:6C:F3:F4:89', 'E0:27:6C:F3:F4:88', '8C:35:92:83:8C:58', '8C:35:92:83:8C:59', '8C:35:92:83:8D:14', '8C:35:92:83:8D:15', '8C:35:92:83:8B:46', '8C:35:92:83:8B:47', 'E0:27:6C:EC:C8:12', 'E0:27:6C:EC:C8:11', '8C:35:92:83:8D:94', '8C:35:92:83:8D:95', '8C:35:92:83:8C:56', '8C:35:92:83:8C:57', 'E0:27:6C:EC:CA:2C', 'E0:27:6C:EC:CA:2B', '8C:35:92:83:8B:B0', '8C:35:92:83:8B:B1']
    for mac in data:
        send_magic_packet(mac)
        print(f'发送魔术唤醒包: {mac}')

if __name__ == '__main__':
    main()