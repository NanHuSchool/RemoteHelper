# -*- coding: utf-8 -*-
import os
import csv

def main(cvs_name):
    # csv数据文件位置
    csv_path = os.path.join(os.path.dirname(__file__), cvs_name)
    # 检测文件
    if os.path.exists(csv_path):
        print(f"数据位置： {csv_path}")
    else:
        print(f"找不到文件： {cvs_name}")
        exit(1)

    # 创建rdp保存文件夹
    savedir_name = "rdp"
    savedir_path = os.path.join(os.path.dirname(__file__), savedir_name)
    if os.path.exists(savedir_path):
        print(f"保存文件夹: {savedir_name}")
    else:
        try:
            os.makedirs(savedir_path, exist_ok=True)
            print(f"创建保存文件夹成功：{savedir_path}")
        except OSError as e:
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
            # rdp文件变量
            rdp_name = device_name + ".rdp"
            rdp_path = os.path.join(savedir_path, rdp_name)
            # 写入rdp
            context = f"""screen mode id:i:2
use multimon:i:0
desktopwidth:i:1920
desktopheight:i:1080
session bpp:i:32
winposstr:s:0,3,0,0,800,600
compression:i:1
keyboardhook:i:2
audiocapturemode:i:0
videoplaybackmode:i:1
connection type:i:7
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
redirectlocation:i:1
redirectcomports:i:1
redirectsmartcards:i:1
redirectwebauthn:i:1
redirectclipboard:i:1
redirectposdevices:i:0
drivestoredirect:s:*
autoreconnection enabled:i:1
authentication level:i:0
prompt for credentials:i:0
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
username:s:seewo
"""
            try:
                with open(rdp_path, mode="w", newline="", encoding="utf-8") as rdp_f:
                    rdp_f.write(context)
                    print(f"rdp: {rdp_path}")
            except Exception as e:
                    print(f"{rdp_name} 保存失败")


if __name__ == "__main__":
    main("mac.csv")