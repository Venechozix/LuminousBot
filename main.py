import nextcord
import os
import random
from nextcord.ext import commands
from comandos import listas
bot_token = os.environ['token']

client = commands.Bot(command_prefix ="!")



objlista = listas.Listas()

def get_from_list(l, amount=1):
    l = list(l)
    for _ in range(amount):
        yield l.pop(random.randint(0, len(l)-1))

def main():
  for folder in os.listdir("comandos"):
    if os.path.exists(os.path.join("comandos",folder,"cog.py")):
      client.load_extension(f"comandos.{folder}.cog")  

  @client.event 
  async def on_ready():
      
      await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="a unos imbeciles "))
      
      print(" bot is online")
  
  client.run(bot_token)
if __name__ == '__main__':
    main()


  

