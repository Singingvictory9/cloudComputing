from http.server import HTTPServer, BaseHTTPRequestHandler
from flask import Flask
import json
import requests
import csv

app = Flask(__name__)
class MyHandler(BaseHTTPRequestHandler):

 def _set_response(self, code):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

#@app.route('/')
def do_GET(self):
    self.do_GET_ListTable()
    # example: this is how you get path and command
    print(self.path)
    print(self.command)

@app.route('/api/tables/', methods=['GET'])
def do_GET_ListTable(self):
        print("inside func")
        print(self.path)
        data2 = {
            "row": "sample_b",
            "data2": [
                {
                    "value": "data_b",
                    "time": "1234"
                }
            ]
        }
        data_json2 = json.dumps(data2,)

        self._set_response(200)
        self.wfile.write(data_json2.encode("utf8"))

        print("do_GET_ListTable")
def do_POST_CreateTable(self):
        print("Create Table")
        print(self.path)
        data = None
        content_length = self.headers['content-length']

        if content_length != None:
            content_length = int(content_length)
            data = self.rfile.read(content_length)
         #print the content, just for you to see it =)
        print(data)
        datafortable = json.loads(data)
        print (datafortable)
        print(datafortable["name"])

        TableList = []
        TableList.append(data)

        with open( datafortable["name"]+'.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([datafortable["column_families"][0]["column_family_key"],
                                 datafortable["column_families"][0]["columns"][0],
                                 datafortable["column_families"][0]["columns"][1],
                                 datafortable["column_families"][1]["columns"][0],
                                 datafortable["column_families"][1]["columns"][1],"row", "data"])

@app.route('/api/tables/<int:pk>', methods=['GET'])
def do_GET_GetTableInfo(self):
        print("Getting Table Info")
        print(self.path)
        url = MySupport.url(self.HOSTNAME, self.PORT, "/api/tables")
        url_table1 = url + "/table1"  # no longer exists
        url_table2 = url + "/table2"

        expected = {
            "name": "table2",
            "column_families": [
                {
                    "column_family_key": "key1",
                    "columns": ["column_key1", "column_key2"]
                },
                {
                    "column_family_key": "key2",
                    "columns": ["column_key3", "column_key4"]
                }
            ]
         }
        data_json2 = json.dumps(expected, pk)
        self._set_response(200, pk)
        self.wfile.write(expected.encode("utf8"))

@app.route('/api/tables/<int:pk>', methods=['DELETE'])
def do_DELETE(self):
    # example: send just a 200
    self._set_response(200)

#Bigtable Control functions

@app.route('/api/tables/<int:pk> <int:cell>', methods=['GET'])
def do_GET_RetrieveACell(self):
        print("Retrieve A Cell")
        print(self.path)

@app.route('/api/tables/<int:pk> <int:cells>', methods=['GET'])
def do_GET_RetrieveCells(self):
        print("Retrieve  Cells")
        print(self.path)

@app.route('/api/tables/<int:pk> <int:row>', methods=['GET'])
def do_GET_RetrieveRow(self):
        print("Retrieve Row" )
        print(self.path)

if __name__ == '__main__':
    server_address = ("localhost", 8080)
    handler_class = MyHandler
    server_class = HTTPServer

    httpd = HTTPServer(server_address, handler_class)
    print("sample server running...")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()