#!/usr/bin/env python# -*- coding: utf-8 -*-import socketsock = socket.socket()sock.connect(('127.0.0.1', 9090))sock.send('lol'.encode())data = sock.recv(1024)sock.close()# data = sock.recv(1024).decode()print(data)