from http.server import HTTPServer, BaseHTTPRequestHandler
from flask import Flask
import json
import requests

app = Flask(__name__)
class MyHandler(BaseHTTPRequestHandler):
    def _set_response(self, code):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    #@app.route('/api/tables', methods=['GET'])
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
        data_json2 = json.dumps(data2)

        self._set_response(200)
        self.wfile.write(data_json2.encode("utf8"))

        print("do_GET_ListTable")
    def do_GET_GetTableInfo(self):
        print("Getting Table Info")
        print(self.path)
    def do_GET_RetrieveACell(self):
        print("Retrieve A Cell")
        print(self.path)

    def do_GET_RetrieveRow(self):
        print("Retrieve Row" )
        print(self.path)



    def do_GET(self):
        self.do_GET_ListTable()
        # example: this is how you get path and command
        print(self.path)
        print(self.command)

        if self.path =="/api/tables":
            self.do_GET_ListTable()

        elif self.path == "api/tables/:pk":
            self.do_GET_GetTableInfo()

        elif self.path == "api/tables/:pk/cell":
            self.do_GET_RetrieveACell()

        elif self.path == "api/tables/:pk/cells":

            self.do_GET_RetrieveCells()

        elif self.path == "api/tables/:pk/row":
            self.do_GET_RetrieveRow()


        # example: returning an object as JSON
        #data = {
            #"row": "sample_a",
            #"data": [
                #{
                    #"value": "data_a",
                    #"time": "1234"
                #}
            #]
        #}
        #data_json = json.dumps(data)

        #self._set_response(200)
        #self.wfile.write(data_json.encode("utf8"))




        self._set_response(200)



    def do_POST_CreateTable(self):
        print("Create Table")
        print(self.path)

    def do_POST_InsertACell(self):
        print("Insert cell")
        print(self.path)

    def do_POST_SetMemTableMaxEntries(self):
        print("Setting mem table entry")
        print(self.path)

    def do_POST(self, url, data):
        # example: reading content from HTTP request
        # data = None
        content_length = self.headers['content-length']

        # if content_length != None:
        #     content_length = int(content_length)
        #     data = self.rfile.read(content_length)
        #
        #     # print the content, just for you to see it =)
        #     print(data)
        #     try:
        #         res = requests(POST, url, data)
        #         if res is not None:
        #             set_response(200)
        #     except:
        #         print("Error occurred"
        if self.path == "/api/tables":
                    self.do_POST_CreateTable()

        elif self.path == "api/tables/:pk/cell":
                    self.do_POST_InsertACell()

        elif self.path == "api//memtable":
             self.do_POST_SetMemTableMaxEntries()

    def do_DELETE(self):
        # example: send just a 200
        self._set_response(200)


    # @app.route('/api/tables', methods=['POST'])
    # def do_POST_CreateTable(self):
    #     print("do_POST_CreateTable")
    #
    # @app.route("/api/tables,methods==['DELETE']")
    # def do_DELETE_deletetable(self):
    #     print("do_DELETE_DeleteTable")
    #
    # @app.route("/api/tables,methods==['GET']")



if __name__ == "__main__":
    server_address = ("localhost", 8080)
    handler_class = MyHandler
    server_class = HTTPServer

    httpd = HTTPServer(server_address, handler_class)
    print("sample server running...")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt: pass

    httpd.server_close()









