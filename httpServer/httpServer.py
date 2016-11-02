#coding:utf-8
import socket
import re
import utils
from utils import httpserver
Host = ''
Port = 8000

if __name__ == '__main__':
    server = httpserver()
    server.run(Host,Port,10) 


#ok_header = '''HTTP/1.1 200 OK
#Content-Type: text/html

#'''
#index_content = ok_header
#with open('index.html',encoding='utf-8') as file:
##print(file.read())
##index_content = ok_header + file.read().decode('cp936')
##    data = file.read().decode('utf-8').encode('GBK')
#    index_content += file.read()
#    file.close()

## open rag.html
#file = open('rag.html','r')
#with open('rag.html','r',encoding='utf-8') as file:
#    rag_content = ok_header+ file.read()
#    file.close()

#file = open('1.jpg','rb')
#pic_header= 'HTTP/1.x 200 ok\nContent-Type: image/jpeg\n'
#file_content = file.read()
#length = len(file_content)
#pic_header += 'Content-Length' + str(length) + '\n\r\n'
#pic_content = pic_header + str(file_content)
#file.close()

#file = open('favicon.ico','rb')
#favicon_header = 'HTTP/1.x 200 ok\nContent-Type: image/x-icon\n'
#file_content = file.read()
#length = len(file_content)
#favicon_header += 'Content-Length'+str(length)+'\n\r\n'
#favicon_content = favicon_header + str(file_content)
#file.close()


#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.bind((Host,Port))
#s.listen(100)

## set up a connection and receive message
#while True:
#    conn,addr = s.accept()
#    request = conn.recv(1024)       # reqeust are bytes
#    request_str = request.decode('UTF-8')   # turn to str
##    print("request_str: " + str(type(request_str)) + "\n")
#    method = request_str.split(' ')[0]
##    print("split : "+ str(request_str.split(' ')))
#    print(str(len(request_str.split(' '))))
#    src = request_str.split(' ')[1]                                                     # list index out of range    why?

    
#    print('Connect by: ' + str(addr))
#    print('Request is :\n'+request_str)
    
#    if method == 'GET':
#        if src == '/index.html':
#            content = index_content
#        elif src == '/1.jpg':
#            content = pic_content
#        elif src == '/rag.html':
#            content = rag_content
#        elif src == '/favicon.ico':
#            content = favicon_content
#        elif re.match('^/\?.*$',src):
#           # raise a 404 page error
#            entry = src.split('?')[1]
#            content = ok_header
#            content += entry
#            content += '<br /><font color="green" size="7">register successs!</p>'
#        else:
#            continue

#    elif method == 'POST':
#        form = request.split('\r\n')
#        entry = form[-1]
#        content = ok_header
#        content += entry
#        content += '<br /><font color="green" size="7">register successs!</p>'
        
#    else:
#        continue
#    conn.sendall(content.encode('utf-8'))
#    conn.close() 