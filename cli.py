#!/usr/bin/env python# -*- coding: utf-8 -*-import socketsock = socket.socket()sock.bind(('192.168.3.156', 6000))sock.listen(1)while True:    conn, addr = sock.accept()    data = conn.recv(1024)    print(data)    conn.close()