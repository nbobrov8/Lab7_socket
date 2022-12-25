#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

# Создаем TCP/IP сокет.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаем сокет к порту, который прослушивает сервер.
server_address = ('localhost', 10000)
print('Подключение к {} порт {}'.format(*server_address))
conn = sock.connect(server_address)


while True:
    command = input(">> ")
    print('Получена команда {!r}'.format(command))
    command_line = bytes(command, "utf-8")
    sock.sendall(command_line)
    data = sock.recv(1024)
    if command == "exit":
        sys.exit()
    print("Received {!r}".format(data.decode("utf-8")))
