# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys
import socket
import string
import os

__author__ = "canillas"
__date__ = "$26 fevr. 2015 11:38:54$"


#tentative de POO avec le bot

class bot:
    
    HOST="irc.clubsecu.fr"
    PORT=6667
    NICK="Dame-Bot"
    IDENT="BOT"
    REALNAME="Dame-Bot"
    readbuffer=""
    s=socket.socket( )
    d=[]
    
    
    def readline(self,line): #ne gere que PING, PVMSG et JOIN
    
        message=""
    #je traite les  privmsg et les join et les ping FAIRE UN CASE SWITCH
    
    #ajout d un champ type toujours present pour faire du traitement sur les 
    #types d'action
    
    
    # la taille du tableau est fixe je peux donc forger mon dictionnaire
        if (line[0]=="PING"):
            d = dict(id=0,usr ='serv',act='ping',src=line[1])
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
            d=dict( id = 1,usr = user, act = action, src = source, msg = message)     
            return d
    #la taille du tableau est fixe je peux donc forger mon dictionnaire
        if (line[1]=="JOIN"):
            d=dict(id=2,usr=line[0],act=line[1],whr=line[2])
            return d
    
    
    def __init__(self):
        
        self.s=socket.socket( )
        self.s.connect((self.HOST, self.PORT))
        self.s.send("NICK %s\r\n" % self.NICK)
        self.s.send("USER %s %s bla :%s\r\n" % (self.IDENT, self.HOST, self.REALNAME))
        while 1:
            self.readbuffer=self.readbuffer+self.s.recv(1024)
            temp=string.split(self.readbuffer, "\n")
            self.readbuffer=temp.pop( )

            for line in temp:
                line=string.rstrip(line)
                line=string.split(line)

                if(line[0]=="PING"):
                    self.s.send("PONG %s\r\n" % line[1])
         #connection a  irc    
            print(line)
            self.d=self.readline(line)
            print(self.d)
    
    
    
     
