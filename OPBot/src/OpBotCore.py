# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys
import socket
import string
import os

# POO directly implemented

__author__ = "jbussery"
__date__ = "$5 mars 2015 10:56:47$"

class botinst :
    
    # Attributs
    HOST="irc.clubsecu.fr"
    PORT=6667
    NICK="Moderator-Bot"
    IDENT="BOT"
    REALNAME="Moderator-Bot"
    readbuffer=""
    s=socket.socket( )
    d=[]
    
    # Function to read the irc flow
    def readline(self,line):
    
        