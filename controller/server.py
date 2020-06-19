import socket
from socket import error as SocketError
import errno
import sys
import json
sys.path.append('..')
from googleNewsGetter import getNews
from twitterGetter import getTweet
from feedGetter import google_res
from feedGetter import twitter_res

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 10001        # Port to listen on (non-privileged ports are > 1023)

server_address = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('STARTING UP ', HOST, ' ON PORT ', PORT)
sock.bind(server_address)
sock.listen(1)

while True:
        print('WAITING CONNECTION...')
        connection, addr = sock.accept()
        try:
            print('CONNECTION FROM:', addr)
            i = 0
            while True:
                data = connection.recv(16)
                dataD = data.decode('utf-8')
                print('RECEIVED:', dataD)
                if dataD:
                    #Request for google and twitter news
                    print('getting news...')

                    allTweets = getTweet(dataD)
                    twitter_res(allTweets)

                    allNews, urlNews = getNews(dataD)
                    google_res(allNews)

                    while i != 10:
                        try:
                            print('SENDING FROM TWITTER' + allTweets[i][0] + '\n')
                            connection.sendall(allTweets[i][0].encode('utf-8'))
                        except SocketError as e:
                            if e.errno != errno.ECONNRESET:
                                raise
                            pass
                        print('post except')
                        i += 1
                    i = 0
                    while i != 10:
                        try:
                            print('SENDING FROM GOOGLE' + allNews[i][0] + '\n')
                            connection.sendall(allNews[i][0].encode('utf-8'))
                        except SocketError as e:
                            if e.errno != errno.ECONNRESET:
                                raise
                            pass
                        i += 1
                    break
                else:
                    print(sys.stderr, 'NO MORE DATA FROM ', addr)
                    break
        finally:
            connection.close()