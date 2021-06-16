{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3b4e5cfe",
   "metadata": {},
   "outputs": [],
   "source": [
    "import socket \n",
    "import cv2\n",
    "import pickle\n",
    "import struct\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7d411f6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "host name DESKTOP-ACUL1B1\n",
      "HOST IP: 192.168.56.1\n"
     ]
    }
   ],
   "source": [
    "# Socket Create\n",
    "server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n",
    "host_name  = socket.gethostname()\n",
    "host_ip = socket.gethostbyname(host_name)\n",
    "print('host name',host_name)\n",
    "print('HOST IP:',host_ip)\n",
    "port = 1234\n",
    "socket_address = (host_ip,port)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "03fb5a09",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LISTENING AT: ('192.168.56.1', 1234)\n"
     ]
    }
   ],
   "source": [
    "# Binding the Socket\n",
    "server_socket.bind(socket_address)\n",
    "\n",
    "# listening\n",
    "server_socket.listen(5)\n",
    "print(\"LISTENING AT:\",socket_address)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e91382eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "GOT CONNECTION FROM: ('192.168.56.1', 56799)\n"
     ]
    },
    {
     "ename": "OSError",
     "evalue": "[WinError 10038] An operation was attempted on something that is not a socket",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-c364c87c5882>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      9\u001b[0m             \u001b[0ma\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpickle\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdumps\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mframe\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m             \u001b[0mmessage\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstruct\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpack\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Q\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 11\u001b[1;33m             \u001b[0mclient_socket\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msendall\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     12\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     13\u001b[0m             \u001b[0mcv2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mimshow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'TRANSMITTING VIDEO'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mframe\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mOSError\u001b[0m: [WinError 10038] An operation was attempted on something that is not a socket"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    client_socket,addr = server_socket.accept()\n",
    "    print('GOT CONNECTION FROM:',addr)\n",
    "    if client_socket:\n",
    "        vid = cv2.VideoCapture(0)\n",
    "        \n",
    "        while(vid.isOpened()):\n",
    "            img,frame = vid.read()\n",
    "            a = pickle.dumps(frame)\n",
    "            message = struct.pack(\"Q\",len(a))+a\n",
    "            client_socket.sendall(message)\n",
    "            \n",
    "            cv2.imshow('TRANSMITTING VIDEO',frame)\n",
    "            key=cv2.waitKey(1)\n",
    "            if key==13:\n",
    "                client_socket.close()\n",
    "                    \n",
    "cv2.destriyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "585b3ab3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c88a5c56",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
