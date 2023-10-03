REM Tsinghua Mirror
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

REM 更新pip
pip install -U pip

REM 安装依赖包
pip install -R requirements.txt