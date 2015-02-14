
import sys
import socket
import string

def tata(line,s):
    for word in line: 
        if(word ==":TATA"):
            s.send("PRIVMSG #resir TUTU \r\n")
    

def toto(line,s):
    for word in line: 
        if(word ==":TOTO"):
            s.send("PRIVMSG #resir TATA \r\n")

def readline(line,d):
    
    message=""
    #je traite les  privmsg et les join
    
    # la taille du tableau est fixe je peux donc forger mon dictionnaire
    if (line[0]=="PING"):
        d = dict(usr ='serv',act='ping',src=line[1])
        return d 
    #la taille du tableau est variable     
    if (line[1]=="PRIVMSG"):
        user=line[0]
        action=line[1]
        source=line[2]
        #je recupere les informations "fixe" et je les enleve du tableau 
        line.pop(2)
        line.pop(1)
        line.pop(0)
        # je concatene tout le reste 
        for word in line:
            message = message+word+" "
        #j'enleve le premiere caractere ":" pour avoir un message parsable 
        message=string.lstrip(message,':')
        d=dict( usr = user, act = action, src = source, msg = message)     
        return d
    #la taille du tableau est fixe je peux donc forger mon dictionnaire
    if (line[1]=="JOIN"):
        d=dict(usr=line[0],act=line[1],whr=line[2])
        return d
        

def run():
    HOST="irc.clubsecu.fr"
    PORT=6667
    NICK="Sp1p3-Bot"
    IDENT="BOT"
    REALNAME="Sp1p3-Bot"
    readbuffer=""
    d=dict()



    s=socket.socket( )
    s.connect((HOST, PORT))
    s.send("NICK %s\r\n" % NICK)
    s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))

    while 1:
        readbuffer=readbuffer+s.recv(1024)
        temp=string.split(readbuffer, "\n")
        readbuffer=temp.pop( )

        for line in temp:
            line=string.rstrip(line)
            line=string.split(line)

            if(line[0]=="PING"):
                s.send("PONG %s\r\n" % line[1])
         #connection a  irc    
            print(line)
            
          #affichage de debug 
          
          #debut des actions avec "line" comme flux de donnee 

            toto(line,s)        
            tata(line,s)        
            print(readline(line, d))
           