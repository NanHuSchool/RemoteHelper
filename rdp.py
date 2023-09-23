# -*- coding: utf-8 -*-
import os
import socket
import subprocess
from datetime import datetime

def main():
    # 登录Windows系统账号的用户名
    username = os.getlogin()
    hostname = socket.gethostname()
    ip_adress = socket.gethostbyname(hostname)
    # 时间
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    # 保存文件名
    file_name = username + '_' + hostname + '_' + current_time
    print("文件名统一前缀： " + file_name)

    # IPConfig
    ipconfig_output = subprocess.check_output(['ipconfig', '/all']).decode('gb2312')
    with open(file_name + '.txt', mode='w', newline='', encoding='utf-8') as ip_file:
        ip_file.write(ipconfig_output)

    # RDP 
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
full address:s:{ip_adress}
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
username:s:{username}
"""
    with open(file_name + '.rdp', mode='w', newline='', encoding='utf-16le') as rdp_file:
        rdp_file.write(context)

if __name__ == '__main__':
    main()