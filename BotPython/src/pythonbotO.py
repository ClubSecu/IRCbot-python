# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "canillas"
__date__ = "$13 fevr. 2015 14:42:01$"


import socket

class Pybot:
    
    def __init__(self, HOST="irc.clubsecu.fr",PORT=6667,NICK="Sp1p3-Bot3000",IDENT="BOT",REALNAME="Sp1p3-Bot"):
        self.HOST = HOST
        self.PORT = PORT
        self.NICK = NICK
        self.IDENT = IDENT
        self.REALNAME = REALNAME
        self.readbuffer=""
        self.s=s=socket.socket()
        
    def connect():
        s.connect((HOST, PORT))
        s.send("NICK %s\r\n" % NICK)
        s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
        out=[]; 
        
        while !(line[0]=="PING"):
            readbuffer=readbuffer+s.recv(1024)
            temp=string.split(readbuffer, "\n")
            readbuffer=temp.pop( )

            for line in temp:
                line=string.rstrip(line)
                line=string.split(line)

                if(line[0]=="PING"):
                    s.send("PONG %s\r\n" % line[1])
                    out[0]="PING"
            
                print(line)
 