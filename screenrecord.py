# -*- coding: utf-8 -*-
# 使用ffmpeg录制视频，为了进行伪装，故使用chrome浏览器图标
import os
import sys
from datetime import datetime

# ffmpeg 程序
ffmepg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg.exe')
# 保存路径
workspace_path = r"E:\tmp"
# 当前日期
current_time = datetime.now()
day_time = current_time.strftime("%Y-%m-%d")
all_time = current_time.strftime("%Y-%m-%d_%H%M%S")
# 保存文件夹
save_path = workspace_path + "\\" + day_time
# 保存文件名
save_name = all_time + ".mkv"
# 文件保存完整路径
save_file = save_path + "\\" + save_name

def check_workspace():
    # 总工作目录
    if os.path.exists(workspace_path):
        print(f"工作目录： {workspace_path}")
    else:
        try:
            # 创建工作目录
            os.makedirs(workspace_path, exist_ok=True)
            print(f"创建工作目录 {workspace_path} 成功")
        except OSError as e:
            print(f"创建工作目录 {workspace_path} 失败： {e}")
            sys.exit(1)
    # 保存目录
    if os.path.exists(save_path):
        print(f"保存目录： {save_path}")
    else:
       try:
            # 创建保存目录
            os.makedirs(save_path, exist_ok=True)
            print(f"创建保存目录 {save_path} 成功")
       except OSError as e:
           print(f"创建保存目录 {save_path} 失败： {e}")
           sys.exit(1)

def main():
    check_workspace()
    # 打印信息
    print(r"########################################")
    print(f"""工作目录： {workspace_path}
保存目录： {save_path}
文件名： {save_name}
文件地址： {save_file}
ffmepg： {ffmepg_path}""")
    print(r"########################################")
    print("\n")
    # 获取设备列表: ffmpeg -list_devices true -f dshow -i dummy
    # 录屏时间 （秒）
    record_time = 600
    # 开始录制
    # 只录制屏幕，不录制声音
    # os.system(f"{ffmepg_path} -y -f gdigrab -framerate 60 -video_size 1920x1080 -i desktop -t {record_time} -c:v libx265 -preset ultrafast -b:v 10M \"{save_file}\"")
    os.system(f"{ffmepg_path} -y -f gdigrab -framerate 60 -video_size 1920x1080 -i desktop -f dshow -i audio=\"麦克风阵列 (Built-in Audio)\" -t {record_time} -c:v libx265 -preset ultrafast -b:v 10M -c:a aac -strict experimental \"{save_file}\"")
    
if __name__ == '__main__':
    main()