# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import re
import socket
import string
from time import gmtime, strftime

__author__ = "Fabien"
__date__ = "$26 mars 2015 17:41:54$"

privmsg = re.compile(r"^:(.*)!.* PRIVMSG (#[^ ]*) :(.*)$")

class Bot:

    def __init__(self, serv, port, chan, nick, ident, realname):
        self.nick = nick
        self.serv = serv
        self.port = port
        self.chan = chan
        self.ident = ident
        self.realname = realname
        self.master = ident
        
        # Buffer and socket
        self.s = socket.socket( )
        self.buffer = ''
        
        # Triggers !
        self.trigger = {
                        'Repeat': False,
                        'Record': False,
                        }
        
        print 'New bot:' + self.nick
        
    # connect() : connexion to an IRC server
    def connect(self):
        print 'Connect to: ' + self.serv + ':' + str(self.port)
        self.s.connect((self.serv, self.port))
        connected = False
        while not connected:
            self.readlines()
            for self.line in self.buffer:
                if self.line is not '':
                    match = re.match(r".* NOTICE AUTH .* Found .*$", self.line)
                    if match:
                        self.command_nick(self.nick)
                        self.s.send('USER %s %s bla :%s\r\n' % (self.nick, self.serv, self.realname))
                    match = re.match(r"^PING (:.*)$", self.line)
                    if match:
                        self.s.send('PONG ' + match.group(1) + "\r\n")
                        connected = True
    
    # readlines() : read lines printed
    def readlines(self):
        self.buffer = self.s.recv(2048)
        temp = string.split(self.buffer, '\r\n')
        self.buffer = temp
    
    # join(string) : /JOIN channel
    def command_join(self, chan):
        self.s.send('JOIN ' + chan + '\r\n')
        
    # nick(string) : /NICK nickname
    def command_nick(self, nick):
        self.s.send('NICK %s\r\n' % (nick))
        
    # kick(string,string) : /KICK nickname reason
    def command_kick(self, nick, reason):
        self.s.send('KICK %s %s\r\n' % (nick, reason))
    
    def command_ping(self):
        self.match = re.match(r"^PING (.*)$", self.line)
        if self.match:
            self.s.send('PONG %s\r\n' % self.match(1))

    # trigger_turn(string,string) : turn on or off a trigger
    def trigger_turn(self, trig, turn):
        if trig in self.trigger.keys():
            if turn == 'on':
                self.trigger[trig] = True
                self.s.send('PRIVMSG %s Trigger : %s on\r\n' %(self.chan, trig))
            elif turn == 'off':
                self.trigger[trig] = False
                self.s.send('PRIVMSG %s Trigger : %s off\r\n' %(self.chan, trig))
        else:
            self.s.send("PRIVMSG %s Trigger : %s doesn't existe\r\n" %(self.chan, trig))
        
    # function_repeat() : bot will repeat everything
    def function_repeat(self,line):
        if self.trigger['Repeat']:
            m = privmsg.match(line) # Get informations about the message
            if m:
                self.s.send('PRIVMSG %s %s : %s\r\n' % (m.group(2), m.group(1), m.group(3)))
    
    def function_record(self,line):
        if self.trigger['Record']:
            self.match = privmsg.match(line) # Get informations about the message
            if self.match:
                f = open("irc.log", 'a')
                f.write(strftime("%d %b %Y %H:%M:%S ") + '%s - %s : %s\r\n' % (self.match.group(2), self.match.group(1), self.match.group(3)))
                f.close()
            
    def function_botmaster(self,line):
        self.match = privmsg.match(line) # Get informations about the message
        if self.match:
            if self.master == self.match.group(1):
                master_msg = re.match(r"^(" + bot.nick + r") : ([a-zA-Z]*) ([on|off]*)$",self.match.group(3))
                if master_msg:
                    bot.trigger_turn(master_msg.group(2),master_msg.group(3))
        
    # functions() : lauch all functions
    def functions(self,line):
        self.function_repeat(line)
        self.function_record(line)