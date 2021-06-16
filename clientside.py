{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d831f628",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import struct\n",
    "import pickle\n",
    "import socket"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3acc1cd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n",
    "host_ip = '192.168.56.1' # paste your server ip address here\n",
    "port = 1234\n",
    "client_socket.connect((host_ip,port)) # a tuple\n",
    "data = b\"\"\n",
    "payload_size = struct.calcsize(\"Q\")\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "775169d7",
   "metadata": {},
   "outputs": [
    {
     "ename": "error",
     "evalue": "unpack requires a buffer of 8 bytes",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31merror\u001b[0m                                     Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-0fef9594616b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[0mpacked_msg_size\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mpayload_size\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m     \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mpayload_size\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m     \u001b[0mmsg_size\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstruct\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0munpack\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Q\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mpacked_msg_size\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m     \u001b[1;32mwhile\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m<\u001b[0m \u001b[0mmsg_size\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31merror\u001b[0m: unpack requires a buffer of 8 bytes"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    while len(data) < payload_size:\n",
    "        packet = client_socket.recv(4*1024) # 4K\n",
    "        if not packet: break\n",
    "        data+=packet\n",
    "    packed_msg_size = data[:payload_size]\n",
    "    data = data[payload_size:]\n",
    "    msg_size = struct.unpack(\"Q\",packed_msg_size)[0]\n",
    "    \n",
    "    while len(data) < msg_size:\n",
    "        data += client_socket.recv(4*1024)\n",
    "    frame_data = data[:msg_size]\n",
    "    data  = data[msg_size:]\n",
    "    frame = pickle.loads(frame_data)\n",
    "    cv2.imshow(\"RECEIVING VIDEO\",frame)\n",
    "    key=cv2.waitKey(1)\n",
    "    if key==13:\n",
    "        break;\n",
    "       \n",
    "    \n",
    "client_socket.close()\n",
    "cv2.destroyAllWindows() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9087dee9",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e591ffb2",
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
