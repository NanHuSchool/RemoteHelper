@echo off
rmdir /s /q build
rmdir /s /q out
del /s /q *.spec

mkdir out
gcc quickset.c -o out\quickset.exe
pyinstaller -i icon_rdp.ico --distpath out --onefile rdp.py
pyinstaller --onefile --distpath out wol.py