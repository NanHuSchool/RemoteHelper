#include <stdio.h>
#include <stdlib.h>

int main(){
    // 显示控制面板
    system("reg add HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\HideDesktopIcons\\NewStartPanel /v {5399E694-6CE5-4D6C-8FCE-1D8870FDCBA0} /t REG_DWORD /d 0 /f");
    // 关闭防火墙
    system("netsh advfirewall set allprofiles state off");
    // 防火墙放行远程桌面3389默认端口
    system("netsh advfirewall firewall add rule name=\"Open Port 3389\" dir=in action=allow protocol=TCP localport=3389");
    // Windows Defender 开启
    system("reg add \"HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\" /v DisableAntiSpyware /t REG_DWORD /d 2 /f");
    system("reg add \"HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection\" /v DisableRealtimeMonitoring /t REG_DWORD /d 2 /f");
    // 开启远程桌面
    system("reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\" /v fDenyTSConnections /t REG_DWORD /d 0 /f");
    // 本地安全策略
    system("reg add HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Lsa /v LimitBlankPasswordUse /t REG_DWORD /d 0 /f");
    system("reg add HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\ControlSet001\\Lsa /v LimitBlankPasswordUse /t REG_DWORD /d 0 /f");
    // 同步时间
    system("net start w32time");
    system("w32tm /resync");
    // 任务栏时钟精确到
    system("reg add HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced /v ShowSecondsInSystemClock /t REG_DWORD /d 1 /f");
    // 显示所有文件扩展名
    system("reg add HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced /v HideFileExt /t REG_DWORD /d 0 /f");
    // 关闭打开程序的“安全警告”
    system("reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Associations /v ModRiskFileTypes /t REG_SZ /d \".bat;.exe;.reg;.vbs;.chm;.msi;.js;.cmd\" /f");
    // 重启资源管理器
    system("taskkill /f /im explorer.exe");
    system("start explorer.exe");
    // 刷新DNS服务
    system("ipconfig /flushdns");
    // 开启防火墙
    system("reg add HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile /v EnableFirewall /t REG_DWORD /d 1 /f");
    system("reg add HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\PublicProfile /v EnableFirewall /t REG_DWORD /d 1 /f");
    system("reg add HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\DomainProfile /v EnableFirewall /t REG_DWORD /d 1 /f");
    system("netsh advfirewall set allprofiles state on");
    // 重启系统
    // system("shutdown /r /t 0");
}