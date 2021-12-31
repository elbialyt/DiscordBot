import discord
import os 
import requests 
import json
from dadjokes import Dadjoke
import random
import keep_alive

client = discord.Client()

overwatch = ["overwatch", "OW", "trash game",   ]

tarek = ["papa t", "tarek", "Tarek", "TAREK"]

responsestooverwatchs = ["DID SOMEONE SAY OW?", "i  love that game", "OW for life and dont forget it"]

responsestotarek = ["wow, that tarek guy must be good at coding", "whoever that tarek mister is he is so cool", "isn't that tarek guy Margot Robbie's boyfriend?", "Tarek is so handsome", "Didn't that Tarek guy save 3 kittens from a burning house?", ""]


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event 
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    msg = message.content

    if msg.startswith('$help'):
        await message.channel.send('This is a super cool bot Tarek coded with python.\n Commands: $dadjoke, $inspire, $who is a physics superstar')

    if msg.startswith('$who is a physics superstar'):
        await message.channel.send('JONATHAN JONATHAN JONATHAN')
    
    if msg.startswith('$dadjoke'):
      dadjoke = Dadjoke()
      await message.channel.send(dadjoke.joke)
    
    if msg.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)
    
    if any(word in msg for word in overwatch):
      await message.channel.send(random.choice(responsestooverwatchs))

    if any(word in msg for word in tarek):
      await message.channel.send(random.choice(responsestotarek))

keep_alive.keep_alive()  
  
client.run(os.getenv('TOKEN'))