# -*- coding: utf-8 -*-
#
# GNU General Public License v3.0
# Copyright (C) 2024 OpenNanHu
# 将当前目录下csv文件中的信息生成rdp文件
import os
import csv

def generate(cvs_name):
    # csv数据文件位置
    csv_path = os.path.join(os.path.dirname(__file__), cvs_name)
    # 检测文件
    if os.path.exists(csv_path):
        print(f"数据位置：{csv_path}")
    else:
        print(f"找不到文件：{cvs_name}")
        exit()

    # 创建rdp保存文件夹
    out_dir = "rdp"
    out_path = os.path.join(os.path.dirname(__file__), out_dir)
    try:
        if not os.path.exists(out_path):
            os.makedirs(out_path, exist_ok=True)
            print(f"创建保存文件夹成功：{out_path}")
    except OSError as e:
            print(f"创建保存文件夹失败：{e}")
            exit()

    # 打开CVS文件并读取
    with open(csv_path, mode="+r", encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        # 跳过标题行
        next(csv_reader)
        # 每行读取，并获取相关信息
        for r in csv_reader:
            # 设备名称,IP,MAC1,MAC2,Account,WOL_Status
            device_name = r[0]
            ip_address = r[1]
            username=r[4]
            # rdp文件变量
            rdp_name = device_name + ".rdp"
            rdp_path = os.path.join(out_path, rdp_name)
            # 写入rdp
            context = f"""screen mode id:i:2
use multimon:i:0
desktopwidth:i:1920
desktopheight:i:1080
session bpp:i:32
winposstr:s:0,1,72,269,932,1020
compression:i:1
keyboardhook:i:0
audiocapturemode:i:0
videoplaybackmode:i:1
connection type:i:6
networkautodetect:i:1
bandwidthautodetect:i:1
displayconnectionbar:i:1
enableworkspacereconnect:i:0
disable wallpaper:i:0
allow font smoothing:i:0
allow desktop composition:i:0
disable full window drag:i:1
disable menu anims:i:1
disable themes:i:0
disable cursor setting:i:0
bitmapcachepersistenable:i:1
full address:s:{ip_address}
audiomode:i:0
redirectprinters:i:1
redirectcomports:i:0
redirectsmartcards:i:1
redirectwebauthn:i:1
redirectclipboard:i:1
redirectposdevices:i:0
autoreconnection enabled:i:1
authentication level:i:0
prompt for credentials:i:1
negotiate security layer:i:1
remoteapplicationmode:i:0
alternate shell:s:
shell working directory:s:
gatewayhostname:s:
gatewayusagemethod:i:4
gatewaycredentialssource:i:4
gatewayprofileusagemethod:i:0
promptcredentialonce:i:0
gatewaybrokeringtype:i:0
use redirection server name:i:0
rdgiskdcproxy:i:0
kdcproxyname:s:
enablerdsaadauth:i:0
drivestoredirect:s:*
username:s:{username}
"""
            try:
                with open(rdp_path, mode="w", newline="", encoding="utf-8") as f:
                    f.write(context)
                    f.close
                    print(f"rdp: {rdp_path}")
            except Exception as e:
                    print(f"{rdp_name} 保存失败：{e}")


if __name__ == "__main__":
    generate("mac.csv")
    generate("mac_server.csv")