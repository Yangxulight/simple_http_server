import socket
import os.path as path
from types import *
Host = ''
Port = 8000
ok_header = '''HTTP/1.1 200 OK
Content-Type: text/html

'''
file_content = '''<html>
<head>
<title>JinanUniversity</title>
</head>

<body>
<p>PythonHTTPServer</p>
<img src="1.jpg"/>
</body>
</html>
'''


# default 'text/plain'
MIMEType_Dict = {
	'.html':'text/html',
	'.xml':'text/xml',
	'.gif':'image/gif',
	'.jpg':'image/jpeg',
	'.png':'image/png',
	'default':'text/plain'
}


class http_server(object):
	def __init__(self):
		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

	def run(self,host="",port=8000,max_connection=100):
		self.s.bind((host,port))
		self.s.listen(max_connection)
		print_host = ''
		if host == '':
			print_host = 'localhost'
		print("Runing server on %s:%d" % (print_host,port))
		while True:
			try:
				conn,addr = self.s.accept()
				print("Receive request from "+ str(addr))
			except KeyboardInterrupt:
				break
			except socket.error as msg:
				print('%s'%msg)
			do_server(conn)

def do_server(s):
	request_bytes = s.recv(1024)
	request = request_bytes.decode('utf-8')
	print("The content of the request is:\n"+request)
	# method,src = parse_request(request)
	# response = get_response(file_content,'text/html')
	# response_bytes = response.encode('utf-8')	
	# s.sendall(response_bytes)
	handle_request(request,s)


# localhost:8000/index.html
# GET /index.html HTTP/1.1
# Accept: text/html, application/xhtml+xml, image/jxr, */*
# Accept-Language: zh-Hans-CN,zh-Hans;q=0.5
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393
# Accept-Encoding: gzip, deflate
# Host: localhost:8000
# Connection: Keep-Alive

def parse_request(request):
	method,src = request.split(' ')[0], request.split(' ')[1][1:]
	# print("method: %s,src: %s"%(method,src))
	return method, src

# 返回请求包装
def get_response(content,MIMEType):
	content_length = len(content)
	header = "HTTP/1.0 200 OK\r\n"\
			+"Server: myHttpServer\r\n"\
			+"Content-Type:" + MIMEType+"\r\n"\
			+"Content-Length:" + str(content_length)+"\r\n\r\n"
	header = to_bytes(header)
	content = to_bytes(content)
	response = header + content
	return response	

# 获取主体
def get_content(filename,encoding='utf-8'):
	# 获取文件类型
	file_type = path.splitext(filename)[1]
	if file_type == '.html' or file_type == '.txt':
		f = open(filename,'rt',encoding=encoding)
		ret = f.read()
		ret.encode('utf-8')
	else:
		f = open(filename,'rb')
		ret = f.read()
	f.close()
	return ret

def get_MIMEType(filename):
	file_type = path.splitext(filename)[1]
	ret = ''
	if file_type in MIMEType_Dict:
		ret = MIMEType_Dict[file_type]
	else:
		ret = MIMEType_Dict['default']
	return ret

def handle_request(request,s):
	method ,src = parse_request(request)
	if method == 'GET':
		MIMEType = get_MIMEType(src)
		content = get_content(src)
		# content = file_content
		response = get_response(content,MIMEType)
		# print("sending request:\n"+response.decode('utf-8'))
		# response_bytes = response.encode('utf-8')
		s.sendall(response)
	elif method == 'POST':
		form = request.split('\r\n')
		# 找到空的一行
		idx = form.index('')
		entry = form[idx:]
		values = entry[-1].split('=')[-1]
		response = file_content + '\n' + '<p>'+ values + '</p>'
		response = to_bytes(response)
		s.sendall(response)

def to_bytes(s):
	if isinstance(s,bytes):
		return s
	else:
		return s.encode('utf-8')

if __name__ == '__main__':
	server = http_server()
	server.run(Host,Port)