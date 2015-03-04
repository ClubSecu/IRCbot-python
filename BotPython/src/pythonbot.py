
import sys
import socket
import string
import os
import random
import hashlib
import praw  #https://praw.readthedocs.org/en/v2.1.20/ sinon a commenter# #wrapper api reddit

def tata(line,s):
    for word in line: 
        if(word ==":TATA"):
            s.send("PRIVMSG #resir TUTU \r\n")
    

def toto(line,s):
    for word in line: 
        if(word ==":TOTO"):
            s.send("PRIVMSG #resir TATA \r\n")

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
        
def answer(d,s):
    user=""
    
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                    s.send("PRIVMSG %s %s \r\n" %(d['src'],d['msg'])) 
                else:  #si le message est prive
                    user,id = string.split(d['usr'],'!') #je decoupe l'id pour avoir le log
                    #print(user,id)
                    user=string.lstrip(user,':') # j'enleve le caractere ":" 
                    s.send("PRIVMSG %s %s \r\n" %(user,d['msg'])) 
    

def salut(d,s,NICK):
    user=""
    message=""
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'JOIN'): # je check l'action est bien join
                    user,id = string.split(d['usr'],'!') #je decoupe l'id pour avoir le loggin 
                    print(user)
                    if (user != ":"+NICK ):
                        user=string.lstrip(user,':') # j'enleve le caractere ":" de l'user
                        message = "Bienvenu dans le chat "+user 
                        target=string.lstrip(d['whr'],':') #j'enleve le caracete : de la source
                        s.send("PRIVMSG %s %s \r\n" %(target,message)) #je salue la personne 

                    
def joinClubSecu(d,s,usersec):
     
    user=""
    message=""
    ope="Nomekrax"
    opmessage=""
    buff=""
    chan="#resir"
    
    #print(usersec)
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'JOIN'): # je check l'action est bien join
                    user,id = string.split(d['usr'],'!') #je decoupe l'id pour avoir le loggin 
                    print(user,id)
                    user=string.lstrip(user,':') # j'enleve le caractere ":" de l'user
                    message = "Bienvenu dans le chat "+user 
                    target=string.lstrip(d['whr'],':') #j'enleve le caracete : de la source
                    
                    if (user in usersec): #je verifie que l'user est bien dans la liste des Users
                        opmessage="!!! "+user+" join "+chan+" ; Member of Club Secu ?"  
                        s.send("PRIVMSG %s %s \r\n" %(ope,opmessage)) #j'envoie un mp a Nomekrax pour la mettre au club secu 
                        opmessage=" - /sajoin "+user+" #clubsecu"
                        s.send("PRIVMSG %s %s \r\n" %(ope,opmessage))
                    
    

def citationLecture(d,s):
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                   
                    if(d['msg'] == "!citation "):
                       
                        fichiercitation=open("Citation","r")
                        citation=fichiercitation.read()
                        citation=citation.split("\n")
                        fichiercitation.close
                        rand = random.randint(0,len(citation))
                        message = citation[rand-1]
                        print(rand)
                        s.send("PRIVMSG #resir %s \r\n" %(message))
                      

def rules(d,s): #commentaire a changer
        if (d != None): # je verifie que mon dicto n'est pas vide
            if 'act' in d: #je verifie que mon dictio est bien forme
                if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                    if (d['src'][0] == '#'):  #si le message est sur un salon
                   
                        if(d['msg'] == "!rules "):
                       
                            fichiercitation=open("Rules","r")
                            citation=fichiercitation.read()
                            citation=citation.split("\n")
                            fichiercitation.close
                            rand = random.randint(0,len(citation))
                            message = citation[rand-1]
                            print(rand)
                            s.send("PRIVMSG #resir %s \r\n" %(message))

def citationEcriture(d,s):
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                    msg1=d['msg'].split(" ")  #on decoupe 
                    #print(msg1)
                    #print(len(msg1))
                    if (msg1[0]=="!q"):  #ici pour modifier le mode de commande (ici !q)
                        if (len(msg1) == 2):
                            fichiercitation=open("Citation","r") # j'ouvre le fichier des citations
                            citation=fichiercitation.read()  #j'extrait les citations
                            citation=citation.split("\n")#je les formates dans un tableau 
                            fichiercitation.close # je ferme le fichier
                            rand = random.randint(0,len(citation))  #j'en choisis une au hasard
                            message = citation[rand-1] #je la sauvegarde dans une variable pour traitement ? 
                            #print(rand)
                            s.send("PRIVMSG #resir %s \r\n" %(message)) #je l'envoie dans le chan resir
                        if (len(msg1)>=3): 
                            user,id = string.split(d['usr'],'!') #je decoupe l'id pour avoir le loggin 
                            print(user,id)
                            user=string.lstrip(user,':') # j'enleve le caractere ":" de l'user
                            msg1.pop(0) #je vire le !q
                            #print msg1
                            msg2=""
                            for i in range(len(msg1)): #je reconcatene le message dans une variable
                                msg2=msg2+" "+msg1[i]
                                
                            #print msg2
                            msg2=msg2+"\n" #j'ajoute un saut de ligne 
                            #msg2 = user+" a dit \""+msg2+"\"\n"
                            fichiercitation=open("Citation","a") #j'ouvre le ficher en mode "j'ecris apres"
                            fichiercitation.write(msg2) # j'ecrit le message 
                            fichiercitation.close
                            s.send("PRIVMSG #resir Citation enregistree \r\n" ) #affichage sur resir d'un message de confirmation
                            
                      
def noob(d,s):
    
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                    
                    if(d['msg'] == "!noob "):
                        message = "\"With great power comes great IR-responsabilities\""
                        s.send("PRIVMSG #resir %s \r\n" %(message))
    
    
    
    
                       
                       
                       
def bite(d,s):
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                    
                    if(d['msg'] == "!bite "):
                        
                        message = "Nomekrax say BITE it, just BITE it"
                        s.send("PRIVMSG #resir %s \r\n" %(message))
        
                
                   


def md5(d,s):#commentaire a faire 
     if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                    msg1=d['msg'].split(" ")  #on decoupe 
                    #print(msg1)
                    #print(len(msg1))
                    if (msg1[0]=="!md5"):  #ici pour modifier le mode de commande (ici !q)
                        if (len(msg1) == 3):
                            
                            m= hashlib.md5()
                            m.update(msg1[1])
                            message = m.hexdigest()  
                            message ="le code md5 de "+msg1[1]+" est "+message
                            #print message
                            s.send("PRIVMSG #resir %s \r\n" %(message)) #je l'envoie dans le chan resir
                           
def sha512(d,s): #commentaire a faire
     if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                    msg1=d['msg'].split(" ")  #on decoupe 
                    #print(msg1)
                    #print(len(msg1))
                    if (msg1[0]=="!sha512"):  #ici pour modifier le mode de commande (ici !q)
                        if (len(msg1) == 3):
                            
                            m= hashlib.sha512()
                            m.update(msg1[1])
                            message = m.hexdigest()  
                            message ="le code sha512 de "+msg1[1]+" est "+message
                            #print message
                            s.send("PRIVMSG #resir %s \r\n" %(message)) #je l'envoie dans le chan resir
    
    
    
def rulesacc(d,s): #commentaire a changer
        if (d != None): # je verifie que mon dicto n'est pas vide
            if 'act' in d: #je verifie que mon dictio est bien forme
                if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                    if (d['src'][0] == '#'):  #si le message est sur un salon
                   
                        if(d['msg'] == "!rulesacc "):
                       
                            fichiercitation=open("Ferengie","r")
                            citation=fichiercitation.read()
                            citation=citation.split("\n")
                            fichiercitation.close
                            rand = random.randint(0,len(citation))
                            message = citation[rand-1]
                            s.send("PRIVMSG #resir %s \r\n" %(message))
    

def netsec(d,s): #commentaire a faire 

    
    if (d != None): # je verifie que mon dicto n'est pas vide
            if 'act' in d: #je verifie que mon dictio est bien forme
                if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                    if (d['src'][0] == '#'):  #si le message est sur un salon
                   
                        if(d['msg'] == "!netsec "):
                            
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
                            
                            r=praw.Reddit(user_agent='python_bot')
                            submissions=r.get_subreddit('netsec').get_hot(limit=5)
                            message = "Les 5 dernieres new hot de reddit sur netsec sont : \n"
                            s.send("PRIVMSG #resir "+message+"")
                            for x in submissions: 
                                message=str(x)+"\n"
                                s.send("PRIVMSG #resir "+message+"\n")
   

def remote(d,s): #commentaire a faire
     if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                    msg1=d['msg'].split(" ")  #on decoupe 
                    #print(msg1)
                    #print(len(msg1))
                    if (msg1[0]=="!remote"):  #ici pour modifier le mode de commande (ici !q)
                        if (len(msg1) == 3):
                            
                           
                            message = msg1[1] 
                           
                            
                            s.send("PRIVMSG #resir %s \r\n" %(message)) #je l'envoie dans le chan resir
    
    
def blackhat(d,s): #commentaire a faire 
    
    if (d != None): # je verifie que mon dicto n'est pas vide
            if 'act' in d: #je verifie que mon dictio est bien forme
                if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                    if (d['src'][0] == '#'):  #si le message est sur un salon
                   
                        if(d['msg'] == "!blackhat "):
                            
                            r=praw.Reddit(user_agent='python_bot')
                            submissions=r.get_subreddit('blackhat').get_hot(limit=5)
                            message = "Les 5 dernieres new hot de reddit sur blackhat sont : \n"
                            s.send("PRIVMSG #resir "+message+"")
                            for x in submissions: 
                                message=str(x)+"\n"
                                s.send("PRIVMSG #resir "+message+"\n")
   
    

def musclor(d,s):
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                    msg1=d['msg'].split(" ")  #on decoupe 
                    #print(msg1)
                    #print(len(msg1))
                    if (msg1[0]=="!musclor"):  #ici pour modifier le mode de commande (ici !q)
                        if (len(msg1) == 2):
                            fichiercitation=open("Musclor","r") # j'ouvre le fichier des citations
                            citation=fichiercitation.read()  #j'extrait les citations
                            citation=citation.split("\n")#je les formates dans un tableau 
                            fichiercitation.close # je ferme le fichier
                            rand = random.randint(0,len(citation))  #j'en choisis une au hasard
                            message = citation[rand-1] #je la sauvegarde dans une variable pour traitement ? 
                            #print(rand)
                            s.send("PRIVMSG #resir %s \r\n" %(message)) #je l'envoie dans le chan resir
                        if (len(msg1)>=3): 
                            user,id = string.split(d['usr'],'!') #je decoupe l'id pour avoir le loggin 
                            print(user,id)
                            user=string.lstrip(user,':') # j'enleve le caractere ":" de l'user
                            msg1.pop(0) #je vire le !q
                            #print msg1
                            msg2=""
                            for i in range(len(msg1)): #je reconcatene le message dans une variable
                                msg2=msg2+" "+msg1[i]
                                
                            #print msg2
                            msg2=msg2+"\n" #j'ajoute un saut de ligne 
                            #msg2 = user+" a dit \""+msg2+"\"\n"
                            fichiercitation=open("Musclor","a") #j'ouvre le ficher en mode "j'ecris apres"
                            fichiercitation.write(msg2) # j'ecrit le message 
                            fichiercitation.close
                            s.send("PRIVMSG #resir Musclor vous salue ! \r\n" ) #affichage sur resir d'un message de confirmation


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
    
    fichierusersec=open("Users","r") #lien du fichier et mode ici r = read , w = write
    #fichierop=open("OP","r")
    usersec = fichierusersec.read()
    usersec = usersec.split("\n")
    fichierusersec.close
    
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
         #connection a  irc    
            print(line)
            
          #affichage de debug 
          
          #debut des actions avec "line" comme flux de donnee 

      
            d = readline(line, d)
            print(d)
            #answer(d,s)
            
            salut(d, s,NICK)
            joinClubSecu(d,s,usersec)
            #citationLecture(d, s)
            citationEcriture(d,s)
            bite(d, s)
            noob(d, s)
            rules(d,s)
            md5(d,s)
            sha512(d,s)
            rulesacc(d,s)
            netsec(d,s)
            netsecbrief(d,s)
            remote(d,s)
            blackhat(d,s)
            musclor(d,s)

            
            
           
            
           