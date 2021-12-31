from flask import Flask,request,jsonify
import numpy as np
import json
from absolute_calculator import AbsoluteDifference



class Server:

    def __init__(self):
        print("hello")

    def run(self):
        app = Flask(__name__)
        @app.route('/calculate')
        def absolute_difference():
            print(type(request.args.get("task")))
            input_data = request.args.get("task").split('\\n')
            print(input_data)
            obj = AbsoluteDifference(input_data[0])
            if not obj.checkTestCaseNumber():
                error_text = "Not a valid test case"
                return error_text
            else:
                result = obj.calculator(input_data[1:])
                result.append("I am from node2")
                print(result)
                return jsonify(result)

        app.run(host='0.0.0.0',port=5000)