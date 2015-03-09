# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "jbussery&Lcanillas"
__date__ = "$6 mars 2015 10:09:20$"

import sys
import socket
import string
import os
import praw  #https://praw.readthedocs.org/en/v2.1.20/ sinon a commenter# #wrapper api reddit



def readline(line,d): #ne gere que PING, PVMSG et JOIN
    
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


def help(d,s):
    info =[]
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message                
                if (d['src'][0] == '#'):  #si le message est sur un salon                   
                    if(d['msg'] == "!helpreddit "):
                        print("User requested Help section")
                        info.append("Les flux reddit dispo sont : \n")
                        info.append("- NetSec : !netsec & !netsecbrief\n")
                        info.append("- Blackhat : !blackhat & !blackhatbrief\n")
                        info.append("- ReverseEngineering : !revengineering & revengineeringbrief\n")
                        info.append("- Malware : !malware & !malwarebrief\n")
                        for index in range(0, len(info) ):
                            print(info[index])
                            s.send("PRIVMSG #resir "+info[index]+"")


def netsec(d,s): #commentaire a faire 
    
    if (d != None): # je verifie que mon dicto n'est pas vide
            if 'act' in d: #je verifie que mon dictio est bien forme
                if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                    if (d['src'][0] == '#'):  #si le message est sur un salon
                   
                        if(d['msg'] == "!netsec "):
                            print("User requested Netsec section")
                            
                            r=praw.Reddit(user_agent='python_bot')
                            submissions=r.get_subreddit('netsec').get_hot(limit=5)
                            message = "Les 5 dernieres new hot de reddit sur netsec sont : \n"
                            s.send("PRIVMSG #resir "+message+"")
                            for x in submissions: 
                                message=str(x)+"\n"
                                s.send("PRIVMSG #resir "+message+"\n")
                                link=x.url
                                s.send("PRIVMSG #resir "+link+"\n")
                                
    
def netsecbrief(d,s): #commentaire a faire 
    
    if (d != None): # je verifie que mon dicto n'est pas vide
            if 'act' in d: #je verifie que mon dictio est bien forme
                if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                    if (d['src'][0] == '#'):  #si le message est sur un salon
                   
                        if(d['msg'] == "!netsecbrief "):
                            print("User requested Netsec section")
                            
                            r=praw.Reddit(user_agent='python_bot')
                            submissions=r.get_subreddit('netsec').get_hot(limit=5)
                            message = "Les 5 dernieres new hot de reddit sur netsec sont : \n"
                            s.send("PRIVMSG #resir "+message+"")
                            for x in submissions: 
                                message=str(x)+"\n"
                                s.send("PRIVMSG #resir "+message+"\n")
   
def blackhat(d,s): #commentaire a faire 

    
    if (d != None): # je verifie que mon dicto n'est pas vide
            if 'act' in d: #je verifie que mon dictio est bien forme
                if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                    if (d['src'][0] == '#'):  #si le message est sur un salon
                   
                        if(d['msg'] == "!blackhat "):
                            print("User requested Blackhat section")
                            
                            r=praw.Reddit(user_agent='python_bot')
                            submissions=r.get_subreddit('blackhat').get_hot(limit=5)
                            message = "Les 5 dernieres new hot de reddit sur blackhat sont : \n"
                            s.send("PRIVMSG #resir "+message+"")
                            for x in submissions: 
                                message=str(x)+"\n"
                                s.send("PRIVMSG #resir "+message+"\n")
                                link=x.url
                                s.send("PRIVMSG #resir "+link+"\n")
                                
def blackhatbrief(d,s): #commentaire a faire 
    
    if (d != None): # je verifie que mon dicto n'est pas vide
            if 'act' in d: #je verifie que mon dictio est bien forme
                if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                    if (d['src'][0] == '#'):  #si le message est sur un salon
                   
                        if(d['msg'] == "!blackhatbrief "):
                            print("User requested Blackhat section")
                            
                            r=praw.Reddit(user_agent='python_bot')
                            submissions=r.get_subreddit('blackhat').get_hot(limit=5)
                            message = "Les 5 dernieres new hot de reddit sur blackhat sont : \n"
                            s.send("PRIVMSG #resir "+message+"")
                            for x in submissions: 
                                message=str(x)+"\n"
                                s.send("PRIVMSG #resir "+message+"\n")
                                
def RevEngineering(d,s): #commentaire a faire 

    
    if (d != None): # je verifie que mon dicto n'est pas vide
            if 'act' in d: #je verifie que mon dictio est bien forme
                if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                    if (d['src'][0] == '#'):  #si le message est sur un salon
                   
                        if(d['msg'] == "!revengineering "):
                            print("User requested ReverseEngineering section")
                            
                            r=praw.Reddit(user_agent='python_bot')
                            submissions=r.get_subreddit('ReverseEngineering').get_hot(limit=5)
                            message = "Les 5 dernieres new hot de reddit sur ReverseEngineering sont : \n"
                            s.send("PRIVMSG #resir "+message+"")
                            for x in submissions: 
                                message=str(x)+"\n"
                                s.send("PRIVMSG #resir "+message+"\n")
                                link=x.url
                                s.send("PRIVMSG #resir "+link+"\n")
                                

def RevEngineeringbrief(d,s): #commentaire a faire 
    
    if (d != None): # je verifie que mon dicto n'est pas vide
            if 'act' in d: #je verifie que mon dictio est bien forme
                if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                    if (d['src'][0] == '#'):  #si le message est sur un salon
                   
                        if(d['msg'] == "!revengineeringbrief "):
                            print("User requested ReverseEngineering section")
                            
                            r=praw.Reddit(user_agent='python_bot')
                            submissions=r.get_subreddit('ReverseEngineering').get_hot(limit=5)
                            message = "Les 5 dernieres new hot de reddit sur ReverseEngineering sont : \n"
                            s.send("PRIVMSG #resir "+message+"")
                            for x in submissions: 
                                message=str(x)+"\n"
                                s.send("PRIVMSG #resir "+message+"\n")
 
def malware(d,s): #commentaire a faire 

    if (d != None): # je verifie que mon dicto n'est pas vide
            if 'act' in d: #je verifie que mon dictio est bien forme
                if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                    if (d['src'][0] == '#'):  #si le message est sur un salon
                   
                        if(d['msg'] == "!malware "):
                            print("User requested Malware section")
                            
                            r=praw.Reddit(user_agent='python_bot')
                            submissions=r.get_subreddit('Malware').get_hot(limit=5)
                            message = "Les 5 dernieres new hot de reddit sur malware sont : \n"
                            s.send("PRIVMSG #resir "+message+"")
                            for x in submissions: 
                                message=str(x)+"\n"
                                s.send("PRIVMSG #resir "+message+"\n")
                                link=x.url
                                s.send("PRIVMSG #resir "+link+"\n")
                                

def malwarebrief(d,s): #commentaire a faire 
    
    if (d != None): # je verifie que mon dicto n'est pas vide
            if 'act' in d: #je verifie que mon dictio est bien forme
                if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                    if (d['src'][0] == '#'):  #si le message est sur un salon
                   
                        if(d['msg'] == "!revengineeringbrief "):
                            print("User requested Malware section")
                            
                            r=praw.Reddit(user_agent='python_bot')
                            submissions=r.get_subreddit('Malware').get_hot(limit=5)
                            message = "Les 5 dernieres new hot de reddit sur malware sont : \n"
                            s.send("PRIVMSG #resir "+message+"")
                            for x in submissions: 
                                message=str(x)+"\n"
                                s.send("PRIVMSG #resir "+message+"\n")

def run():
    HOST="irc.clubsecu.fr"
    PORT=6667
    NICK="Reddit-Bot"
    IDENT="BOT"
    REALNAME="Sp1p3-Bot"
    readbuffer=""
    
    
    d=dict()
    s=socket.socket( )
    s.connect((HOST, PORT))
    s.send("NICK %s\r\n" % NICK)
    s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
    
   
    #lecture du ficher contenant les membres du clubs secu et mise de ceux-ci dans un tableau 
    
    while 1:
        readbuffer=readbuffer+s.recv(1024)
        temp=string.split(readbuffer, "\n")
        readbuffer=temp.pop( )
        
        for line in temp:
            line=string.rstrip(line)
            line=string.split(line)

            if(line[0]=="PING"):
                s.send("PONG %s\r\n" % line[1])
            s.send("JOIN #resir\r\n")
         #connection a  irc    
            #print(line)
            
     
            d = readline(line, d)
            #print(d)

            help(d,s)
            netsec(d,s)
            netsecbrief(d,s)
            RevEngineering(d,s)
            RevEngineeringbrief(d,s)
            blackhat(d,s)
            blackhatbrief(d,s)
            malware(d,s)
            malwarebrief(d,s)

if __name__ == "__main__":
   print("Starting bot")
   run()
