from flask import Flask, Response
from flask_restful import Resource, Api
import json 


def DummyApis(server):
    @server.route("/api/sachin", methods=["GET", "POST"])
    def api():
        return {'hello': 'world'}
    # api.add_resource(HelloWorld, '/hello')


    @server.route("/api/dummy", methods=["GET", "POST"])
    def dummy_api():
        return {'hello': 'This is dummy api'}
