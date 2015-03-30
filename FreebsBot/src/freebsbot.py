# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import bot
import re

__author__ = "Fabien"
__date__ = "$26 mars 2015 17:41:33$"

nick = 'FreebsBot'
ident = "Freebien"
realname = nick
serv = 'irc.clubsecu.fr'
port = 6667
chan = '#flood'

if __name__ == "__main__":
    print 'FreebsBot v0.1a'
    bot = bot.Bot(serv, port, chan, nick, ident, realname)
    bot.connect()
    bot.command_join(bot.chan)
    while True:
        bot.readlines()
        for bot.line in bot.buffer:
            bot.command_ping()

            bot.privmsg = re.match(r"^:(.*)![^ ]* PRIVMSG (#[^ ]*) :(.*)$",bot.line) # Get informations about the message
            if bot.privmsg:
                # print('%s %s %s' %(m.group('nick'),m.group('chan'),m.groupe('msg')))
                # bot master
                if bot.master == bot.privmsg.group(1):
                    master_msg = re.match(r"^(" + bot.nick + r") : ([a-zA-Z]*) ([on|off]*)$",bot.privmsg.group(3))
                    if master_msg:
                        bot.trigger_turn(master_msg.group(2),master_msg.group(3))

            bot.functions(bot.line)