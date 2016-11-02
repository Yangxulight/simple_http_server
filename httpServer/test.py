# A test file for every module in utils
import socket
import utils


#   RequestHandler
# Test for parse()
def test_parse():
    handler = utils.RequestHandler()
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error:
        print("socket created error\n")
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((Host,Port))
    s.listen(5)
    while True:
        client, addr = s.accept()
        data = client.recv(4096).decode('utf-8')
        method, URI, protocal, body = handler.parse(data)
        print("method:%s\nURI:%s\nprotocal:%s\nbody:%s" % (method,URI,protocal,body))
        client.close()
    s.close() 
