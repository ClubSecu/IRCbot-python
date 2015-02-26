# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import DameCore

__author__ = "canillas"
__date__ = "$26 fevr. 2015 11:38:42$"

if __name__ == "__main__":
    print "Hello World"
    #toto = DameCore.bot(host = "irc.clubsecu.fr", port = 6667, nick = "Man-Bot",realname="Man-Bot")
    tata = DameCore.bot()
    tutu = toto = DameCore.bot(host = "irc.clubsecu.fr", port = 6667, nick = "Child-Bot",realname="Man-Bot")
