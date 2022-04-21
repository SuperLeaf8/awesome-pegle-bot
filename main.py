import discord
from discord.ext import commands
import pyautogui as g
from json import load

bot = commands.Bot(command_prefix="p!")

stop = [
    "stop",
    "quit"
]

@bot.event
async def on_ready():
    print("ready")

@bot.command()
async def start(ctx):
    print("start")
    await ctx.send("Start")
    with open("com.json","r") as f:
        com = load(f)
        while True:
            def check_func(msg):
                cont = False
                msgc = msg.content.lower().split(" ")[0]
                cont = msgc in [i for i in com.keys()]
                return (msg.channel == ctx.channel) and (cont or (msg.content.lower() in stop))
            msg = await bot.wait_for('message',check=check_func)
            print("recv",msg.content)
            m = (msg.content.lower()).split(" ")
            if m in stop:
                print("stop")
                await ctx.send("Stopped")
                break
            
            else:
                if com[m[0]] == "click":
                    g.click()
                
                elif com[m[0]] == "right":
                    try:
                        g.moveRel(int(m[1]),0)
                        print("here")
                    except:
                        pass
                elif com[m[0]] == "left":
                    try:
                        g.moveRel(int(m[1])*-1,0)
                    except:
                        pass
                elif com[m[0]] == "up":
                    try:
                        g.moveRel(0,int(m[1])*-1)
                    except:
                        pass
                elif com[m[0]] == "down":
                    try:
                        g.moveRel(0,int(m[1]))
                    except:
                        pass

@bot.command
async def coms(ctx):
    msg = ""
    with open("coms.json","r") as f:
        com = load(f)
        for i in com.keys():
            msg += f"{i}: {com[i]}\n"
    await ctx.send(msg)

with open("token.json","r") as f:
    token = load(f)

bot.run(token)