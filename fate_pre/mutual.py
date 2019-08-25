#!/usr/bin/env python
# coding: utf-8

from tornado.web import Application,RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import options,define,parse_command_line
from tornado.httpserver import HTTPServer
from tornado.escape import json_encode,utf8
import csv
import pandas as pd
from util import predict
import numpy as np


def load_data_topredict():
    user_data = np.zeros((10, 5))
    with open("data.txt", "r")as file:
        for idx, line in enumerate(file.readlines()):
            user_data[idx] = line.split(",")[1:]
    return predict(user_data)

define("port",default=4321,type=int)

class TestHandler(RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin",'*')
        self.set_header("Access-Control-Allow-Methods",'POST,GET,PUT,DELETE,OPTIONS')
        self.set_header("Access-Control-Allow-Credentials",'True')
        self.set_header("Access-Control-Max-Age",1000)
        self.set_header("Access-Control-Allow-Headers",'*')
        self.set_header("Content-type",'application/json')
        # print(self.get_arguments("data"))
        s = self.get_argument("data")
        pre = load_data_topredict()
        # print(s)
        result_header = [{
            "developmentId":80015,
            "id":"leave-17",
            "name":"leave",
            "version":17,
			"result":pre
        },{
            "developmentId":80012,
            "id":"leave-15",
            "name":"leave",
            "version":15,
        }]
        self.write(json_encode(result_header))
        # self.write(json_encode(pre))
        self.finish()



app = Application(handlers=[('/test/',TestHandler)])
http_server = HTTPServer(app)
http_server.bind(options.port)
http_server.start(1)
IOLoop.current().start()





