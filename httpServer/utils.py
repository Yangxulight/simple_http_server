import re
import socket
from config import route,setting
from email.utils import formatdate
from os.path import isfile
from os.path import splitext
ok_header_html = '''HTTP/1.1 200 OK
Content-Type: text/html

'''
ok_header_jpg = '''HTTP/1.x 200 ok
Content-Type: image/jpg

'''

error_header = '''
'''
# some simple http codes status map
Http_code_list = {
100:"100 Continue",
200:"200 OK",
202:"202 Accepted",
403:"403 Forbidden",
404:"404 Not Found",
502:"502 Bad Gateway",
503:"503 Service Unavailable",
504:"504 Gateway Time-out"
}

class httpserver(object):

    def __init__(self):
        try:
            self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error:
            print(" Server socket created failed.\n")
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        self.handler = RequestHandler()

    
    def run(self,host,port,max_connect = 10):
        try:
            self.s.bind((host,port))
            self.s.listen(max_connect)  
            while True:
                try:
                    client_conn,addr = self.s.accept()
                    request = self.handler.receive(client_conn,4096)
                    method,URI,protocal,body = self.handler.parse(request)
                    if method == "GET":
                        file_path = self.handler.get_abs_dir(URI)
                        contents, content_type = self.handler.get_contents_content_type(URI)
                        response = self.handler.respond(content_type,contents)
                except Error_404:
                    response = self.handler.respond('text/plain','File not found',404)
                except Error_502:
                    response = self.handler.respond('text/plain','Bad Gateway',502)
                finally:
                    client_conn.send(response.encode('utf-8'))
                    client_conn.close()
        finally:
            self.s.close()

    def do_get(filename):

        response = ''
        return response
    def do_post(filename,argv):
        return 0
    def parse(request):
        message = request.spilt('\r\n',1)
    
    # return all the src from the html content
    def search_redirect(http_content):
        src_list = []
        return src_list
    
    def error_page():
        error_page_path = route("error_page")
        error_page = ''
        with open(error_page_path,encodeing='utf-8') as f:
            error_page = error_header + f.read()
            f.close()
        return error_page
    
    def run_server(host,port):
        self.host = host
        self.port = port
        pass
   
class RequestHandler(object):
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)
# create response to client    
    def respond(self,content_type,contents,status_code=200):
        # convert content into bytes, reqired by python3
        if not isinstance(contents,bytes):
            contents = contents.encode('utf-8')
        response = []
        response.append(setting['protocal']+' %s' % Http_code_list[status_code])
        response.append('Date: %s' % formatdate(usegmt=True))
        response.append('Content-type: %s; Character-Type: UTF-8' % (content_type))
        response.append('Conetent-Length: %s' % str(len(contents)))
        response.append('\r\n%s' % contents)
        return '\r\n'.join(response) 


# receive a request from the client connection
    def receive(self,client_conn,buffer_size = 4096):
        request = ''
        while True:
            buff = client_conn.recv(buffer_size)
            request += buff.decode('utf-8')
            if len(buff) < buffer_size:
               return request
        
        
#GET /1.jpg HTTP/1.1
#Host: localhost:8000
#Connection: keep-alive
#Cache-Control: max-age=0
#Upgrade-Insecure-Requests: 1
#User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36
#Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
#Accept-Encoding: gzip, deflate, sdch, br
#Accept-Language: zh-CN,zh;q=0.8


#GET /1.html HTTP/1.1
#Host: localhost:8000
#Connection: keep-alive
#Upgrade-Insecure-Requests: 1
#User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36
#Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
#Accept-Encoding: gzip, deflate, sdch, br
#Accept-Language: zh-CN,zh;q=0.8

#   check the client request into [method,URI,protocal,body] 
    def parse(self,request):
        content = request.split('\r\n',1)   # only take the first two lines
        line0, body = content[0].split(' ',2), content[1]
        method, URI, protocal = line0[0],line0[1],line0[2]
        return method,URI,protocal,body

    def get_abs_dir(self,URI):       # return the right uri in the server
        root_dir = route["root"]
        abs_path = root_dir+URI
        return abs_path


    def get_contents_content_type(self,filename):
    # get the file type
        file_type = splitext(filename)[1][1:]
        abs_path = route['root']+ filename
        content_type = 'text/plain'
        with open(abs_path,'rb') as f:
            contents = f.read()
        if file_type == 'jpg' or file_type == 'jpeg' or file_type == 'bmp' or file_type == 'gif':
            content_type = 'image/jpeg'
        elif file_type == 'html':
            content_type = 'text/plain'
        return contents,content_type

class Error_404(Exception):
    pass
class Error_502(Exception):
    pass
            
