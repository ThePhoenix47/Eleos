import subprocess
import time

def on_CTCP(bot, event):
    ctcptype = event.arguments[0].upper()
    if len(event.arguments) > 1:
        args = event.arguments[1:]
    else:
        args = []

    if ctcptype == "VERSION":
        version = subprocess.getoutput("git describe")
        bot.ctcpreply(event, ctcptype, "Eleos {0}".format(version))
    elif ctcptype == "PING":
        if len(args) > 0:
            bot.ctcpreply(event, ctcptype, repr(" ".join(args))[1:-1])
        else:
            bot.ctcpreply(event, ctcptype, time.time())