import asyncio
import discord
from discord.ext import commands
import pyautogui as g
from json import load
from random import randint

bot = commands.Bot(command_prefix="p!")

stop = [
    "stop",
    "quit"
]

curses = [
    "fuck off",
    "lose",
    "shut up",
    "dumbass",
    "eat my shit",
    "Valued user, your input has not been recorded. Please try again."
]

def gamble(percent): # used for the rng so when someone puts in a command, there is only a chance it will register
        num = round(percent,1)
        num *= 10
        chances = range(1,num+1)
        num = randint(0,1000)
        if num in chances:
            return True
        else:
            return False

async def if_user(ctx):
        with open("properties.json","r") as f:
            data = load(f)
            user = data["user"]
            return ctx.author.id == user

class PeggleBot(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.tog = True # toggle for duel matches, if 1: players can control game
        self.running = False # to make sure no more than one instance of the command runs

        # properties // put in properties.json
        with open("properties.json","r") as f:
            data = load(f)
            if data["doRNG"]:
                self.rng = data["rng"]
            else:
                self.rng = 100
            if data["doDelay"]:
                self.delay = data["delay"]
            else:
                self.delay = 0
        self.rng = 40 # refer to gamble command
        self.delay = 0.5 # global cooldown (blame the idea on bobjeff)

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")

    @commands.command()
    async def start(self,ctx):
        if self.running:
            return
        self.running = True
        print("start")
        await ctx.send("Start")
        with open("com.json","r") as f:
            com = load(f)
            while True:
                def check_func(msg):
                    cont = False
                    msgc = msg.content.lower().split(" ")[0]
                    cont = msgc in [i for i in com.keys()]
                    return (msg.channel == ctx.channel) and (cont or (msg.content.lower() in stop)) and self.tog
                msg = await bot.wait_for('message',check=check_func)
                # print("recv",msg.content)
                m = (msg.content.lower()).split(" ")
                if m[0] in stop:
                    print("stop")
                    await ctx.send("Stopped")
                    self.running = False
                    break
                
                if gamble(self.rng):
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
                else:
                    await ctx.send(curses[randint(0,len(curses)-1)])
            await asyncio.sleep(self.delay)
        # print("helloo")

    @commands.command()
    async def coms(self,ctx):
        msg = ""
        with open("com.json","r") as f:
            com = load(f)
            for i in com.keys():
                msg += f"{i}: {com[i]}\n"
        await ctx.send(msg)


    @commands.command()
    async def t(self, ctx, channelid:int):
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

    @commands.check(if_user)
    @commands.command()
    async def toggle(self,ctx):
        self.tog = not self.tog
        await ctx.send(f"user control {self.tog}")

bot.add_cog(PeggleBot(bot))

with open("token.json","r") as f:
    token = f.read()

bot.run(token)