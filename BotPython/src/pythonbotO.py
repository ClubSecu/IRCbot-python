# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


import socket

class Pybot:
    
    def __init__(self, HOST="irc.clubsecu.fr",PORT=6667,NICK="Sp1p3-Bot3000",IDENT="BOT",REALNAME="Sp1p3-Bot"):
        self.HOST = HOST
        self.PORT = PORT
        self.NICK = NICK
        self.IDENT = IDENT
        self.REALNAME = REALNAME
        self.readbuffer=""
        self.soc=s=socket.socket()
        
        
    def connect():
        s.connect((HOST, PORT))
        s.send("NICK %s\r\n" % NICK)
        s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
        out=""; 
        
        while out!="PING":
            readbuffer=readbuffer+s.recv(1024)
            temp=string.split(readbuffer, "\n")
            readbuffer=temp.pop( )

            for line in temp:
                line=string.rstrip(line)
                line=string.split(line)

                if(line[0]=="PING"):
                    s.send("PONG %s\r\n" % line[1])
                    out="PING"
                
            
            return s    
                
    def runRead(sock):
        
        while 1:
            readbuffer=readbuffer+sock.recv(1024)
            temp=string.split(readbuffer, "\n")
            readbuffer=temp.pop()
        
            for line in temp:
                line=string.rstrip(line)
                line=string.split(line)
            
            print(line)
            
               
        return 0
 
