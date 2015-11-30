#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        while 1:
            line = self.rfile.read()
            if not line:
                break
            linea = line.decode('utf-8')
            print(linea)
            lista = linea.split()
            if lista[0] == 'INVITE' or lista[0] == 'ACK' or lista[0] == 'BYE':
                pass
            else:
                self.wfile.write(b'SIP/2.0 405 Method Not Allowed')
                break

            if (not 'sip' in lista[1].split(':') or
                  not 'SIP/2.0' in lista or not '@' in lista[1]):
                self.wfile.write(b'SIP/2.0 400 Bad Request')
                break

            if 'INVITE' in lista:
                self.wfile.write(b'SIP/2.0 100 Trying'
                + b'\r\n\r\n'+ b'SIP/2.0 180 Ring'
                + b'\r\n\r\n' + b'SIP/2.0 200 OK'
                + b'\r\n\r\n')

            elif 'ACK' in lista:
                os.system('./mp32rtp -i 127.0.0.1 -p 23032 < ' + sys.argv[3])

            elif 'BYE' in lista:
                self.wfile.write(b'SIP/2.0 200 OK'+ b'\r\n\r\n')


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit('Usage: python server.py IP port audio_file')
    else:
        print('Listening...')
    serv = socketserver.UDPServer(('', int(sys.argv[2])), EchoHandler)
    serv.serve_forever()
