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


# Contenido que vamos a enviar
LINE = METODO + ' ' + 'sip:' + LOGIN + ' ' + 'SIP/2.0'
print(LINE)

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IP, PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
