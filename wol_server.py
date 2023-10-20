# -*- coding: utf-8 -*-
from wol_mac import wake_mac

def main(csv_file):
    wake_mac(csv_file)

if __name__ == '__main__':
    main("mac_server.csv")