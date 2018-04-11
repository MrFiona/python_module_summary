#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-04-10 23:11
# Author  : MrFiona
# File    : http_server.py
# Software: PyCharm



from http.server import BaseHTTPRequestHandler, HTTPServer
from io import StringIO

from 简单构建Http服务器.test_server import test


class HttpServer(BaseHTTPRequestHandler):
    post_num = 0
    string_io = StringIO()

    def do_POST(self):
        body = self.rfile.read(int(self.headers['Content-Length']))
        # if len(HttpServer.string_io.getvalue()) == 0:
        test(HttpServer.string_io, HttpServer.post_num)
        print("HttpServer.string_io.getvalue():\t", HttpServer.string_io.getvalue())
        print("body:\t", body)
        self.send_response(200)
        self.send_header("Content-Type", "text/ascii")
        self.send_header("Content-Length", "2")
        self.end_headers()
        self.wfile.write(b"OK")
        HttpServer.post_num += 1
        print("HttpServer.post_num:\t", HttpServer.post_num)


httpd = HTTPServer(('', 8088), HttpServer)
httpd.serve_forever()




