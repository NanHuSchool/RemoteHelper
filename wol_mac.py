# -*- coding: utf-8 -*-
import os
import csv
from wakeonlan import send_magic_packet

def main(csv_name):
    # csv数据文件位置
    csv_path = os.path.join(os.path.dirname(__file__), csv_name)
    # 检测文件
    if os.path.exists(csv_path):
        print(f"数据位置： {csv_path}")
    else:
        print(f"找不到文件： {csv_name}")
        exit(1)
    # 打开CVS文件并读取
    with open(csv_path, mode="r", encoding="utf-8") as f:
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

if __name__ == "__main__":
    main("mac.csv")