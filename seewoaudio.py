# -*- coding: utf-8 -*-
import os
from datetime import datetime
import click

@click.command()
def get_devices():
    ''' 获取当前所连接的设备 '''
    os.system('ffmpeg -list_devices true -f dshow -i dummy')
    # 按任意键退出脚本
    input()
    exit

def check_workdir(workdir: str):
    if os.path.exists(workdir):
        print(f'保存目录：{workdir} 已存在')
    else:
        try:
            os.makedirs(workdir, exist_ok=True)
            print(f'保存目录：{workdir} 创建成功')
        except OSError as e:
            print(f'保存目录：{workdir} 创建失败！！！')
            exit()

@click.command()
@click.option('--device', '-d', help=r'进行录音的设备', type=str, default='麦克风 (USB Microphone)')
@click.option('--record_time', '-t', help=r'录制时长（单位：分钟）（默认值：40）', type=int, default=40)
@click.option('--out_dir', '-o', help=r'保存文件夹（默认值：D:\EasiRecorder）', type=str, default=r'D:\EasiRecorder')
@click.option('--codec_audio', '-c', help=r'音频编码格式（默认值：pcm_s16le）',type=str,default='pcm_s16le')
@click.option('--perfix_customize', '-p', help=r'自定义保存文件名前缀（默认值：Record） 文件名格式：perfix_%Y-%m-%d_%H%M%S.wav', type=str, default='Record')
@click.option('--file_format', '-f', help=r'文件格式（默认值：wav）', type=str, default='wav')
def run(device: str, record_time: str, out_dir: str, codec_audio:str, perfix_customize:str, file_format:str):
    ''' 运行录音 '''
    # 创建保存目录
    check_workdir(out_dir)
    # 时间
    current_time = datetime.now()
    times = current_time.strftime('%Y-%m-%d_%H%M%S')
    # 保存文件名
    save_name = perfix_customize + '_' + times + '.' + file_format
    # 保存路径（秒）
    record_time_second = record_time * 60
    save_path = os.path.join(out_dir, save_name)
    # 保存时间
    ffmpeg = os.path.join(os.path.dirname(__file__), 'ffmpeg.exe')
    # ffmpeg程序
    print(f"""########################################
    文件名：{save_name}
    保存文件夹：{out_dir}
    保存文件绝对路径：{save_path}
    录制设备：{device}
    录制时长：{record_time}分钟 
    编码格式：{codec_audio}
    文件格式：{file_format}
########################################""")
    command = f'{ffmpeg} -y -f dshow -i audio=\"{device}\" -t {record_time_second} -c:a {codec_audio} -ar 44100 -ac 2 {save_path}'
    print(command)
    os.system(command)

@click.group()
def cli():
    pass

cli.add_command(run)
cli.add_command(get_devices, name='getdevices')

if __name__ == '__main__':
    cli()