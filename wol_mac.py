# -*- coding: utf-8 -*-
import os
import sys
import csv
from wakeonlan import send_magic_packet

def wake_mac(csv_path):
    if getattr(sys, 'frozen', False):
        print('当前运行是用 pyinstaller 打包的环境')
        csv_abspath = os.path.join(os.path.dirname(__file__), csv_path)
        print(f"csv文件：{csv_abspath}")
    # 判断csv文件是否存在
    elif os.path.exists(csv_path):
        csv_abspath = os.path.abspath(csv_path)
        print(f"csv文件：{csv_abspath}")
    else:
        print(f"找不到csv文件： {csv_path}")
        sys.exit()

    # 读取文件
    with open(csv_abspath, mode="r", encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        # 跳过标题行
        next(csv_reader)
        # 每行读取，并获取相关信息
        for r in csv_reader:
            # 设备信息 IP Mac地址1 Mac地址2
            device_name = r[0]
            ip_address = r[1]
            mac_address_one = r[2]
            mac_address_two = r[3]
            print(f"""
############################################################
    设备名称：{device_name}
    IP地址：{ip_address}
    Mac地址1：{mac_address_one}
    Mac地址2：{mac_address_two}
############################################################""")
            send_magic_packet(mac_address_one)
            send_magic_packet(mac_address_two)

def main():
    wake_mac(".\mac.cv")

if __name__ == '__main__':
    main()