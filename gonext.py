import discord
import os
import time
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

timer = 0
surrenderStarted = False
surrenderVote = 0
uniqueUsers = []
lastVote = 0

async def timeOutFF(message):
    await asyncio.sleep(600)
    await message.channel.send('Surrender Vote Timed Out')
    resetFF()

def resetFF():
    global timer
    global surrenderStarted
    global uniqueUsers
    global surrenderVote
    global lastVote

    surrenderStarted = False
    surrenderVote = 0
    timer = 0
    uniqueUsers.clear()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.author.id)

    global timer
    global surrenderStarted
    global uniqueUsers
    global surrenderVote
    global lastVote
    
    if message.content.startswith('/ff'):
        print (30 - (time.time() - timer))
        # if timer == 0 or time.time() - timer < 30:
        #     if timer == 0:
        #         timer = time.time()
        #     await message.channel.send('Too early in the game to surrender. (' + str(30 - (time.time() - timer)) + ' seconds left)')
        if surrenderStarted and message.author not in uniqueUsers:
            surrenderVote += 1
            lastVote = time.time()
            uniqueUsers.append(message.author)
            if surrenderVote == 5:
                resetFF()
                await message.channel.send("Surrender Vote Successful. Defeat.")
            else: 
                await message.channel.send('Surrender Vote (' + str(surrenderVote) + '/5)')
        elif not surrenderStarted and time.time() - timer > 30:
            surrenderStarted = True
            surrenderVote += 1
            uniqueUsers.append(message.author)
            await message.channel.send('Surrender Vote Started (1/5)')
            await timeOutFF(message)
        elif surrenderStarted and message.author in uniqueUsers:
            await message.channel.send("Vote already Counted!")

    if message.content.startswith('/forceff') and message.author.id == 116354250316972040:
        resetFF()
        await message.channel.send("Surrender Vote Successful. Defeat.")
        
            

    if message.content.startswith('Scott'):
        await message.channel.send('Adelman')


client.run('')