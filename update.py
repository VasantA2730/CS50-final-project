#UPDATES DATABASE USING DISCORD.PY

import discord
import sqlite3
from discord.ext import commands

member_ids=[]
member_names=[]

conn=sqlite3.connect('players.db')
db=conn.cursor()
db.execute("CREATE TABLE IF NOT EXISTS players(id INTEGER PRIMARY KEY,name TEXT NOT NULL,mmr INTEGER NOT NULL DEFAULT 100)")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('bot ready')
    for guild in bot.guilds:
        if str(guild) == 'COVID-19 Bunker':
            for member in guild.members:
                member_ids.append(member.discriminator)
                member_names.append(member.name)

    i=0
    for member in member_ids:
        db.execute("INSERT OR IGNORE INTO players (id,name) VALUES(:id,:name)",{"id":int(member), "name":member_names[i]})
        db.execute("UPDATE players SET name=:name WHERE id=:id",{"name":member_names[i],"id":member})
        i+=1

    print(db.execute("SELECT * FROM PLAYERS").fetchall())
    conn.commit()
    conn.close()
    print("end")

bot.run("MTAzNzI2Mzg2MDUwMTA2OTg0NA.GKJ7Nv.TNRRZcCj3adSA9ii3YusWNQi1kE_Tdomx-NBxg")