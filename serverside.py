#server side streaming

import socket, cv2, pickle,struct,imutils

ssocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)
port = 9999
socket_address = (host_ip,port)


ssocket.bind(socket_address)


ssocket.listen(10)
print("LISTENING AT:",socket_address)


while True:
    csocket,addr = ssocket.accept()
    print('GOT CONNECTION FROM:',addr)
    if csocket:
        vid = cv2.VideoCapture(0)

        while(vid.isOpened()):
            img,frame = vid.read()
            frame = imutils.resize(frame,width=320) 
            a = pickle.dumps(frame)
          
            message = struct.pack("Q",len(a))+ a  # 2000000  + a (data)
            csocket.sendall(message) 
            
            cv2.imshow('SERVER VIDEO',frame)
            key = cv2.waitKey(1) & 0xFF
            if key == 13:
                csocket.close()