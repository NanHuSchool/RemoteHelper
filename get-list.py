# -*- coding: utf-8 -*-

def main():
    mac = []
    with open('data.txt', 'r') as data:
        for line in data:
            mac.append(line.strip())
    print(mac)

if __name__ == '__main__':
    main()