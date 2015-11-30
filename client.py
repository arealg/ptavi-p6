#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

if len(sys.argv) != 3:
    sys.exit('Usage: python3 client.py method receiver@IP:SIPport')

server_port = sys.argv[2].split('@')

METODO = sys.argv[1]
LOGIN = sys.argv[2].split(':')[0]
IP = server_port[1].split(':')[0]
PORT = int(server_port[1].split(':')[1])
LINE = METODO + ' ' + 'sip:' + LOGIN + ' ' + 'SIP/2.0'

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IP, PORT))

my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print(data.decode('utf-8'))
ack_msg = data.decode('utf-8')

if ('100 Trying' in ack_msg and '180 Ring' in ack_msg
    and '200 OK' in ack_msg):
    my_socket.send(bytes('ACK' + ' ' + 'sip:' + LOGIN + ' '
                   + 'SIP/2.0', 'utf-8')
                   + b'\r\n')

print('Finalizado')
my_socket.close()
