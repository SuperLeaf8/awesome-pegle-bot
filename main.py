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
            if m[0] in stop:
                print("stop")
                await ctx.send("Stopped")
                break
            
            else:
                # if com[m[0]] == "click": bad code
                if m[0] == com["click"]:
                    g.click()
                elif m[0] == com["right"]:
                    try:
                        g.moveRel(int(m[1]),0)
                    except:
                        pass
                elif m[0] == com["left"]:
                    try:
                        g.moveRel(int(m[1])*-1,0)
                    except:
                        pass
                elif m[0] == com["up"]:
                    try:
                        g.moveRel(0,int(m[1])*-1)
                    except:
                        pass
                elif m[0] == com["down"]:
                    try:
                        g.moveRel(0,int(m[1]))
                    except:
                        pass

@bot.command()
async def coms(ctx):
    msg = ""
    with open("com.json","r") as f:
        com = load(f)
        for i in com.keys():
            msg += f"{i}: {com[i]}\n"
    await ctx.send(msg)


@bot.command()
async def t(ctx, channelid:int):
    channel = await bot.fetch_channel(channelid)
    async with channel.typing():
        def check(m):
            return (m.author == ctx.author) and (m.channel == ctx.channel)
        try:
            msg = await bot.wait_for('message',check=check,timeout=30)
        except:
            return
        else:
            await channel.send(msg.content)


with open("token.json","r") as f:
    token = load(f)

bot.run(token)