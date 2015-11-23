#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys



class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        IP = self.client_address[0]
        PUERTO = self.client_address[1]
        print("{} {}".format(IP, PUERTO))
        while 1:
            line = self.rfile.read()
            if not line:
                break
            linea = line.decode('utf-8')
            lista = linea.split()
            print(lista)
            if 'INVITE' in lista:
                self.wfile.write(b'\r\n\r\n' + b'SIP/2.0 100 Trying: al recibir un INVITE'
                + b'\r\n\r\n'+ b'SIP/2.0 180 Ring: al recibir un INVITE'
                + b'\r\n\r\n' + b'SIP/2.0 200 OK: en caso de exito'
                + b'\r\n\r\n')



if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', int(sys.argv[2])), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
